#!/usr/bin/env python3
"""Check the workflow's portable docs and historical evidence without network calls."""
import argparse
import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
FILES = ['README.md'] + [f'README_{x}.md' for x in
    ['es', 'pt', 'ja', 'ko', 'de', 'fr', 'tr', 'zh-TW', 'zh-CN', 'ru']]
CASE_IDS = [1, 2, 10, 19, 5, 6, 15, 16, 26, 3, 4, 12, 13, 14, 25, 27,
            7, 8, 11, 20, 9, 17, 24, 18, 21, 22]


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True)


def slug(text):
    text = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', text)
    return re.sub(r'[^\w\- ]', '', text.lower()).replace(' ', '-')


def fenced(text):
    return re.findall(r'^```[^\n]*\n(.*?)^```', text, re.M | re.S)


def historical(text):
    return text[text.index('## 🎥'):text.index('## 🌟')]


def destinations(text):
    # Strip code before extracting structured links; do not swallow adjacent CJK.
    text = re.sub(r'^```[^\n]*\n.*?^```', '', text, flags=re.M | re.S)
    return re.findall(r'\]\(([^\s)]+)\)|(?:href|src|poster)=[\"\']([^\"\']+)', text)


def media(text):
    return Counter(re.findall(r'(?:src|poster)=[\"\']([^\"\']+)', historical(text)))


def check(base=None):
    failures = []
    tracked = set(git('ls-tree', '-r', '--name-only', 'HEAD').splitlines())
    readmes = [ROOT / name for name in FILES]
    assert len(list(ROOT.glob('README*.md'))) == len(FILES), 'Expected 11 READMEs'
    shared_code = None
    total_relative = 0
    for path in [*readmes, *sorted((ROOT / 'docs').glob('*.md'))]:
        text = path.read_text()
        explicit = re.findall(r'<a id="([^"]+)"', text)
        headings = re.findall(r'^#{1,6} (.+)$', text, re.M)
        anchors = set(explicit) | {slug(x) for x in headings}
        if len(explicit) != len(set(explicit)):
            failures.append(f'{path.name}: duplicate explicit anchor')
        if text.count('```') % 2:
            failures.append(f'{path.name}: unbalanced fences')
        if path in readmes:
            ids = [int(x) for x in re.findall(r'<a id="case-(\d+)"', text)]
            if ids != CASE_IDS:
                failures.append(f'{path.name}: historical case order/count changed')
            code = fenced(text[:text.index('<a id="community-examples">')])
            if shared_code is None:
                shared_code = code
            if code != shared_code:
                failures.append(f'{path.name}: current tutorial code differs from English')
            for required in ['2026-10-21', 'seedance-2.5-image-to-video',
                             'image_urls', '"adaptive"', 'draft_expires_at',
                             'seedance-2.5-draft-to-video', '@evolinkai/cli@latest']:
                if required not in text:
                    failures.append(f'{path.name}: missing {required}')
            if 'launch/seedance-2-5' in text or 'Send to Video' in text:
                failures.append(f'{path.name}: obsolete launch/UI route')
            if base:
                old = git('show', f'{base}:{path.name}')
                if fenced(historical(old)) != fenced(historical(text)):
                    failures.append(f'{path.name}: changed historical prompt bytes')
                if media(old) != media(text):
                    failures.append(f'{path.name}: historical case media changed')
                sources = lambda s: set(re.findall(r'https://x.com/[^\s)\"<>]+', s))
                if sources(old) != sources(text):
                    failures.append(f'{path.name}: creator source links changed')
                old_show = old[old.index('## 🌟'):old.index('## 💡')]
                new_show = text[text.index('## 🌟'):text.index('<a id="parameters">')]
                if old_show.rstrip() != new_show.rstrip():
                    failures.append(f'{path.name}: creator showcase changed')
        for pair in destinations(text):
            target = next(x for x in pair if x)
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                if parsed.netloc == 'evolink.ai':
                    for key in ['utm_source=github', 'utm_medium=', 'utm_campaign=', 'utm_content=']:
                        if key not in parsed.query:
                            failures.append(f'{path.name}: missing attribution {target}')
                continue
            total_relative += 1
            dest = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            rel = str(dest.relative_to(ROOT))
            if not dest.exists() and rel not in tracked:
                failures.append(f'{path.name}: missing target {target}')
                continue
            if parsed.fragment and (not parsed.path or dest.suffix == '.md'):
                dest_text = text if dest == path else dest.read_text()
                dest_anchors = anchors if dest == path else (
                    set(re.findall(r'<a id="([^"]+)"', dest_text)) |
                    {slug(x) for x in re.findall(r'^#{1,6} (.+)$', dest_text, re.M)})
                if unquote(parsed.fragment) not in dest_anchors:
                    failures.append(f'{path.name}: missing anchor {target}')
        # Tables: unescaped pipes inside code or links are not extra columns.
        width = None
        in_code = False
        for line in text.splitlines():
            if line.startswith('```'):
                in_code = not in_code
            if in_code or not line.startswith('|'):
                width = None
                continue
            columns = len(re.split(r'(?<!\\)\|', line))
            if width and columns != width:
                failures.append(f'{path.name}: inconsistent Markdown table: {line[:90]}')
            width = columns
    if failures:
        raise SystemExit('\n'.join(failures))
    print(json.dumps({'readmes': len(FILES), 'cases_per_locale': len(CASE_IDS),
        'relative_links_checked': total_relative, 'historical_base': base,
        'result': 'passed'}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--base', help='Known baseline commit for source/media/prompt preservation')
    check(parser.parse_args().base)
