# Maintaining this workflow guide

## Source of truth

- `README.md` is the English source; the ten `README_<locale>.md` files carry the same current workflow, route boundaries and historical case inventory
- Current instructions use EvoLink model/API documentation and the current MCP/CLI setup page; record the verification date when changing status or parameters
- Community examples keep their original source URL, author, media, model/platform description and fenced prompt text. They are not automatically verified EvoLink outputs
- The new tutorial in `docs/api-workflow.md` is explicitly repository-authored instructional material. Do not attach a community creator's name to these new prompts
- Historical case IDs are stable, including the existing gap at 23. Do not renumber externally linked cases; use explicit `case-N` anchors
- Creator media remain at their existing repository/GitHub attachment locations. Updating routing text does not authorize replacing or relabelling those outputs

## Update checklist

1. Inspect the current default branch and existing worktree before editing
2. Verify the exact model ID, media fields, route restrictions, task/result schema and setup commands against current sources
3. Distinguish public availability, schema validation, mock execution and a real paid generation; report each accurately
4. Preserve source posts, creator links, media and historical prompt bytes. Add a migration note instead of relabelling a 2.0 result as 2.5
5. Keep case summaries evidence-bounded. Grid layouts, prompt length, cost ratios and identity preservation require measured evidence before making guarantees
6. Update all eleven READMEs together. Translate explanatory prose; keep the shared runnable code and example prompt blocks identical
7. Rebuild Menu links and check both explicit IDs and heading fragments
8. Check local media against the Git tree, since a sparse checkout may not materialize `images/`
9. Audit every new or changed external destination, distinguish login-required pages from broken public links, and keep creator source URLs free of EvoLink attribution parameters
10. Run the relevant checks below; record limitations in the PR. Never call mock execution a real API test

## Validation

```bash
python3 scripts/verify_workflow_docs.py
bash -n examples/tasks.sh
python3 -m unittest discover -s tests -v
git diff --check
```

The documentation validator checks all eleven inventories, navigation, relative targets, shared code, current parameter fields and historical source/prompt preservation against a supplied base when available. The helper tests use a fake transport to exercise polling, failure, duplicate submission and download behavior; they do not spend credits or establish live account access.

## Community case format

Keep an explicit `<a id="case-N"></a>` before the case heading, the original linked title and author, followed by an EvoLink adaptation note. Select I2V for an actual first frame and R2V for identity/storyboard references; explain changes to media and duration when reproducing a case. Keep showcase-only posts labelled as examples rather than inventing missing prompts.

## Attribution

EvoLink navigation links use `utm_source=github`, a placement-specific `utm_medium`, campaign `GPT-Image-2-Seedance-2.5-Workflow`, and `utm_content` identifying the placement. API endpoints, the MCP server address, GitHub source links and media URLs are not marketing navigation links. Keep attribution out of those technical and creator URLs.
