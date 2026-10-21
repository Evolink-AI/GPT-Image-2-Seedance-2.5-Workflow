# Product photo → GPT Image 2 → Seedance 2.5

Create one product scene, approve its composition, and animate it into a five-second silent shot. This is a repository-authored tutorial, not a community creator's prompt or a claimed live generation result. Documentation and model schemas were checked on 2026-10-21; account access, output quality and settled charges still need your own validation.

## Before you start

- Use Bash, Python 3 for the optional checks, `jq`, and curl 7.76+ (`--fail-with-body` support)
- [Create an account](https://evolink.ai/signup?utm_source=github&utm_medium=docs&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=signup), fund generation, and obtain an [API key](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=docs&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=api_key)
- Set `EVOLINK_API_KEY` in your environment; do not commit it or paste it into public issues
- Prepare a product photo you have permission to use, available as a direct public JPEG/PNG/WebP URL; a local path or a page containing an image is not an image URL
- Check [current model pricing](https://evolink.ai/seedance-2-5?utm_source=github&utm_medium=docs&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=pricing) before submitting. Image charges depend on token use and settings; the final image cost may be known only after generation. Image, video, draft and final are separate billable tasks

Run the following steps from the repository root. Use a new working directory for a deliberately new run; keep receipts from earlier runs for recovery. The helper refuses to submit again if its receipt directory already exists.

```bash
source examples/tasks.sh
mkdir -p workflow-output
cd workflow-output
export PRODUCT_IMAGE_URL="https://your-public-host.example/product.jpg"
```

Replace the example domain before running. The snippets below submit paid tasks only when you execute `submit_task`; inspect each payload and approve its cost first. The helper never automatically retries creation. If a submission times out before a task ID is returned, inspect the saved response and your account's task history before considering another submission.

## 1. Generate one product scene

This prompt asks the image model to preserve product details; verify the result rather than treating that instruction as a guarantee. A single scene makes it easy to inspect the first frame. Storyboard grids have a different role; see [video route selection](#choose-a-video-route).

```bash
jq -n --arg product "$PRODUCT_IMAGE_URL" '{
  model: "gpt-image-2",
  prompt: "Create one 16:9 studio product photograph using the supplied product photo. Keep the product shape, label and colors as close to the reference as possible. Place it upright on a neutral stone pedestal, soft side lighting, clean background, room for later ad copy. One scene, no storyboard grid, no added text or extra products.",
  image_urls: [$product], size: "16:9", resolution: "1K",
  quality: "medium", output_format: "png", n: 1
}' > image-request.json

# Inspect image-request.json and approve this image generation before running:
submit_task images image-request.json image-receipt
wait_task "$(cat image-receipt/task-id.txt)" image-result.json
download_result image-result.json product-scene.png
```

Open `product-scene.png`. Check label spelling, shape, product count, framing and image dimensions. Fix the image before paying for motion if it is wrong. Each deliberate regeneration needs a new receipt directory and incurs its own charge.

The image-to-video input must meet its own limits: 300–6000 px per side, width/height ratio 0.4–2.5, at most 30 MB. A GPT Image 2 result that works as an image is not automatically valid as a video input. The selected 16:9 1K setting is intended to fit these limits; inspect the actual file, resize if necessary, upload the changed file and use its new public URL.

Source: [GPT Image 2 API](https://evolink.ai/docs/en/api-manual/image-series/gpt-image-2/gpt-image-2-image-generation?utm_source=github&utm_medium=docs&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=image_docs)

## 2. Animate the approved image

Continue only after reviewing the scene. The API I2V route accepts the first-frame image's proportions through `adaptive`; it does not accept a fixed `16:9` parameter. Silence is explicit here.

```bash
APPROVED_IMAGE_URL=$(jq -er '.results[0]' image-result.json)
jq -n --arg image "$APPROVED_IMAGE_URL" '{
  model: "seedance-2.5-image-to-video",
  prompt: "Five-second studio product shot. The product remains stationary on the pedestal. The camera makes one gentle push-in, with soft reflections moving naturally across the surface. Keep the product geometry and label as close to the first frame as possible. No added text, no dialogue, no music.",
  image_urls: [$image], duration: 5, quality: "720p",
  aspect_ratio: "adaptive", generate_audio: false, output_format: "mp4"
}' > video-request.json

# Inspect video-request.json and approve this video generation before running:
submit_task videos video-request.json video-receipt
wait_task "$(cat video-receipt/task-id.txt)" video-result.json
download_result video-result.json product-video.mp4
```

If you edited or re-uploaded the scene, replace `APPROVED_IMAGE_URL` with that file's URL before building the video payload. Returning a task ID means the task was accepted, not completed. A completed result is still subject to visual review: check product deformation, unwanted cuts, camera movement and silence. Add final typography and music in editing if needed. Save results promptly; generated asset links are temporary, normally valid for 24 hours.

Sources: [Seedance 2.5 I2V](https://evolink.ai/docs/en/api-manual/video-series/seedance2.5/seedance-2.5-image-to-video?utm_source=github&utm_medium=docs&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=video_docs), [task status and result fields](https://evolink.ai/docs/en/api-manual/task-management/get-task-detail?utm_source=github&utm_medium=docs&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=task_docs)

## Optional: draft to final

Choose this branch **instead of** the normal video submission above if you want to review a 480p draft before paying for a 1080p final. The draft is charged at the relevant 480p rate, and conversion is charged separately at the relevant 1080p rate; it is not a free upgrade or a guarantee of lower total cost.

```bash
jq '.quality = "480p" | .draft = true' video-request.json > draft-request.json
# Approve the draft charge, then submit once:
submit_task videos draft-request.json draft-receipt
wait_task "$(cat draft-receipt/task-id.txt)" draft-result.json
download_result draft-result.json product-draft.mp4
jq '{id, status, draft_expires_at, usage}' draft-result.json
```

Review the draft before continuing. Use its returned `draft_expires_at`; the default is 24 hours after completion, and expiration while queued can also fail conversion. A 503 `draft_unavailable` means stop or explicitly choose normal generation and its cost. Do not silently switch routes or submit duplicate paid requests.

```bash
DRAFT_TASK_ID=$(jq -er 'select(.status == "completed") | .id' draft-result.json)
jq -n --arg source "$DRAFT_TASK_ID" '{
  model: "seedance-2.5-draft-to-video",
  source_task_id: $source, output_format: "mp4"
}' > final-request.json

# Approve the separate 1080p charge and check expiry before running:
submit_task videos final-request.json final-receipt
wait_task "$(cat final-receipt/task-id.txt)" final-result.json
download_result final-result.json product-final.mp4
```

Conversion inherits the draft's creative settings. Do not add a new prompt, media, duration or quality to the conversion request. To change the scene or motion, create and review a new draft. Inspect the final output independently.

The conversion route's MP4 uses 10-bit HEVC; playback needs a compatible player. If your editor requires MOV, request `output_format: "mov"` on the conversion itself; it does not inherit the draft's container choice.

Source: [Draft-to-Video API](https://evolink.ai/docs/en/api-manual/video-series/seedance2.5/seedance-2.5-draft-to-video?utm_source=github&utm_medium=docs&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=draft_docs)

## Choose a video route

The per-case notes in the READMEs suggest a route for adapting each historical idea, not a tested reproduction of its output.

| Intended use of the input | Route | How to adapt a community example |
| --- | --- | --- |
| A finished first frame, or first and last frames | `seedance-2.5-image-to-video` | Use one scene as the first frame; crop a single panel out of a grid if necessary. Two URLs define first/last frames, not two arbitrary style references |
| Character sheets, product identity, storyboard sequence, style or motion references | `seedance-2.5-reference-to-video` | Explain each asset's role with `@image1`, `@video1`, `@audio1`. A grid is sequence guidance; exact panel timing/order is not guaranteed |
| Change an existing video's content | `seedance-2.5-video-edit` | Supply the target video, `duration: -1` and `aspect_ratio: "adaptive"` |
| Continue an existing video | `seedance-2.5-video-extend` | Supply the target video and `aspect_ratio: "adaptive"`; review continuity between generated segments |
| Generate without media | `seedance-2.5-text-to-video` | Use a textual scene and motion description; do not add media URL arrays |

I2V, T2V, R2V and Extend support 4–30 seconds or automatic duration `-1`; Edit follows the input with `-1`. The example uses a fixed five seconds for a predictable requested duration. Current API resolutions are 480p, 720p and 1080p. For a one-second edited shot, generate a supported clip and trim it; for a 35–50 second choreography, split, assemble or extend. Describing `24fps` in a historical prompt does not expose a frame-rate setting.

Check each route's current schema and prices. R2V with video input, Edit and Extend use video-input billing, which includes input time and output time; do not apply an output-only I2V estimate to them. Consult the [parameter guide](https://evolink.ai/docs/en/api-manual/video-series/seedance2.5/seedance-2.5-overview?utm_source=github&utm_medium=docs&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=route_docs) before changing workflows.

## Recovery and errors

| Symptom | Next action |
| --- | --- |
| 401 / 403 | Check the selected key and account/model permission |
| 402 | Check balance and billing before submitting another generation |
| 400 | Check `image_urls`, public file access, dimensions and `adaptive`; Draft requires top-level `draft: true` with 480p |
| 429 or a transient GET failure | Stop the local poll; resume querying the same task later |
| Creation times out with no ID | Keep the receipt directory, inspect the saved response and account history; submission outcome may be unknown |
| Task `failed` | Read `.error`; fix the cause before deliberately creating a new paid task |
| Waiting times out | Resume the same task ID; the server task can keep running after local waiting stops |
| Draft conversion expires | The old draft cannot be converted; a new draft is a new paid generation |
| Output is wrong | Revise deliberately; each regeneration or conversion is a separate task |

Resume without creating anything:

```bash
wait_task "$(cat video-receipt/task-id.txt)" video-result.json
download_result video-result.json product-video.mp4
jq '.usage' video-result.json
```

## Using an agent instead

[Connect EvoLink MCP or set up the CLI](https://evolink.ai/mcp?utm_source=github&utm_medium=docs&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=agent_setup). The CLI's companion skill handles discovery, inputs, quotes and task tracking; use the prompt in your language's README. Browser OAuth setup is separate from the raw API key used by the curl examples. Do not paste API keys into the agent conversation for CLI setup.

The legacy `npx evolink-seedance` package targets Seedance 2.0; installing it does not establish 2.5 support. This documentation update does not change or publish that package.
