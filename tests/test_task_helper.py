"""Exercise task receipts and recovery using a fake curl, never a paid API."""
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

HELPER = Path(__file__).resolve().parents[1] / 'examples' / 'tasks.sh'
FAKE_CURL = '''#!/usr/bin/env python3
import json,os,sys
from pathlib import Path
a=sys.argv[1:]
with open(os.environ['CALL_LOG'],'a') as f: f.write(json.dumps(a)+'\\n')
out=a[a.index('--output')+1]
if '--request' in a:
    result={'id':'task-test-123','status':'pending'}
else:
    result=json.loads(os.environ.get('FAKE_RESULT','{"status":"completed","results":["https://assets.example/video.mp4"]}'))
Path(out).write_text(json.dumps(result))
sys.exit(int(os.environ.get('FAKE_EXIT','0')))
'''


class TaskHelperTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'curl').write_text(FAKE_CURL)
        (self.root / 'curl').chmod(0o755)
        self.env = dict(os.environ, PATH=str(self.root)+os.pathsep+os.environ['PATH'],
                        EVOLINK_API_KEY='fake-test-only', CALL_LOG=str(self.root/'calls'))
        (self.root/'request.json').write_text('{"model":"seedance-2.5-image-to-video"}')

    def run_bash(self, code, **env):
        return subprocess.run(['bash', '-c', 'source "$1"; '+code, 'test', str(HELPER)],
            cwd=self.root, env=dict(self.env, **env), text=True, capture_output=True)

    def calls(self):
        path = self.root/'calls'
        return [json.loads(x) for x in path.read_text().splitlines()] if path.exists() else []

    def test_creation_saves_id_and_refuses_duplicate(self):
        result = self.run_bash('submit_task videos request.json receipt')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.root/'receipt/task-id.txt').read_text().strip(), 'task-test-123')
        duplicate = self.run_bash('submit_task videos request.json receipt')
        self.assertNotEqual(duplicate.returncode, 0)
        self.assertEqual(len(self.calls()), 1)

    def test_completed_poll_does_not_create(self):
        result = self.run_bash('wait_task task-test-123 result.json 1')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(self.calls()), 1)
        self.assertNotIn('--request', self.calls()[0])

    def test_failed_task_stops_without_resubmitting(self):
        result = self.run_bash('wait_task task-test-123 result.json 1',
            FAKE_RESULT='{"status":"failed","error":{"code":"invalid_media"}}')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('invalid_media', result.stderr)
        self.assertEqual(len(self.calls()), 1)

    def test_timeout_retains_original_id_without_post(self):
        result = self.run_bash('sleep() { SECONDS=$((SECONDS + 2)); }; wait_task task-test-123 result.json 1',
            FAKE_RESULT='{"status":"processing"}')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('task-test-123', result.stderr)
        self.assertTrue(all('--request' not in x for x in self.calls()))

    def test_transport_failure_retains_receipt(self):
        result = self.run_bash('submit_task videos request.json receipt', FAKE_EXIT='28')
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue((self.root/'receipt/request.json').exists())
        self.assertTrue((self.root/'receipt/created.json').exists())
        self.assertEqual(len(self.calls()), 1)
        self.assertIn('do not automatically repeat POST', result.stderr)

    def test_download_uses_result_without_credentials(self):
        (self.root/'result.json').write_text('{"status":"completed","results":["https://assets.example/video.mp4"]}')
        result = self.run_bash('download_result result.json video.mp4')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn('--header', self.calls()[0])
        self.assertNotIn('fake-test-only', str(self.calls()))

    def test_unexpected_status_stops(self):
        result = self.run_bash('wait_task task-test-123 result.json 1', FAKE_RESULT='{"status":"unknown"}')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Unexpected status', result.stderr)


if __name__ == '__main__':
    unittest.main()
