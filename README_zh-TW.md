<div align="center">

<a href="https://evolink.ai/seedance-2-5?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=banner"><img src="images/workflow-banner.png" alt="GPT Image 2 × Seedance 2.5 工作流程指南"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![awesome-seedance-2.5-prompts](https://img.shields.io/badge/📦_awesome--seedance--2.5--prompts-181717?logo=github)](https://github.com/EvoLinkAI/awesome-seedance-2.5-prompts)
[![EvoLink MCP / CLI](https://img.shields.io/badge/EvoLink-MCP%20%2F%20CLI-181717)](https://evolink.ai/mcp?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=top_badge)
[![awesome-seedance-2.5-guide](https://img.shields.io/badge/📦_awesome--seedance--2.5--guide-181717?logo=github)](https://github.com/EvoLinkAI/awesome-seedance-2.5-guide)
[![awesome-gpt-image-2-prompts](https://img.shields.io/badge/📦_awesome--gpt--image--2--prompts-181717?logo=github)](https://github.com/EvoLinkAI/awesome-gpt-image-2-prompts)


[![🇺🇸 English](https://img.shields.io/badge/🇺🇸_English-Default_Source-111111)](README.md)
[![🇪🇸 Español](https://img.shields.io/badge/🇪🇸_Español-Ver-ffb703)](README_es.md)
[![🇵🇹 Português](https://img.shields.io/badge/🇵🇹_Português-Ver-2a9d8f)](README_pt.md)
[![🇯🇵 日本語](https://img.shields.io/badge/🇯🇵_日本語-表示-52b788)](README_ja.md)
[![🇰🇷 한국어](https://img.shields.io/badge/🇰🇷_한국어-보기-4ea8de)](README_ko.md)
[![🇩🇪 Deutsch](https://img.shields.io/badge/🇩🇪_Deutsch-Ansehen-f4a261)](README_de.md)
[![🇫🇷 Français](https://img.shields.io/badge/🇫🇷_Français-Voir-e76f51)](README_fr.md)
[![🇹🇷 Türkçe](https://img.shields.io/badge/🇹🇷_Türkçe-Görüntüle-d62828)](README_tr.md)
[![🇹🇼 繁體中文](https://img.shields.io/badge/🇹🇼_繁體中文-查看-8338ec)](README_zh-TW.md)
[![🇨🇳 简体中文](https://img.shields.io/badge/🇨🇳_简体中文-查看-ef476f)](README_zh-CN.md)
[![🇷🇺 Русский](https://img.shields.io/badge/🇷🇺_Русский-Смотреть-577590)](README_ru.md)

</div>

# GPT Image 2 × Seedance 2.5

先用 GPT Image 2 確認畫面，再用 Seedance 2.5 生成影片，適用於產品廣告、角色鏡頭與分鏡，提供 Agent 與 API 兩種操作路線

> 文件與 schema 核對日期為 2026-10-21，新教學是倉庫編寫的示例，未宣稱完成真實生成或效能實測

<a id="quick-start"></a>
## 快速開始

**Seedance 2.5 — 已在 EvoLink 開放**

[EvoLink MCP / CLI](https://evolink.ai/mcp?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=agent_setup) · [Seedance 2.5](https://evolink.ai/seedance-2-5?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=model) · [API key](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=api_key) · [Sign up](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=signup)

支援遠端 MCP 的客戶端請依設定頁連線；終端 Agent 使用下方 CLI（需要 Node.js 22+），在瀏覽器登入後安裝配套 Skill，每次生成前先查詢兩個指定模型的素材要求、參數與費用

```bash
npm install -g @evolinkai/cli@latest
evolink auth login
evolink skills install
evolink models schema gpt-image-2 --json
evolink models schema seedance-2.5-image-to-video --json
```

```text
Use EvoLink to turn my product photo into a five-second product video.
Use GPT Image 2 for one 16:9 scene, then Seedance 2.5 for animation.
Check current inputs, parameters and costs first; ask me before each paid task.
Show me the image before creating the video. Keep the product still and use
a gentle camera push-in. No dialogue or music; request silent video.
Inspect product details instead of promising exact logo or identity preservation.
Pass the approved image URL as the first frame with aspect_ratio=adaptive.
Poll the original task ID, then return the video and save a local copy.
```

<a id="product-workflow"></a>
## 產品圖到影片

準備有權使用的產品圖及公開圖片 URL，也可讓 Agent 先上傳本機檔案；用 GPT Image 2 生成一張 16:9 產品場景圖；檢查產品、Logo、構圖與圖片尺寸；將確認後的圖片結果 URL 作為 Seedance 2.5 首幀；持續查詢原 Task ID，完成後儲存影片，再用剪輯工具加入最終文字

[完整 API 操作教學（英文）](docs/api-workflow.md) · [GPT Image 2 API](https://evolink.ai/docs/en/api-manual/image-series/gpt-image-2/gpt-image-2-image-generation?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=image_docs) · [Seedance 2.5 I2V API](https://evolink.ai/docs/en/api-manual/video-series/seedance2.5/seedance-2.5-image-to-video?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=video_docs)

```bash
# Set EVOLINK_API_KEY in your environment; use a real approved image URL.
export APPROVED_IMAGE_URL="https://your-public-host.example/approved-scene.png"
jq -n --arg image "$APPROVED_IMAGE_URL" '{
  model: "seedance-2.5-image-to-video",
  prompt: "Five-second product shot. The product stays still; gentle camera push-in. No dialogue or music.",
  image_urls: [$image], duration: 5, quality: "720p",
  aspect_ratio: "adaptive", generate_audio: false
}' > video-request.json
curl --fail-with-body --request POST \
  https://api.evolink.ai/v1/videos/generations \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-binary @video-request.json --output video-created.json
# Save .id from video-created.json; task creation is not video completion.
```

<a id="draft-workflow"></a>
## 選用：樣片轉正式片

影片請求頂層設定 `draft: true`、`quality: "480p"`，檢查完成的樣片後，將其任務 ID 作為 `source_task_id` 提交至 `seedance-2.5-draft-to-video` 生成 1080p 正式片，兩次請求分別收費；預設樣片完成後 24 小時內可轉，以返回的 `draft_expires_at` 為準並預留排隊時間；樣片模式不可用時應停止，或明確選擇一般生成及其費用

```json
{
  "model": "seedance-2.5-draft-to-video",
  "source_task_id": "YOUR_COMPLETED_UNEXPIRED_DRAFT_TASK_ID",
  "output_format": "mp4"
}
```

[Draft → 1080p](docs/api-workflow.md#optional-draft-to-final) · [Pricing](https://evolink.ai/seedance-2-5?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=pricing)

<a id="community-examples"></a>
## 歷史社群案例

保留案例原有模型與平台描述、提示詞、作者連結與媒體，Seedance 2.0 案例是歷史參考，不能視為 Seedance 2.5 API 實測；過往倉庫編輯留下的模型標註尚未全部逐帖核對，請依各案例的遷移說明重新生成並驗收；原提示詞的創作要求不等於 API 參數契約

<a id="menu"></a>
## 📑 目錄

- [快速開始](#quick-start)
- [產品圖到影片](#product-workflow)
- [選用：樣片轉正式片](#draft-workflow)
- [歷史社群案例](#community-examples)
- [參數與實際檢查](#parameters)
- [相關資源](#related-resources)
- [🎥 分鏡技巧](#-分鏡技巧)
  - [Case 1: 標準分鏡 → 影片（by @kiyoshi_shin）](#case-1)
  - [Case 2: 3×3 宮格分鏡法（by @servasyy_ai）](#case-2)
  - [Case 10: 多幀參考 → 快剪影片（by @heygentlewhale）](#case-10)
  - [Case 19: 分鏡優先的成本控管（by @0xbisc）](#case-19)
- [📱 商業與產品](#-商業與產品)
  - [Case 5: App MVP 展示影片（by @Shin_Engineer）](#case-5)
  - [Case 6: 15 秒商業廣告（by @ai_mitosan）](#case-6)
  - [Case 15: 奢華廣告 — 分鏡到成片（by @insmind_com）](#case-15)
  - [Case 16: 電影感美食影片（by @kingofdairyque）](#case-16)
  - [Case 26: 商品圖 → 短影音廣告（by @insmind_com）](#case-26)
- [🎨 動畫與角色](#-動畫與角色)
  - [Case 3: 角色三視圖 → 動畫（by @YaReYaRu30Life）](#case-3)
  - [Case 4: 動畫 OP 風格影片（by @Toshi_nyaruo_AI）](#case-4)
  - [Case 12: Claude Code × 角色設定圖 → 動畫（by @old_pgmrs_will）](#case-12)
  - [Case 13: 舞蹈序列宮格 → 舞蹈影片（by @Ciri_ai）](#case-13)
  - [Case 14: 漫畫頁 → 動畫影片（by @nimentrix）](#case-14)
  - [Case 25: K-Pop 編舞 — 精細控制（by @Kashberg_0）](#case-25)
  - [Case 27: 角色登場動畫（by @0xbisc）](#case-27)
- [🎵 音樂影片與短片](#-音樂影片與短片)
  - [Case 7: 結合 Suno 的音樂影片（by @fukaborichannel）](#case-7)
  - [Case 8: 賽博龐克風格短片（by @ponyodong）](#case-8)
  - [Case 11: 日系 MV — 全 AI 工具鏈（by @Tz_2022）](#case-11)
  - [Case 20: Claude 鏡頭表 → 音樂影片（by @CoffeeVectors）](#case-20)
- [🎮 遊戲概念](#-遊戲概念)
  - [Case 9: 遊戲與互動內容（by @op7418）](#case-9)
  - [Case 17: 遊戲介面動畫 — 完整流程（by @0xInk_）](#case-17)
  - [Case 24: GTA 風格城市遊戲概念（by @markgadala）](#case-24)
- [🛠 製作工具](#-製作工具)
  - [Case 18: 單一 Agent 自動化工作流程（by @venturetwins）](#case-18)
  - [Case 21: 選角宮格 — 演員試鏡（by @8fstudioz）](#case-21)
  - [Case 22: 3D 雕塑 → AI 渲染 → 動畫（by @_DAntunes_）](#case-22)
- [🌟 社群精選](#-社群精選)

## 🎥 分鏡技巧

<!-- Case 1: Standard Storyboard → Video (by @kiyoshi_shin) -->
<a id="case-1"></a>
### Case 1: [標準分鏡 → 影片](https://x.com/kiyoshi_shin/status/2047133524403400847)（by [@kiyoshi_shin](https://x.com/kiyoshi_shin)）

> **EvoLink 重現路線:** `seedance-2.5-image-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

最常見的工作流程。先用 GPT Image 2 生成分鏡畫面，再交給 Seedance 2.0 製作動畫。非常適合宣傳影片、短篇劇情與動畫 OP。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/storyboard_case1/input.jpg" width="280" alt="GPT Image 2 生成的分鏡"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/ac25fc3d-b6cb-4149-a8ba-e7e10c5b1faa" width="280" controls></video></td>
</tr></table>

**步驟：**

1. 向 GPT Image 2 描述你的場景並生成分鏡圖
2. 在 Seedance 2.0 的 Image-to-Video 模式中匯入分鏡圖
3. 匯出各段片段後，在剪輯軟體中組裝

**GPT Image 2 提示詞：**

```
Create a 6-panel storyboard for a 15-second brand promotional video. Label each panel with a shot description.
Style: cinematic, cool color tone, widescreen 16:9.
Content: the journey of a product from factory to the customer's hands.
```

**Seedance 2.0 提示詞：**

```
Cinematic brand advertisement, slow camera push-in, product centered in frame, warm side lighting, soft background blur, no people, 3 seconds.
```

> [!NOTE]
> 目前 2.5 單次生成 4–30 秒，較短鏡頭在剪輯時裁切；I2V 僅接受 adaptive，請預先設定圖片比例；提示詞中的 24fps 不是 API 幀率參數


<!-- Case 2: 3×3 Grid Storyboard Method (by @servasyy_ai) -->
<a id="case-2"></a>
### Case 2: [3×3 宮格分鏡法](https://x.com/servasyy_ai/status/2047198012750143999)（by [@servasyy_ai](https://x.com/servasyy_ai)）

> **EvoLink 重現路線:** `seedance-2.5-reference-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

這是社群嘗試的網格方法，可用於表達順序意圖，但倉庫沒有對照測試證明失敗率更低或動作更準確

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/storyboard_case2/output.jpg" width="400" alt="3×3 宮格分鏡輸出"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/00f32388-a17b-4b9c-8da3-1956436ce91b" width="400" controls></video></td>
</tr></table>



**步驟：**

1️⃣ 輸入你想創作的內容 + ✅ 提示詞「Create a storyboard in a 3×3 grid format」
2️⃣ 用 ChatGPT 根據步驟 1 的圖片生成提示詞
3️⃣ 在 Seedance 中參考步驟 1 的圖片
4️⃣ 輸入步驟 2 生成的提示詞。

**GPT Image 2 提示詞：**

```
[describe your scene] and Create a storyboard in a 3×3 grid format
```

**Seedance 2.0 提示詞：**
turn this image into video
```
[Describe the motion and style. Example: Japanese full-color animation, fast cuts, high frame count, 24fps, dark fantasy anime OP style, intense battle scenes.]
```

> [!NOTE]
> 這是社群嘗試的網格方法，可用於表達順序意圖，但倉庫沒有對照測試證明失敗率更低或動作更準確


<!-- Case 10: Multi-Frame Reference Storyboard (by @heygentlewhale + @ai_gezgini) -->
<a id="case-10"></a>
### Case 10: [多幀參考 → 快剪影片](https://x.com/heygentlewhale/status/2047969137969004946)（by [@heygentlewhale](https://x.com/heygentlewhale)）

> **EvoLink 重現路線:** `seedance-2.5-reference-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

向 Seedance 2.0 傳入一張包含多個參考幀的分鏡圖，並指示它依序跟隨場景。模型會將幀的位置解讀為場景提示，直接輸出連貫的快剪效果——無需手動拼接。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/storyboard_case10/input.jpg" width="280" alt="GPT Image 2 多幀分鏡"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/4d7af334-4e49-4de4-899e-803f72116c21" width="280" controls></video></td>
<td align="center"><video src="https://github.com/user-attachments/assets/5def7e00-6fc6-4a4e-8075-5f37cb24b84c" width="280" controls></video></td>
</tr></table>

**步驟：**

1. 在 GPT Image 2 中生成多格分鏡圖（12 幀，3×4 或 4×3 網格）
2. 在 Seedance 2.0 中以該分鏡圖作為參考圖上傳
3. 撰寫包含幀數與剪輯風格的序列提示詞

**GPT Image 2 提示詞：**

```
Create a 12-panel storyboard grid for a [N]-second [genre] film:
- 4 columns × 3 rows, left-to-right, top-to-bottom reading order
- Each panel: [shot type] + [action description]
- Location: [setting], Time: [day/night], Mood: [atmosphere]
- Consistent character design and scene across all panels
- No text labels, no panel borders
Output as a single image.
```

**Seedance 2.0 提示詞：**

```
Follow the storyboard sequence of the 12 reference frames in image1, edited as a fast-cut memory montage.
[Describe visual style — example below:]
A nostalgic romance film set in 1990s Singapore, shot on 35mm film in Kodak Portra 800 style.
Soft grain, dreamy blur, warm highlights, and slight color shifts create a vintage cinematic atmosphere.
```

**通用序列提示詞（via [@ai_gezgini](https://x.com/ai_gezgini/status/2047349122315805016)）：**

```
Use this storyboard to generate a video, follow the scene order, keep transitions smooth,
and preserve cinematic lighting and pacing.
[Add any extra visual details you want.]
```

> [!NOTE]
> 這是社群嘗試的網格方法，可用於表達順序意圖，但倉庫沒有對照測試證明失敗率更低或動作更準確


<!-- Case 19: Storyboard-First Cost Control (by @0xbisc) -->
<a id="case-19"></a>
### Case 19: [分鏡優先的成本控管](https://x.com/0xbisc/status/2049100073481716076)（by [@0xbisc](https://x.com/0xbisc)）

> **EvoLink 重現路線:** `seedance-2.5-reference-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

先檢查分鏡，再決定是否生成影片，節省多少取決於圖片設定、影片設定與修改次數，不能承諾固定 10–50 倍價差或所有任務的最低成本

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/storyboard_case19/output.jpg" width="400" alt="分鏡優先工作流程輸出"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/09e04d80-c0d1-4a8c-9b74-2efe474acfcd" width="400" controls></video></td>
</tr></table>

**步驟：**

1. 用 GPT Image 2 生成一張 8 格的分鏡宮格
2. 逐格檢視——可單獨重新生成或編輯每一格直到滿意
3. 等整張分鏡完全鎖定後，再匯入 Seedance 2.0
4. 從定稿的分鏡一次性生成影片

**GPT Image 2 提示詞：**

```
Create a single cinematic storyboard image containing 8 panels, arranged in a 4-column horizontal grid layout across the canvas.
Panels are evenly distributed in 4 columns, forming a balanced multi-row composition.
Use generous white space between panels and around the entire layout, creating a calm, refined editorial presentation.
Minimalist editorial design, white background, precise alignment, consistent spacing, strong grid system.
Subtle divider lines, ultra-thin, low-contrast, neutral tone, strictly aligned to the grid.
Each panel is presented as a clean modular card with a clear hierarchy: image frame on top, minimal text block below.
Refined modern sans-serif typography, light to regular weight, tight typographic control, consistent scale rhythm.
Visual consistency across all panels: a white flying dragon and a short blond-haired young male wearing a loose flowing white robe riding on its back. A glowing spherical object remains consistent in appearance.
Style: live-action cinematic realism, human actor proportions, natural skin detail, physically accurate lighting, real-world materials, high-end film still quality, ultra high resolution, sharp focus.
Cinematic sequence:
Scene 01
Shot type
Wide shot, low-angle tracking
Narrative
Dragon skims rapidly above ground toward vast geometric ruins, rider standing steadily, bright daylight
Scene 02
Shot type
Wide shot, side view
Narrative
Dragon enters ruin airspace, stone structures begin sinking and shifting, geometry reconfigures
Scene 03
Shot type
Medium shot, tracking
Narrative
Dragon navigates through moving structures forming a spatial maze, rider leans forward, focused
Scene 04
Shot type
Push-in shot, centered composition
Narrative
Massive floating ring appears at center, glowing sphere suspended inside, focal point established
Scene 05
Shot type
Wide-angle, low-angle tracking, high speed
Narrative
Dragon dives through narrow moving gaps, massive structures pass extremely close, intense speed and compression
Scene 06
Shot type
Close-up, centered composition
Narrative
Rider reaches forward to grasp glowing sphere, golden light illuminating face and arm
Scene 07
Shot type
Wide shot, upward motion
Narrative
Dragon ascends sharply as ruins collapse below, structures sinking and closing, dust fills air
Scene 08
Shot type
Wide shot, high-angle view
Narrative
Dragon exits above collapsed ruins, open sky, clear silhouette of rider and dragon, resolution moment
```

**Seedance 2.0 提示詞：**

```
Generate video based strictly on storyboard @ image1. Follow the storyboard exactly as shown, matching each panel's composition, framing, and action. Keep perfect visual continuity with no errors or inconsistencies.
```

> [!NOTE]
> 先檢查分鏡，再決定是否生成影片，節省多少取決於圖片設定、影片設定與修改次數，不能承諾固定 10–50 倍價差或所有任務的最低成本


## 📱 商業與產品

<!-- Case 5: App MVP Demo Video (by @Shin_Engineer) -->
<a id="case-5"></a>
### Case 5: [App MVP 展示影片](https://x.com/Shin_Engineer/status/2047182050323812381)（by [@Shin_Engineer](https://x.com/Shin_Engineer)）

> **EvoLink 重現路線:** `seedance-2.5-image-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

利用 GPT Image 2 為一款尚未存在的 App 生成近似成品的 UI 截圖，再透過 Seedance 2.0 製作成產品展示影片。發布到 TikTok 或社群媒體，在正式開發前測試市場興趣。

| 輸出 |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/app_case5/output0.jpg" width="400" alt="GPT Image 2 生成的 App UI 截圖 1"></a> |

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/app_case5/output1.jpg" width="220" alt="App UI 截圖 2"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/app_case5/output2.jpg" width="220" alt="App UI 截圖 3"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/app_case5/output3.jpg" width="220" alt="App UI 截圖 4"></a></td>
</tr></table>

**步驟：**

1. 向 GPT Image 2 描述你的 App 概念與設計語言
2. 生成 3 到 5 張關鍵 UI 截圖（首頁、功能頁、個人頁等）
3. 依照使用者流程排序後，匯入 Seedance 2.0
4. 匯出展示影片並發布，觀察市場反應

**GPT Image 2 提示詞：**

```
Design [N] UI screenshots for a "[app concept]" app:
1. [Page 1 name and description]
2. [Page 2 name and description]
3. [Page 3 name and description]
Style: [iOS/Android] native design language, [primary color] accent, [light/dark] mode.
Output as realistic app screenshots, not wireframes or mockups.
```

**Seedance 2.0 提示詞：**

```
Smooth app UI transition animation, screen tap interaction, natural interface motion, clean and modern feel, 3 seconds.
```

> [!NOTE]
> 對外標明這是 AI 生成的概念展示，區分設想中的介面與互動和已實作的產品功能


<!-- Case 6: 15-Second Commercial (by @ai_mitosan) -->
<a id="case-6"></a>
### Case 6: [15 秒商業廣告](https://x.com/ai_mitosan/status/2047146600422846762)（by [@ai_mitosan](https://x.com/ai_mitosan)）

> **EvoLink 重現路線:** `seedance-2.5-reference-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

> 目前 2.5 單次生成 4–30 秒，較短鏡頭在剪輯時裁切；I2V 僅接受 adaptive，請預先設定圖片比例；提示詞中的 24fps 不是 API 幀率參數

兩步驟流程：GPT Image 2 生成主視覺與對應分鏡，再由 Seedance 2.0 製作各段動畫。加入字幕與音樂，就能組成完整的 15 秒廣告片。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/commercial_case6/input1.jpg" width="280" alt="GPT Image 2 主視覺產品圖"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/commercial_case6/input2.jpg" width="280" alt="GPT Image 2 分鏡"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/09ae3c57-b8fb-4323-ba76-7777541fe4a3" width="280" controls></video></td>
</tr></table>

**步驟：**

1. 用 image2 生成主視覺 + 分鏡
2. 把分鏡送入 Seedance2.0 轉成影片

**分鏡數量參考：**

| 影片長度 | 分鏡數量 | 每段時長 |
| :---: | :---: | :---: |
| 15 秒 | 4–5 | 3–4 秒 |
| 30 秒 | 8–10 | 3 秒 |
| 60 秒 | 15–18 | 3–4 秒 |

**GPT Image 2 提示詞：**

```
夜カフェ　深夜スイーツをテーマにした15秒CMを作るので、絵コンテを作って。 
プロの映像クリエイターによる15秒、８カット、マルチショット、ライティング重視。
```

**Seedance 2.0 提示詞：**

```
15秒、８カット、マルチショット、ライティング重視
```


<!-- Case 15: Luxury Commercial — Storyboard to Film (by @insmind_com) -->
<a id="case-15"></a>
### Case 15: [奢華廣告 — 分鏡到成片](https://x.com/insmind_com/status/2049481439285223785)（by [@insmind_com](https://x.com/insmind_com)）

> **EvoLink 重現路線:** `seedance-2.5-reference-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

用 GPT Image 2 生成奢華香水廣告的 3×4 分鏡宮格（共 12 幀），再用 Seedance 2.0 動畫成具備品牌級電影質感的影片。結構化的流程——序場 → 儀式 → 轉化 → 收束 → 品牌結尾——能在一次生成中完成完整敘事弧。371 讚 / 8.4 萬觀看 / 255 收藏。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/luxury_case15/output.jpg" width="400" alt="奢華廣告分鏡"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/281fef1e-f42d-442c-b06e-44d7cff221ec" width="400" controls></video></td>
</tr></table>

**步驟：**

1. 用 GPT Image 2 生成 12 幀分鏡宮格（3×4），採用編輯誌排版與奢華品牌美學
2. 將整張分鏡宮格作為單張參考圖匯入 Seedance 2.0
3. 提示 Seedance 將整段序列動畫化為一支電影感奢華廣告
4. 在剪輯軟體中加上音樂與最終調色

**GPT Image 2 提示詞：**

```
Create a high-end 9:16 luxury fragrance pitch deck storyboard in 3x4 grid (12 frames), editorial layout, Aesop/Byredo style, beige + lavender palette. Structured flow: intro → ritual → transformation → resolution → brand closure. Each frame split: top cinematic image (no text) + bottom storyboard notes. Luxury minimal European aesthetic, calm femininity, slow living mood. Candle is the emotional center throughout
```

**Seedance 2.0 提示詞：**

```
Animate the provided 3x4 storyboard into a smooth cinematic video. Preserve exact shot order and continuity. Use slow push-in, gentle pan, subtle orbit, and rack focus. Lighting transitions from soft morning glow to warm golden ambient light. Fragrance brand editorial aesthetic, minimal luxury, soft film grain. No new shots, no reordering, candle remains emotional focus in all scenes
```

> [!NOTE]
> 這是社群嘗試的網格方法，可用於表達順序意圖，但倉庫沒有對照測試證明失敗率更低或動作更準確


<!-- Case 16: Cinematic Food Video (by @kingofdairyque) -->
<a id="case-16"></a>
### Case 16: [電影感美食影片](https://x.com/kingofdairyque/status/2049812014596599834)（by [@kingofdairyque](https://x.com/kingofdairyque)）

> **EvoLink 重現路線:** `seedance-2.5-reference-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

用 GPT Image 2 + Seedance 2.5 製作極度寫實的美食料理影片，搭配時間戳記式的鏡頭描述。每段時間戳（0–2 秒、2–4 秒等）定義一個特定的鏡位與動作，讓 Seedance 對 15 秒序列有精準掌控。55 讚 / 1K 觀看。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/food_case16/input.jpg" width="400" alt="美食影片分鏡輸入"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/30a20e57-8384-4117-adf7-4f92faebeb33" width="400" controls></video></td>
</tr></table>

**步驟：**

1. 寫出詳細的時間戳鏡頭表，描述每個 2 秒區段
2. 依鏡頭表用 GPT Image 2 生成分鏡圖
3. 把圖片與完整時間戳提示詞一起送入 Seedance 2.0
4. 模型會跟隨時間戳結構，輸出一段連貫的料理過程

**Seedance 2.0 提示詞：**

```
Ultra-realistic cinematic 15-second vertical video (9:16), 4K, dark rustic wooden table,
soft dramatic lighting, shallow depth of field, natural textures, no text, no subtitles, no music.
[0-2s] Top-down shot: hands gently touch a bowl of [ingredient]. Subtle ambient movement.
[2-4s] Side close shot: [preparation action] in slow motion, catching warm light.
[4-6s] Macro shot: hands [action]. Texture detail visible.
[6-8s] 45-degree angle: [ingredient] pours into [vessel]. Natural bounce and movement.
[8-10s] Top angled close-up: hands carefully [assembly action]. Precise controlled motion.
[10-12s] Side shot: oven door opens. Warm golden light spills out with gentle steam.
[12-14s] Close-up: [finishing touch]. Surface becomes glossy, light reflecting softly.
[14-15s] Final frontal shot: finished [dish] on rustic table. Hands enter frame softly.
```

> [!NOTE]
> 這是社群嘗試的網格方法，可用於表達順序意圖，但倉庫沒有對照測試證明失敗率更低或動作更準確


<!-- Case 26: Product Image → Short Video Ad (by @insmind_com) -->
<a id="case-26"></a>
### Case 26: [商品圖 → 短影音廣告](https://x.com/insmind_com/status/2049843814337306974)（by [@insmind_com](https://x.com/insmind_com)）

> **EvoLink 重現路線:** `seedance-2.5-image-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

把靜態商品圖轉成讓觀眾停下來的社群短影音。將你既有的商品照作為參考圖傳給 GPT Image 2，生成情境構圖，再交給 Seedance 2.0 動畫化。專為電商與社群行銷設計——直接從手邊的商品照產出 TikTok / Reels 可用內容。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/product_case26/output.jpg" width="400" alt="商品影片廣告輸出"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/880c0019-e45a-4eb9-be6f-638ff71a0e0f" width="400" controls></video></td>
</tr></table>

**步驟：**

1. 輸入商品圖片。
2. 生成核心場景。
3. 定義動態與結構。
4. 風格與限制條件

> [!NOTE]
> 這個案例與案例 15（奢華廣告）的差別在於：它是從既有商品照出發，而非從零生成所有畫面。最適合手上已有商品圖、想快速做成影片廣告的電商賣家。


## 🎨 動畫與角色

<!-- Case 3: Character Sheet → Animation (by @YaReYaRu30Life) -->
<a id="case-3"></a>
### Case 3: [角色三視圖 → 動畫](https://x.com/YaReYaRu30Life/status/2047203375314571501)（by [@YaReYaRu30Life](https://x.com/YaReYaRu30Life)）

> **EvoLink 重現路線:** `seedance-2.5-reference-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

用 GPT Image 2 生成角色三視圖（正面、側面、背面），再以此作為 Seedance 2.0 動畫的視覺錨點。非常適合動漫角色、遊戲角色與公仔展示。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/character_case3/input0.jpg" width="260" alt="角色三視圖正面"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/character_case3/input1.jpg" width="260" alt="角色三視圖側面"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/character_case3/input2.jpg" width="260" alt="裝備設定圖"></a></td>
</tr></table>

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/character_case3/output.jpg" width="400" alt="角色三視圖與裝備合成"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/92a0aa56-441f-40db-b9c9-13410254cb3f" width="400" controls></video></td>
</tr></table>

**步驟：**

1. 三視圖（角色）+ 兩張裝備三視圖。以此為基礎，準備一張將各裝備穿戴完畢的三視圖。因圖片張數限制，角色附件在此省略
2. 根據三視圖製作分鏡
3. 用 Seedance2.0 將分鏡轉成影片

**GPT Image 2 提示詞：**

```
Create a storyboard based on this three-view drawing  
```

**Seedance 2.0 提示詞：**

```
Turn the storyboard into video using Seedance2.0
```


<!-- Case 4: Anime OP Style Video (by @Toshi_nyaruo_AI) -->
<a id="case-4"></a>
### Case 4: [動畫 OP 風格影片](https://x.com/Toshi_nyaruo_AI/status/2047216971184546231)（by [@Toshi_nyaruo_AI](https://x.com/Toshi_nyaruo_AI)）

> **EvoLink 重現路線:** `seedance-2.5-reference-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

用 GPT Image 2 建立場景設定圖，再讓 Seedance 2.0 自由發揮動畫。比較受限（分鏡引導）與自由（僅靠提示詞）的輸出結果，有助於決定每個鏡頭的最佳方式。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/character_case4/output0.jpg" width="280" alt="動畫 OP 輸出 1"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/f08a2fee-89a7-4c7c-a58a-f1306f87419a" width="280" controls></video></td>
<td align="center"><video src="https://github.com/user-attachments/assets/09d81a41-b5c5-47f3-8c67-442b7a93b019" width="280" controls></video></td>
</tr></table>

**步驟：**

1. 用 Grok 為虛構動畫 OP 撰寫歌詞
2. 用 GPT-image2 將歌詞轉成分鏡
3. 用 seedance2 生成影片

**GPT Image 2 提示詞：**

```
turn the lyrics into a storyboard
```

**Seedance 2.0 提示詞：**

```
Japanese full-color anime, fast cuts, high frame count, 24fps. Dark fantasy anime OP style. Epic battle between protagonist and massive supernatural creatures. High-impact sequence of scenes. Only [character name] appears.
```

> [!NOTE]
> 當 Seedance 自由動畫（不使用分鏡參考）時，結果可能更具動感，但與原始圖片的一致性較低。建議在關鍵角色鏡頭使用分鏡控制，動作場景則使用自由動畫。


<!-- Case 12: Claude Code + Character Sheet → Animation (by @old_pgmrs_will) -->
<a id="case-12"></a>
### Case 12: [Claude Code × 角色設定圖 → 動畫](https://x.com/old_pgmrs_will/status/2045091769180914019)（by [@old_pgmrs_will](https://x.com/old_pgmrs_will)）

> **EvoLink 重現路線:** `seedance-2.5-reference-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

用 Claude Code 撰寫世界觀與角色設定，再將結構化描述傳給 GPT Image 2 生成角色主視覺，最後用 Seedance 2.0 製作動畫。對開發者友善的原創 IP 製作流程。191 讚 / 7K 觀看。

<table><tr>
<td align="center"><a href="https://evolink.ai/seedance-2-5?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/character_case12/output.jpg" width="400" alt="Claude Code + GPT Image 2 角色主視覺"></a></td>
</tr></table>

**步驟：**

1. 用 Claude Code 撰寫世界觀筆記與結構化角色規格（名稱、外觀、性格、場景設定）
2. 將角色規格直接輸入 GPT Image 2，生成主視覺或角色設定圖
3. 以主視覺作為 Seedance 2.0 的參考圖，製作動畫

> [!NOTE]
> Claude Code 輸出的是結構化文字——角色規格、場景描述、對話大綱——GPT Image 2 能很好地將這些作為詳細提示詞處理。這條流程特別適合原創故事 IP：在程式碼中建構世界觀，在 GPT Image 2 中視覺化，在 Seedance 中動畫化。


<!-- Case 13: Dance Sequence Grid → Dance Video (by @Ciri_ai) -->
<a id="case-13"></a>
### Case 13: [舞蹈序列宮格 → 舞蹈影片](https://x.com/Ciri_ai/status/2049034340160704643)（by [@Ciri_ai](https://x.com/Ciri_ai)）

> **EvoLink 重現路線:** `seedance-2.5-reference-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

用 GPT Image 2 生成一張 4×4 的舞蹈姿勢宮格，再作為動作參考送入 Seedance 2.0。模型會將宮格解讀為編舞序列，輸出一段連續的舞蹈影片。進階變體：上傳多個角色參考，實現隨節拍換裝的轉場效果。161 讚 / 9K 觀看。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/dance_case13/output.jpg" width="400" alt="舞蹈序列宮格輸出"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/39376245-e7c7-4812-b770-9e81acf4eca2" width="400" controls></video></td>
</tr></table>

**步驟：**

1. 用 GPT Image 2 生成一張 4×4 宮格圖，展示角色的連續舞蹈姿勢
2. 在 Seedance 2.0 中以該宮格作為參考圖上傳
3. 提示 Seedance 跟隨參考圖中的舞蹈序列
4. （進階）上傳服裝 A 的角色、服裝 B 的角色，以及舞蹈宮格作為三張參考圖，實現舞蹈中途換裝轉場

**GPT Image 2 提示詞：**

```
Transform the input image into a stylized K-pop dance tutorial poster with a fashion-forward streetwear aesthetic, keeping the exact 4x4 grid layout (16 panels) and choreography structure.
Core Composition
Maintain a 16-panel grid (4 columns × 4 rows) with clean spacing

Each panel shows the same female dancer performing sequential choreography

Preserve panel numbering (1–16) in bold, modern UI-style labels

Keep step titles and instructional captions, but redesign typography to feel like K-pop album graphics / dance practice overlays

Subject Styling (K-pop Idol Inspired)

Young female dancer with soft glam K-pop makeup (dewy skin, subtle shimmer, defined eyes)

Hair: long, sleek, slightly dynamic (motion-friendly, flowing during moves)

Expression: confident, charismatic stage presence

Outfit (streetwear-inspired):

Cropped hoodie or oversized zip-up jacket

Cargo pants or parachute pants with straps

Chunky sneakers or platform boots

Optional accessories: chain necklace, ear cuffs, fingerless gloves

Visual Style

Switch from plain grayscale → high-contrast + soft neon accents

Base palette: black, white, gray

Accent colors: neon pink, electric blue, or violet glow (subtle, not overpowering)

Lighting:

Studio lighting with a soft glow + rim light effect

Slight stage-light vibe, like a K-pop dance practice video

Graphics & Effects

Add dynamic motion trails and glow accents on arms, legs, and hair movement

Replace basic arrows with stylized motion graphics (neon strokes, swooshes)

Subtle light streaks or particle effects for energy

Optional faint floor reflection or glossy surface

Typography

Titles: bold, modern, slightly condensed sans-serif (K-pop album style)

Add subtle glow or gradient to titles

Instruction text: clean, minimal, slightly futuristic UI style

Panel numbers: inside rounded squares or pill shapes with neon outline

Camera & Framing

Full-body framing in each panel (consistent scale)

Straight-on angle, but with slight dynamic tilt or perspective energy

Maintain clarity of movement for instructional purpose

Mood & Energy

Feels like a K-pop dance practice meets fashion editorial

Clean but energetic

Stylish, rhythmic, performance-driven

Important Constraints

Keep choreography readable and sequential

Do NOT merge panels or change layout

Maintain consistency of dancer identity across all panels
```

**Seedance 2.0 提示詞：**

```
Character from Image 1 performs the dance based on the breakdown in Image 3. Midway through the performance, they switch outfits on beat into the character from Image 2. Then, the character from Image 2 continues and completes the remaining dance steps from Image 3. Emphasize precise beat synchronization with the music
```

> [!NOTE]
> 這是社群嘗試的網格方法，可用於表達順序意圖，但倉庫沒有對照測試證明失敗率更低或動作更準確
>
> **社群變體：** [@airina_xyz](https://x.com/airina_xyz/status/2049830199236190326) 展示了以都市街舞者為主的基礎流程。[@Kashberg_0](https://x.com/Kashberg_0/status/2049697925262102689) 使用角色板 + 動作參考幀製作 K-Pop 編舞（52 讚 / 2K 觀看）。


<!-- Case 14: Comic Page → Animated Video (by @nimentrix) -->
<a id="case-14"></a>
### Case 14: [漫畫頁 → 動畫影片](https://x.com/nimentrix/status/2049560412979708334)（by [@nimentrix](https://x.com/nimentrix)）

> **EvoLink 重現路線:** `seedance-2.5-reference-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

用 GPT Image 2 製作多格漫畫頁——對角線排版、對話框、電影感敘事——再用 Seedance 2.0 將整頁動畫化。模型會將漫畫格解讀為敘事序列，輸出一段連續的動畫短片。330 讚 / 2.1 萬觀看 / 360 收藏。

<table><tr>
<td align="center"><strong>GPT Image 2 輸入</strong><br><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/comic_case14/input1.jpg" width="260" alt="角色參考 1 — 龍"></a></td>
<td align="center"><br><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/comic_case14/input2.jpg" width="260" alt="角色參考 2 — 少年"></a></td>
<td align="center"><strong>Seedance 2.0 輸入</strong><br><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/comic_case14/input3.jpg" width="260" alt="GPT Image 2 生成的漫畫頁"></a></td>
</tr></table>

<table><tr>
<td align="center"><video src="https://github.com/user-attachments/assets/0b5038e2-dfca-4c65-b5d7-a719a74408b0" width="400" controls></video></td>
</tr></table>

**步驟：**

1. 用 GPT Image 2 製作角色設定圖（正面、側面、背面視圖），鎖定角色外觀
2. 以角色為參考，生成多格漫畫頁
3. 將漫畫頁匯入 Seedance 2.0 並製作動畫

**GPT Image 2 提示詞 — 角色設定圖：**

```
Create a character design style sheet for [describe your character]:
front view, side view, back view on white background.
Make the aspect ratio 4:3.
```

**GPT Image 2 提示詞 — 漫畫頁：**

```
[Character description] and [companion], american comic multi-panel illustration,
diagonal layout, six panels, cinematic storytelling, clear reading flow, with speech bubbles.
[Describe the story sequence across panels.]
```

**Seedance 2.0 提示詞：**

```
Animate this comic page as a cinematic sequence. Follow the panel order from top-left to bottom-right.
Smooth transitions between panels, maintain character consistency, cinematic camera movement.
```

> [!NOTE]
> 對角線排版與對話框能為 Seedance 提供清晰的格線邊界與閱讀順序提示。為獲得最佳效果，每格的動作應保持簡單且明確。這個流程也很適合搭配 Suno 為最終影片加上配樂。


<!-- Case 25: K-Pop Choreography with Detailed Control (by @Kashberg_0) -->
<a id="case-25"></a>
### Case 25: [K-Pop 編舞 — 精細控制](https://x.com/Kashberg_0/status/2049839091899088948)（by [@Kashberg_0](https://x.com/Kashberg_0)）

> **EvoLink 重現路線:** `seedance-2.5-reference-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

原編舞描述的是較長成片，使用 EvoLink Seedance 2.5 時應壓縮或拆成每次不超過 30 秒的任務，再組合或延展；歷史提示詞不能作為單次生成 35–50 秒的介面範例

<table><tr>

<td align="center"><video src="https://github.com/user-attachments/assets/1c088b5e-6305-4bf6-9377-97784d5f8fac" width="400" controls></video></td>
</tr></table>

**步驟：**

1. 撰寫詳細的編舞序列（16 步，附具體舞蹈動作）
2. 用 GPT Image 2 生成展示每一步的參考宮格
3. 將宮格 + 完整編舞描述送入 Seedance 2.0
4. 模型會跟隨步驟序列，並以流暢的轉場銜接


**Seedance 2.0 提示詞：**

```
K-Pop Dance Sequence (16 Steps, Korean Street)
[PROJECT TYPE]
Cinematic K-pop dance video (instruction-to-performance translation)
[CORE REQUIREMENT — STRICT]
The video must faithfully follow the exact 16-step choreography shown in the reference sheet, in the same order, with accurate poses and transitions.
No steps added, removed, or rearranged.
🧍‍♀️ [CHARACTER]
Korean female dancer (K-pop idol aesthetic)
Slim, athletic build
Same consistent face and proportions throughout
Expressive, confident stage presence
Natural, fluid but sharp K-pop movement quality
👕 [WARDROBE — K-POP STYLE]
Fitted crop top
Loose high-waisted jeans
Sneakers
Modern idol styling (clean, trendy)
Fabric reacts naturally to movement (denim weight, subtle folds)
📍 [LOCATION / ENVIRONMENT]
Empty aesthetic Korean street (Seoul-inspired)
Clean urban design: narrow street, minimal signage, soft architecture
No people, no vehicles
Slight cinematic depth (buildings, street lights, textures)
Lighting:
Soft daylight or golden hour (ideal for K-pop vibe)
Balanced highlights + gentle shadows
🔢 [16-STEP CHOREOGRAPHY — LOCKED SEQUENCE]
Starting Pose
Step Touch Right
Step Touch Left
Hip Sway Combo
Body Roll Down
Back Step Sweep
Quarter Turn Pivot
Hair Flip & Pose
Side Step Drag
Cross Behind Unwind
Body Wave Up
Hip Circle
Step Lock Step
Arm Sweep Pose
Chest Pop & Hit
Final Pose (hold 2–3 sec)
🎥 [CAMERA DIRECTION]
Full-body framing at all times
Start: centered wide shot
Smooth tracking + subtle dolly movement
Slight angle variation (front → 3/4 → side for spins)
No fast cuts — continuous flow
Camera movement complements choreography, not distracts
💃 [MOVEMENT STYLE — IMPORTANT]
Authentic K-pop choreography feel
Mix of:
Sharp hits (chest pop, accents)
Smooth transitions (body waves, turns)
Clean isolations (hips, chest, arms)
Controlled spins, balanced footwork
No jitter, no unnatural speed
⏱️ [TIMING]
Each step: ~2–3 seconds
Total duration: ~35–50 seconds
Seamless transitions between steps
🎵 [MUSIC DIRECTION — VERY IMPORTANT]
Genre: K-pop / K-pop instrumental / dance-pop
Tempo: 100–115 BPM
Style:
Clean beat drops
Punchy percussion
Light synth melodies
Modern idol choreography vibe
Sync Notes:
Step transitions hit beats
Step 8 (Hair Flip) hits a musical accent
Step 15 (Chest Pop) synced with a strong beat hit
Final pose lands on a clean musical ending
🎨 [VISUAL STYLE]
Photorealistic
Slightly stylized K-pop MV tone
Soft cinematic grading
Clean, polished, high-end look
⚙️ [OUTPUT SETTINGS]
4K resolution
24–30 FPS
High motion clarity
No distortion, no artifacts
🚫 [RESTRICTIONS]
No extra dancers
No background crowd
No outfit changes
No deviation from choreography
No camera cuts that break continuity
```

> [!NOTE]
> 原編舞描述的是較長成片，使用 EvoLink Seedance 2.5 時應壓縮或拆成每次不超過 30 秒的任務，再組合或延展；歷史提示詞不能作為單次生成 35–50 秒的介面範例


<!-- Case 27: Character Intro Animation (by @0xbisc) -->
<a id="case-27"></a>
### Case 27: [角色登場動畫](https://x.com/0xbisc/status/2049496584283656690)（by [@0xbisc](https://x.com/0xbisc)）

> **EvoLink 重現路線:** `seedance-2.5-image-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

製作賽博龐克 AAA 遊戲風格的角色登場動畫。取任意角色圖片，用 GPT Image 2 重新設計為遊戲角色，生成電影感登場畫面，再用 Seedance 2.0 動畫化揭幕效果。可替換任何角色——此流程不受角色限制。55 讚 / 3K 觀看。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/intro_case27/output.jpg" width="400" alt="角色登場動畫輸出"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/e52eaa0b-b2fa-4c35-b790-a92af05d0c82" width="400" controls></video></td>
</tr></table>

**步驟：**

1. 準備一張角色圖片（自己的畫作、照片或 AI 生成的圖片）
2. 用 GPT Image 2 重新設計為賽博龐克 AAA 遊戲角色——保留臉部特徵，升級風格
3. 生成帶有角色的電影感登場畫面（深色背景、戲劇性打光、標題卡排版）
4. 在 Seedance 2.0 中動畫化登場揭幕效果

**GPT Image 2 提示詞 — 角色重新設計：**

```
based on the provided image, redesign as a cyberpunk AAA game character, keep face identity, keep original outfit, hyper-realistic game character, near-photoreal but still game-rendered, cinematic realism, in-game cutscene quality, cinematic lighting, strong contrast, realistic materials, depth of field, subject in sharp focus, background slightly blurred, strong foreground-background separation, Night City inspired environment, dense futuristic megacity, neon signage, wet streets, reflections, industrial details, fully human appearance, clean natural skin, no mechanical lines, no implants, no cyber patterns, character holding a highly designed futuristic weapon, dynamic action-ready pose, confident and intense expression, 16:9 AAA key visual, strong composition, character dominant, no logo, generate a unique character name fitting the character personality, character name in graffiti-style typography, medium-to-small size, integrated into layout, not dominant, refined character info module, editorial layout style, minimal, no background panel, only 1–2 short traits, extremely concise labels, grid-aligned typography-driven layout, Cyberpunk style UI, neon yellow text only, flat geometric layout, strict alignment, only one info module, no additional graphics, clean image, no heavy grain, no film grain, smooth surfaces, high polish, no anime, illustration, raw photography, metallic UI, gold color, cluttered layout, dense UI, boxes, background panels, color blocks, arrows, mechanical skin lines, cyber patterns

```

**Seedance 2.0 提示詞：**

```
industrial cyberpunk city at night, wet reflective ground, neon lights, distant explosions, floating sparks, cinematic atmosphere
camera always follows the character closely, no cuts, smooth tracking
motion continuity, no pose popping, no animation snapping, physically coherent transitions
0–2s:
character transitions into a low sliding movement
one hand brushing the ground for balance
sparks and debris react dynamically
weapon rotates forward in a smooth, deliberate motion
brief partial slow motion to emphasize control and flow
2–5s:
character raises weapon and fires while still moving forward
stylized compressed slow motion:
muzzle flash expands in layered light
face and muscles illuminated
subtle controlled recoil
shell casings eject in short slow-motion beats
particles and light distort around the shot
eyes focused strictly on target direction
final precise shot lands near the end of this phase
strong forward impact implied (sparks / explosion burst)
5–7s:
character motion fully stops, body settles naturally into final stance
character remains still, only subtle breathing motion
character lifts head and turns toward camera for the first time, then holds eye contact steadily
camera performs a subtle push-in
UI takes full visual focus:
UI builds progressively over the entire duration:
light glitch and scan effects
elements align into a clean layout
character name appears in graffiti handwritten animation, stroke-by-stroke reveal
secondary UI fades and slides in smoothly
```

> [!NOTE]
> 此流程不受角色限制——替換任何角色（動漫、寫實、風格化）皆可適用。關鍵在於 GPT Image 2 的兩步驟處理：先將角色重新設計為目標風格，再構圖登場畫面排版。


## 🎵 音樂影片與短片

<!-- Case 7: Music Video with Suno (by @fukaborichannel) -->
<a id="case-7"></a>
### Case 7: [結合 Suno 的音樂影片](https://x.com/fukaborichannel/status/2047206670020055317)（by [@fukaborichannel](https://x.com/fukaborichannel)）

> **EvoLink 重現路線:** `seedance-2.5-reference-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

三工具組合：GPT Image 2 負責視覺、Seedance 2.0 負責動態、Suno 負責音樂。先製作音樂以鎖定節奏與結構，再設計與節拍對齊的分鏡。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/music_case7/input.jpg" width="280" alt="GPT Image 2 為 MV 生成的分鏡"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/music_case7/output.jpg" width="280" alt="音樂影片輸出幀"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/fd4be5c7-cd02-4a77-ae07-6b80efeff201" width="280" controls></video></td>
</tr></table>

**步驟：**

1. 在 Suno 中生成目標風格的音樂——確認歌曲結構（前奏 / 主歌 / 副歌）
2. 在 GPT Image 2 中依歌曲段落設計分鏡
3. 在 Seedance 2.0 中為每格分鏡製作動畫——讓片段時長對齊節拍
4. 在剪輯軟體中將片段與音軌同步

> [!NOTE]
> 先製作音樂。在設計分鏡前就知道節奏與長度，能讓你精準地將分鏡時間對齊節拍切換點。


<!-- Case 8: Cyberpunk Style Short Film (by @ponyodong) -->
<a id="case-8"></a>
### Case 8: [賽博龐克風格短片](https://x.com/ponyodong/status/2047210987263230133)（by [@ponyodong](https://x.com/ponyodong)）

> **EvoLink 重現路線:** `seedance-2.5-image-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

用 GPT Image 2 建立一致的視覺風格（賽博龐克、霓虹、燈籠、女性美學），再用 Seedance 2.0 為每張圖製作動畫，產出一部介於桌布、海報與故事開場之間的風格化短片。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/cyberpunk_case8/input.jpg" width="280" alt="GPT Image 2 生成的賽博龐克插畫"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/db6ebb63-90dc-47c5-96c5-ab2fa53ed56d" width="280" controls></video></td>
</tr></table>

**步驟：**

1. 在 GPT Image 2 中定義視覺風格系統——固定色彩、打光與角色外觀
2. 生成 4 到 6 張保持相同氛圍的圖片
3. 在 Seedance 2.0 中以緩慢、氛圍感的動態提示詞為每張圖製作動畫
4. 將片段排列組合，構建一段視覺敘事短片


<!-- Case 11: Japanese MV Full Toolchain (by @Tz_2022) -->
<a id="case-11"></a>
### Case 11: [日系 MV — 全 AI 工具鏈](https://x.com/Tz_2022/status/2047684399404056609)（by [@Tz_2022](https://x.com/Tz_2022)）

> **EvoLink 重現路線:** `seedance-2.5-reference-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

四工具流程，製作完整的日系音樂影片：GPT Image 2 負責視覺 → Seedance 2.0 負責動態 → Suno 5.5 負責音樂 → CapCut 負責最終剪輯。742 讚 / 10.7 萬觀看。

<table><tr>
<td align="center"><video src="https://github.com/user-attachments/assets/e5ce621c-7fa3-47b5-99a7-00df7741a651" width="400" controls></video></td>
</tr></table>

**步驟：**

1. 先在 Suno 5.5 中生成音樂——鎖定歌曲長度、節奏與氛圍
2. 在 GPT Image 2 中依歌曲段落設計分鏡
3. 在 Seedance 2.0 中為每格分鏡製作動畫，讓片段時長對齊節拍
4. 將影片片段與 Suno 音軌匯入 CapCut——同步並匯出

> [!NOTE]
> 先製作音樂——在設計分鏡前就知道節拍結構，能讓你精準地將分鏡時間對齊歌曲切換點。這是案例 7（City Pop MV）的延伸，加入 Suno 形成完整迴路，將整條流程視為同步製作而非後期拼接。


<!-- Case 20: Claude Shotlist → MV (by @CoffeeVectors) -->
<a id="case-20"></a>
### Case 20: [Claude 鏡頭表 → 音樂影片](https://x.com/CoffeeVectors/status/2049592150581485757)（by [@CoffeeVectors](https://x.com/CoffeeVectors)）

> **EvoLink 重現路線:** `seedance-2.5-image-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

用 Claude 生成詳細的鏡頭表（15 個一秒片段，各有不同鏡位與動作），用 GPT Image 2 生成一張人物肖像，再用 Seedance 2.0 逐鏡頭製作。將片段剪輯在一起並搭配你的 Suno 音樂，即可完成一支完整 MV。AI 負責創意方向——你只需執行。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/shotlist_case20/input.jpg" width="400" alt="Claude 鏡頭表音樂影片輸出"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/d6ba86c4-65c3-4b1d-aa3c-846667f53b5e" width="400" controls></video></td>
</tr></table>

**步驟：**

1. 用 GPT Image 2 生成一張角色肖像作為視覺錨點
2. 請 Claude 撰寫 15 鏡頭的鏡頭表（每秒一鏡），包含多種角度與動作
3. 將肖像 + 每個鏡頭描述分別送入 Seedance 2.0
4. 將所有片段剪輯在一起並與音軌同步


**Seedance 2.0 提示詞（逐鏡頭）：**

```
A 15-second prestige-TV sequence, one shot per second, scored to an apocalyptic sacred crescendo — low organ and dissonant brass through roaring choir, hammered bells, and earth-shaking timpani to a final shattering harmonic strike. Throughout: a pale young queen with white hair, a tall ornate gold filigree crown, a translucent gauze veil, and a heavily jeweled pale gown — channeler of divine fire from above. Shot entirely handheld — visible micro-shake, breath-rhythm sway, reactive whip-corrections to action, documentary-tense framing.
1 (0–1s) Sky Opens. Handheld wide low-angle, camera tilted up. Black clouds spiral and split in a tear of white-gold light. She stands small below. Organ slams.
2 (1–2s) Eyes To Heaven. Handheld tight close-up, slight float. Her eyes lifted, gold light on her face, a tear of fire tracking down her cheek. Choir enters.
3 (2–3s) Hand Raised. Handheld medium, slight push-in. She raises one palm to the sky. Clouds above twist toward her gesture. Strings climb.
4 (3–4s) First Bolt. Handheld wide. A colossal pillar of holy fire descends and splits a distant black tower. Camera jolts on impact. Hammer beat.
5 (4–5s) The Pointing. Handheld tight medium. She extends one ringed finger slowly toward the horizon. Camera barely breathing. Bells ring.
6 (5–6s) Bolts Rain. Handheld wide, panning to track strikes. Dozens of pillars of holy fire descend across a battlefield. Camera whips reactively to each impact. Drums hammer.
7 (6–7s) Cloaked In Light. Handheld low-angle medium. A shaft of holy fire engulfs her without burning. Camera trembles in the pressure wave. Choir doubles.
8 (7–8s) The Wicked Burn. Handheld tight medium. A robed figure raises a blade — consumed in white-gold fire from above, ash silhouette collapsing. Camera flinches with the strike. Bass hit.
9 (8–9s) Walking Forward. Handheld tracking wide, operator moving with her. She advances across cracked scorched earth, pillars of fire descending in her wake. Strings shriek.
10 (9–10s) Crown Of Lightning. Handheld tight on the crown, slight float. White-gold lightning arcs continuously between the spires. Hair lifts in charged air. Bells climb.
11 (10–11s) Closed Fist. Handheld tight close-up. Her hand closes slowly into a fist. Vast clap of thunder. Camera shakes hard. Sustained held chord.
12 (11–12s) The Cleansing. Handheld wide, operator on a high vantage with visible sway. A fortified city struck by a grid of descending holy fire pillars. She stands small below, untouched. Choir at full roar.
13 (12–13s) The Quiet After. Handheld medium, breathing slowly. She lowers her hand. The storm stills. Ash falls like snow around her. Music drops to near-silence.
14 (13–14s) Eyes Return. Handheld extreme close-up, slight float. Eyes still warm gold blink once slowly. Faintest exhale. Single sustained tone.
15 (14–15s) The Smiting. Handheld frontal wide at dusk, settling into stillness on the final hold. She stands at the center of a vast scorched circle, horizon reduced to smoking ruin. Torn sky still glowing above her. Final shattering harmonic strike sustains.

Style: Photorealistic dark holy fantasy, prestige-TV aesthetic. Anamorphic 35mm, shallow DoF, heavy volumetric atmosphere — smoke, ash, ember haze, heat distortion, charged air shimmer. Palette of scorched bone-white, ivory, ash-gray, storm-slate, and incandescent white-gold. Painterly compositions, fine detail against destruction, organic film grain, heavy highlight bloom on the divine fire. Handheld throughout — visible micro-shake, reactive whip-corrections, breath-rhythm sway, camera flinching with every impact. No tripod stillness until the final hold. Operatic, terrifying, sovereign. The sky itself as her instrument.
```

> [!NOTE]
> 此流程將創意方向（Claude）與視覺執行（GPT Image 2 + Seedance）分離。特別適合需要同一角色大量不同鏡頭的音樂影片。單張肖像作為錨點，能在所有 15 個片段中維持一致性。


## 🎮 遊戲概念

<!-- Case 9: Game & Interactive Content (by @AbleGPT) -->
<a id="case-9"></a>
### Case 9: [遊戲與互動內容](https://x.com/op7418/status/2046854932620525750)（by [@op7418](https://x.com/op7418)）

> **EvoLink 重現路線:** `seedance-2.5-image-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

用 GPT Image 2 生成遊戲風格的 UI 圖片（包含 HUD 元素、技能條、選項覆蓋層），再用 Seedance 2.0 動畫化，模擬互動遊戲畫面。遊戲與插畫風格在 Seedance 中受到的內容限制比寫實人物影像少。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/game_case9/input.jpg" width="400" alt="遊戲 UI 輸入圖"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/3d5d7525-b469-4c3b-aab9-68dc47630fdd" width="400" controls></video></td>
</tr></table>

**步驟：**

1. 用 GPT Image 2 生成 ARPG 或遊戲 UI 風格的圖片，包含 HUD 元素
2. 匯入 Seedance 2.0 並描述互動或戰鬥序列
3. 加入後製特效（粒子、光暈）進行潤飾

**GPT Image 2 提示詞-1：**

```
帮我生成一个以《金瓶梅》为主题的古代 ARPG MMO 开放世界游戏的截图
```
**GPT Image 2 提示詞-2：**
```
出现 UI 选择 UI 之后变成第二张图的场景图
```

**Seedance 2.0 提示詞：**

```
选择 UI 之后变成第二张图右边的场景
```

**變體 — ARPG 遊戲模擬（by [@0xbisc](https://x.com/0xbisc/status/2047315350862352715)）：**

海賊王、怪奇物語，任何 IP——生成一個不存在的世界的遊戲截圖，再用 Seedance 2.0 擴展為即時遊戲畫面。934 讚 / 12.5 萬觀看。

<table><tr>
<td align="center"><video src="https://github.com/user-attachments/assets/983b433a-88ea-4843-9047-fc01396752fe" width="400" controls></video></td>
</tr></table>

**GPT Image 2 提示詞：**

```
Generate an ARPG dialogue game screenshot inspired by [film/series name]
```

**Seedance 2.0：** 使用 Image-to-Video 模式。無需提示詞——Seedance 會讀取 HUD 排版並自動延伸為遊戲畫面序列。

> [!NOTE]
> Seedance 2.0 對寫實人物內容有限制。遊戲、動漫與插畫風格能繞過大部分限制，提供更大的創作空間。


<!-- Case 17: Game Interface Animation Full Pipeline (by @0xInk_) -->
<a id="case-17"></a>
### Case 17: [遊戲介面動畫 — 完整流程](https://x.com/0xInk_/status/2048809000121360649)（by [@0xInk_](https://x.com/0xInk_)）

> **EvoLink 重現路線:** `seedance-2.5-image-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

本合集中最具病毒傳播力的流程：從零開始製作完整的電玩介面動畫。先在 Midjourney 中建立 2D 角色，用 GPT Image 2 轉換為 3D 遊戲風格，設計完整遊戲 UI（HUD、載入畫面、選單），再用 Seedance 2.0 動畫化所有畫面。GPT Image 2 在此表現出色，因為它能處理 UI 細節，且允許反覆修改而不損失品質。2280 讚 / 20.8 萬觀看 / 2793 收藏。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/game_case17/output.jpg" width="400" alt="遊戲介面動畫輸出"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/b83da8f3-3dd6-44a3-bb27-b0d59cab381a" width="400" controls></video></td>
</tr></table>


> [!NOTE]
> 關鍵洞察：GPT Image 2 允許你多次修改同一張圖片而不會品質下降——非常適合反覆調整 UI 排版。先將完整遊戲介面建構為一系列靜態畫面，再讓 Seedance 將它們串接成流暢的動畫。


<!-- Case 24: GTA-Style City Game Concept (by @markgadala) -->
<a id="case-24"></a>
### Case 24: [GTA 風格城市遊戲概念](https://x.com/markgadala/status/2048560337960489385)（by [@markgadala](https://x.com/markgadala)）

> **EvoLink 重現路線:** `seedance-2.5-reference-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

5 分鐘內創造任何版本的 GTA。用 GPT Image 2 生成設定在任何城市（東京、拉各斯、孟買）的遊戲 UI 截圖，再用 Seedance 2.0 動畫化為遊戲實機畫面。成品看起來就像一款不存在的遊戲的真實預告片。99 讚 / 8.7K 觀看。

<table><tr>
<td align="center"><video src="https://github.com/user-attachments/assets/d3b0a7b9-827a-47f6-b24e-eabfacf3e892" width="400" controls></video></td>
</tr></table>

**步驟：**

1. 定義你的 GTA 變體——城市、年代、視覺風格
2. 用 GPT Image 2 生成遊戲截圖：第三人稱視角、HUD 覆蓋層、城市環境
3. 匯入 Seedance 2.0 並動畫化為遊戲實機畫面
4. 將片段組裝成預告片


> [!NOTE]
> 這是案例 9 遊戲概念方法的延伸，專門針對開放世界城市遊戲。HUD 元素（小地圖、血條、通緝星級）是營造「真實遊戲」錯覺的關鍵。適用於任何城市——街景細節越具體，效果越逼真。


## 🛠 製作工具

<!-- Case 18: Single Agent Automated Workflow (by @venturetwins) -->
<a id="case-18"></a>
### Case 18: [單一 Agent 自動化工作流程](https://x.com/venturetwins/status/2048526911056613586)（by [@venturetwins](https://x.com/venturetwins)）

> **EvoLink 重現路線:** `seedance-2.5-image-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

零操作方案：告訴單一 AI Agent（如 Glif）你想要什麼，它會在一次對話中處理整條流程——用 GPT Image 2 生成分鏡，再用 Seedance 2.0 動畫化。無需手動傳檔，無需逐步撰寫提示詞。934 讚 / 7 萬觀看。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/agent_case18/output.jpg" width="400" alt="單一 Agent 自動化工作流程輸出"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/cc01849d-ee9b-47af-a7b0-d13250a001e0" width="400" controls></video></td>
</tr></table>


<!-- Case 21: Casting Grid Actor Audition (by @8fstudioz) -->
<a id="case-21"></a>
### Case 21: [選角宮格 — 演員試鏡](https://x.com/8fstudioz/status/2049547426198151627)（by [@8fstudioz](https://x.com/8fstudioz)）

> **EvoLink 重現路線:** `seedance-2.5-image-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

一次生成試鏡 4 位演員，節省點數。用 GPT Image 2 生成 4 格選角宮格，展示同一角色的不同演員，再在 Seedance 2.0 中用相同台詞逐一測試。在投入完整影片製作前，先找出值得花更多點數的演員。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=community_image"><img src="images/casting_case21/input.jpg" width="400" alt="選角宮格輸入"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/dcdd958f-70cd-43f6-b191-4e0715fe2472" width="400" controls></video></td>
</tr></table>

**步驟：**

1. 用 GPT Image 2 生成 4 格選角宮格——同一角色、4 位不同演員
2. 在 Seedance 2.0 中以相同台詞與動作逐一測試每位演員
3. 比較表演品質（眼神接觸、表情、動作）
4. 僅將剩餘點數投入表現最佳的演員

**GPT Image 2 提示詞：**

```
Create a 16:9 horizontal cinematic casting board showing 4 different actor candidates for the same role.

Style:
[INSERT VISUAL STYLE]
Examples: CGI AAA video game cinematic, photorealistic, anime, stylized 3D

Role brief:
[INSERT ROLE DESCRIPTION]
Describe the type of lead or character the user is casting for.

World / genre:
[INSERT WORLD OR GENRE]
Examples: spy-action thriller, fantasy RPG, sci-fi adventure, crime drama

Wardrobe:
[INSERT WARDROBE DESCRIPTION]
Describe the clothing or outfit direction all 4 actors should share.

Tone:
[INSERT TONE]
Examples: sleek, dangerous, adventurous, grounded, moody, confident

Visual direction:
[INSERT VISUAL RENDERING NOTES]
Describe the rendering quality, material detail, realism level, facial detail, costume detail, and overall look.

Cinematic look:
[INSERT CINEMATIC STYLE]
Examples: blockbuster trailer aesthetic, prestige drama look, AAA game cinematic look

Camera framing:
[INSERT FRAMING]
Examples: 3/4 body, full body, waist-up

Camera angle:
[INSERT CAMERA ANGLE]
Examples: eye-level, slight low angle, slight 3/4 angle

Lens:
[INSERT LENS]
Examples: 50mm cinematic lens, 85mm portrait lens

Depth of field:
[INSERT DEPTH OF FIELD]
Examples: shallow, shallow but controlled

Lighting:
[INSERT LIGHTING SETUP]
Describe the lighting style.

Background:
[INSERT BACKGROUND DESCRIPTION]
Describe the background environment or backdrop.

Colour treatment:
[INSERT COLOUR TREATMENT]
Describe the grading or colour tone.

Layout:
Arrange the 4 actor candidates in a 16:9 horizontal composition with 4 evenly spaced vertical panels across the frame, one actor per panel from left to right.

Character variation:
Each candidate should feel like a different casting choice for the same role. Vary facial structure, age feel, hairstyle, expression, posture, and energy, but keep them grounded in the same world, wardrobe logic, and tonal universe.

Important:
- Same role
- Same world
- Same wardrobe logic
- Same visual style
- Different actor interpretations
- No duplicated faces
- No text
- No labels
- No watermark

The final image should feel like a premium cinematic casting board for [INSERT PROJECT TYPE].
Examples: a film, a game, an animated short, a cinematic trailer
```


**Seedance 2.0 提示詞（逐演員）：**

```
Use the uploaded 16:9 four-panel casting board as the source image.

Create a controlled 15-second cinematic casting audition reel for [INSERT ROLE OR PROJECT TYPE].

Animate the actors one by one in this exact order from left to right:

0.0–3.5 seconds: ONLY the far-left actor performs.
3.5–7.0 seconds: ONLY the second actor from the left performs.
7.0–10.5 seconds: ONLY the third actor from the left performs.
10.5–14.0 seconds: ONLY the far-right actor performs.
14.0–15.0 seconds: hold on the full four-panel board with all actors still.

Each actor delivers the same audition line:
"[INSERT DIALOGUE LINE]"

Performance direction:
Each actor should look directly into the camera while delivering the line, as if performing a screen test audition. Their eye line should stay locked to camera.

Each actor should deliver the line with:
[INSERT PERFORMANCE TRAITS]
Examples: calm control, quiet menace, emotional vulnerability, confidence, charm, intensity, humor

The performance should feel:
[INSERT PERFORMANCE TONE]
Examples: sleek, cinematic, believable, grounded, dramatic, stylized

Each actor should bring a slightly different interpretation of the same role.

Control rules:
ONLY the active actor moves during their assigned time window.
ONLY the active actor speaks during their assigned time window.
ONLY animate the active actor's mouth, eyes, facial expression, head, and subtle upper-body movement.
The active actor must look directly at the camera while speaking.
All other actors remain completely still like frozen reference images.
Do not animate multiple actors at the same time.
Do not change the panel layout.
Do not change actor positions.
Do not cut to a new scene.
Do not reframe into a different composition.
Do not change wardrobe.
Do not change background.
Do not change lighting.
Do not add new characters.
Do not add extra dialogue.
Do not add captions, subtitles, labels, or text.

Camera direction:
Keep the four-panel 16:9 casting board as the main composition. Use only [INSERT CAMERA MOVEMENT STYLE] toward the active actor during their performance window.
Examples: a subtle cinematic push-in, gentle focus emphasis, minimal controlled emphasis

Keep the movement [INSERT CAMERA BEHAVIOUR].
Examples: minimal, smooth, controlled

Keep the actor presented toward camera so the audition feels direct and comparable.

Audio / timing:
Each actor should speak the dialogue clearly within about 3.5 seconds.
The same line is repeated four times, once per actor.
No overlapping voices.
No background conversation.
No unnecessary sound effects.

Final result:
A clean casting audition reel where four actor candidates perform the same line one by one from left to right, each looking directly into the camera, making it easy to compare screen presence, facial acting, eye contact, posture, and dialogue delivery.
```

> [!NOTE]
> 一個角色在靜態圖片中可能看起來很棒，但一旦測試台詞、眼神接觸與表演，可能完全不適合。這個流程在你花費點數製作完整場景之前，就先完成選角決策。


<!-- Case 22: 3D Sculpt → AI Render → Animation (by @_DAntunes_) -->
<a id="case-22"></a>
### Case 22: [3D 雕塑 → AI 渲染 → 動畫](https://x.com/_DAntunes_/status/2049142166232904078)（by [@_DAntunes_](https://x.com/_DAntunes_)）

> **EvoLink 重現路線:** `seedance-2.5-image-to-video` · [API](docs/api-workflow.md#choose-a-video-route)

將傳統 3D 建模與 AI 影片橋接：在 Nomad Sculpt（或任何雕塑軟體）中建立粗略的 3D 黏土模型，用 GPT Image 2 渲染為精緻的插畫，再透過 ComfyUI 用 Seedance 2.0 動畫化。這能讓你精確控制姿勢與構圖，是純文字提示詞無法達到的。

<table><tr>
<td align="center"><video src="https://github.com/user-attachments/assets/f5ecdb0c-d1ca-4291-91bc-eb88de91cd82" width="400" controls></video></td>
</tr></table>

**步驟：**

1. 在 Nomad Sculpt（或 Blender、ZBrush 等）中雕塑粗略的 3D 模型
2. 從你想要的鏡頭角度匯出模型截圖
3. 用 GPT Image 2 將 3D 模型渲染為精緻的插畫或寫實圖片
4. 將渲染後的圖片匯入 Seedance 2.0（透過 ComfyUI 或直接匯入）並製作動畫

> [!NOTE]
> 3D 模型能提供文字提示詞無法做到的東西：對身體姿勢、手部位置與鏡頭角度的精確控制。即使是粗略的黏土模型也足夠——GPT Image 2 會處理所有渲染與細節工作。這條流程非常適合已經使用 3D 工具、想在工作流程中加入 AI 動畫的創作者。


## 🌟 社群精選

這裡持續展示 X 平台創作者分享的 **GPT Image 2 × Seedance 2.0** 作品。點擊影片可播放，點擊作者帳號可開啟原帖。最新新增內容排在最前面。

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/cd87bc68-5613-410e-8dbe-df656aaa504d" width="240" controls></video>
<br/><a href="https://x.com/abxxai/status/2055636095736709190"><b>@abxxai</b></a> · <sub>80,365 views</sub>
<br/><sub>You can literally create anything with AI right now.</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/fd7dac8a-0984-416d-8632-72ecd3106586" width="240" controls></video>
<br/><a href="https://x.com/pabloprompt/status/2055726656287871478"><b>@pabloprompt</b></a> · <sub>75,035 views</sub>
<br/><sub>One Piece BTS · PART 2 😍</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/6ae8904b-6510-4aa5-ba8f-12ab001669ec" width="240" controls></video>
<br/><a href="https://x.com/maarcoofdezz/status/2057371189207584943"><b>@maarcoofdezz</b></a> · <sub>30,023 views</sub>
<br/><sub>Just made a full cinematic ad for a luxury mens cologne usi…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/484aa607-4d00-4543-95d0-7838fe7ce0db" width="240" controls></video>
<br/><a href="https://x.com/AIwithAliya/status/2055674114845925710"><b>@AIwithAliya</b></a> · <sub>24,084 views</sub>
<br/><sub>This looks so neat and clean</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/0c2f7cf0-f7e1-4f52-b7b7-e53c179fcc0d" width="240" controls></video>
<br/><a href="https://x.com/HeyOz_AI/status/2057871032480825398"><b>@HeyOz_AI</b></a> · <sub>17,459 views</sub>
<br/><sub>Claude + GPT Image 2 + seedance + Meta ads MCP Replaced my…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/77e02dda-8b51-4654-8af2-1bbb93f822d6" width="240" controls></video>
<br/><a href="https://x.com/Creatify_AI/status/2056431801971999147"><b>@Creatify_AI</b></a> · <sub>16,350 views</sub>
<br/><sub>Creatify AI agents use the BEST AI models for each process.</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/3adf863a-165b-4d3e-bb20-e427cd3ce648" width="240" controls></video>
<br/><a href="https://x.com/MayorKingAI/status/2057933848948965741"><b>@MayorKingAI</b></a> · <sub>14,113 views</sub>
<br/><sub>I created a steampunk action sequence in a hand-painted 3D…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/800f2bbc-d53b-4075-8e08-b63a2e69c3e3" width="240" controls></video>
<br/><a href="https://x.com/IATheYoker/status/2057402859222933891"><b>@IATheYoker</b></a> · <sub>12,503 views</sub>
<br/><sub>GPT Image 2 + Seedance 2.5 ya pueden crear intros del Mundi…</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/008d22d8-9a47-4051-ab60-7743958cc4c8" width="240" controls></video>
<br/><a href="https://x.com/ShamiWeb3/status/2055832098435629466"><b>@ShamiWeb3</b></a> · <sub>9,644 views</sub>
<br/><sub>A TAPNOW luxury skincare visual in which a glowing beauty m…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/592c1944-d3bf-4db6-b546-f152a836081d" width="240" controls></video>
<br/><a href="https://x.com/GlitterPixely/status/2057903405712953505"><b>@GlitterPixely</b></a> · <sub>8,862 views</sub>
<br/><sub>Quick character highlight intro with GPT Image 2 + Seedance…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/4467f8e3-192a-4937-95a6-1945122a6d66" width="240" controls></video>
<br/><a href="https://x.com/luche_whitewing/status/2055626188241150350"><b>@luche_whitewing</b></a> · <sub>7,837 views</sub>
<br/><sub>深夜の美女👠 lovart (@lovart_jp)× 🎬 GPT-image-2 × Seedance 2.0 で作…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/4d6c8938-e4a2-4bf6-ab16-e7a2ed4d8205" width="240" controls></video>
<br/><a href="https://x.com/DoctorAmna11/status/2057108821537861739"><b>@DoctorAmna11</b></a> · <sub>6,903 views</sub>
<br/><sub>The Ghost Who Couldn’t Scare Anyone</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/ec26a6f4-f6ca-4a4b-bc68-3c11d818982d" width="240" controls></video>
<br/><a href="https://x.com/I_amShiti/status/2057378173856494070"><b>@I_amShiti</b></a> · <sub>5,830 views</sub>
<br/><sub>One AI app gives you access to👇</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/f7323047-0d46-4cba-945f-e8199a837787" width="240" controls></video>
<br/><a href="https://x.com/eijo_AIart/status/2056935787581898972"><b>@eijo_AIart</b></a> · <sub>5,028 views</sub>
<br/><sub>PolloAI GPT-Image2 x Seedance2で、映画製作用ストーリーボードを使った、ショートフィルム制…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/01aa8296-2c8c-4c99-a915-2bbdc9232125" width="240" controls></video>
<br/><a href="https://x.com/aziz4ai/status/2057824424838004836"><b>@aziz4ai</b></a> · <sub>4,885 views</sub>
<br/><sub>JADE FALCON: AWAKENING</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/70eea8b8-d3fa-4555-9c60-52ed8bed4711" width="240" controls></video>
<br/><a href="https://x.com/opener_ai/status/2055627299429777684"><b>@opener_ai</b></a> · <sub>4,353 views</sub>
<br/><sub>Gpt image 2 x Seedance 2.0 @dreamina_ai</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/014d3a33-b68a-4977-8f72-a239b65a835c" width="240" controls></video>
<br/><a href="https://x.com/spect3ral/status/2057871834310148242"><b>@spect3ral</b></a> · <sub>4,319 views</sub>
<br/><sub>Claude + GPT Image 2 + Seedance + Meta Ads MCP</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/2f8d430d-fd0f-4d1b-9c74-92f85fa466b2" width="240" controls></video>
<br/><a href="https://x.com/mdmadeit/status/2055685500279697883"><b>@mdmadeit</b></a> · <sub>3,970 views</sub>
<br/><sub>made a full 1:25 anime short</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/ea9bbdfd-a5b1-4e85-a886-362362f6e3cb" width="240" controls></video>
<br/><a href="https://x.com/Strength04_X/status/2055849751317524982"><b>@Strength04_X</b></a> · <sub>3,737 views</sub>
<br/><sub>Created this cinematic sushi 🍣storyboard with GPT Image 2 +…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/595b4af8-ece2-4cca-98df-982721e685bd" width="240" controls></video>
<br/><a href="https://x.com/jasminekhan90_/status/2057399215228322261"><b>@jasminekhan90_</b></a> · <sub>3,418 views</sub>
<br/><sub>Human connection still matters in an AI future.</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/6e646b59-7485-470d-af4e-de983dda6b12" width="240" controls></video>
<br/><a href="https://x.com/Sogni_Protocol/status/2057822871817191549"><b>@Sogni_Protocol</b></a> · <sub>3,342 views</sub>
<br/><sub>There’s no better combo on the market right now than GPT Im…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/28bb17d7-6fc0-4f94-8716-8b5871a290ea" width="240" controls></video>
<br/><a href="https://x.com/noorlewisx/status/2055863201389240369"><b>@noorlewisx</b></a> · <sub>2,974 views</sub>
<br/><sub>Made with Seedance 2 + GPT Image 2</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/b265ac7b-fb01-4e4c-954c-f4ab748f7fc4" width="240" controls></video>
<br/><a href="https://x.com/markgadala/status/2055896597662228650"><b>@markgadala</b></a> · <sub>2,876 views</sub>
<br/><sub>AI makes creating Pixar quality animations so incredibly ea…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/f4c4152c-15d0-404b-8040-f86d54ecbc28" width="240" controls></video>
<br/><a href="https://x.com/SocialSight/status/2057334346223177973"><b>@SocialSight</b></a> · <sub>2,720 views</sub>
<br/><sub>did you get the news?</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/4ba27b9b-0431-419e-90fe-6a25816979c5" width="240" controls></video>
<br/><a href="https://x.com/hanifproduktif/status/2055828657172820269"><b>@hanifproduktif</b></a> · <sub>2,595 views</sub>
<br/><sub>Replaced (GPT Image 2 + Seedance 2.5)</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/11375c25-a923-44a1-a8a4-8d04acecab31" width="240" controls></video>
<br/><a href="https://x.com/adrianaia_/status/2057474538594607520"><b>@adrianaia_</b></a> · <sub>2,382 views</sub>
<br/><sub>De las calles frías a un salón de clases lleno de amor.</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/0dd27e90-469f-4ee8-aebb-3f3afbf2d8f2" width="240" controls></video>
<br/><a href="https://x.com/itsPolloAI/status/2057333580133724593"><b>@itsPolloAI</b></a> · <sub>2,153 views</sub>
<br/><sub>🎉 Pollo AI × GPT Image 2 × Seedance 2.0 — Results are in.</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/c62c2125-a2c4-4e3a-9e99-e6f94124086c" width="240" controls></video>
<br/><a href="https://x.com/SimplyAnnisa/status/2058068924806160785"><b>@SimplyAnnisa</b></a> · <sub>2,026 views</sub>
<br/><sub>Golden mornings and buttery saltbread bliss</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/7e1d91f7-0153-4b5d-ac13-ae62da10f517" width="240" controls></video>
<br/><a href="https://x.com/Artedeingenio/status/2057401307510481397"><b>@Artedeingenio</b></a> · <sub>1,479 views</sub>
<br/><sub>Using Niji to create children’s illustrations, GPT Image 2…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/5a72d57d-f9fb-42a4-8e15-2de535d3b6a8" width="240" controls></video>
<br/><a href="https://x.com/hasamaru_studio/status/2057433716339933656"><b>@hasamaru_studio</b></a> · <sub>1,461 views</sub>
<br/><sub>GPT Image 2 でショットリストを作成し、 Seedance 2.0 のリファレンス生成で動画を作成しました。</sub>
</td>
<td align="center" valign="top" width="25%"></td>
<td align="center" valign="top" width="25%"></td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/35c556af-1752-4a8a-9965-d1e2314b242e" width="240" controls></video>
<br/><a href="https://x.com/Pixelbunny_ai/status/2051985506414768154"><b>@Pixelbunny_ai</b></a>
<br/><sub>- Create Stunning AAA quality shorts with leading models -…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/75051d48-988e-4e0d-9cfa-389d821abec8" width="240" controls></video>
<br/><a href="https://x.com/Adam38363368936/status/2051969842748735596"><b>@Adam38363368936</b></a>
<br/><sub>GPT image 2+Seedance 2</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/8241abd7-3b4e-4b62-8dca-24dac31926cc" width="240" controls></video>
<br/><a href="https://x.com/ai_hakase_/status/2051950389063282894"><b>@ai_hakase_</b></a>
<br/><sub>【AIでNetflix級のUIを爆速生成！GPT Image 2 × Seedance 2.0】 👉   最新のAIを…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/30710ea7-1f06-49b2-ad31-041fa95046c2" width="240" controls></video>
<br/><a href="https://x.com/Hoshimiko_AIart/status/2051947486353433013"><b>@Hoshimiko_AIart</b></a>
<br/><sub>「見たいアニメに間に合わない……！！」</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/8315ea16-32ff-4078-8dce-44d4d2c896d9" width="240" controls></video>
<br/><a href="https://x.com/Dheer_Red/status/2051915196185346333"><b>@Dheer_Red</b></a>
<br/><sub>Seedance 2.0, Veo 3.1, Nano Banana, GPT Image 2—all in one…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/c57c7caf-ab27-4c79-9ca6-b571d7899139" width="240" controls></video>
<br/><a href="https://x.com/NyaiiBubu/status/2051914243193389078"><b>@NyaiiBubu</b></a>
<br/><sub>AI for UGC modal Rp0 itu nyata 😭</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/1899a3a5-da5c-455b-8fa3-d3c3ab830df4" width="240" controls></video>
<br/><a href="https://x.com/apoorvabr/status/2051904397324722349"><b>@apoorvabr</b></a>
<br/><sub>I like the video concepts of @chrisfirst.</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/1718996f-d0e8-4ba8-abef-1d0e725ed22f" width="240" controls></video>
<br/><a href="https://x.com/MaAyyoub/status/2051900019444154376"><b>@MaAyyoub</b></a>
<br/><sub>Don't ruin a new day by thinking about yesterday.</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/a7d5b81e-708e-4bb5-9263-7bfb9c6e0d01" width="240" controls></video>
<br/><a href="https://x.com/halne369/status/2051867032333803722"><b>@halne369</b></a>
<br/><sub>Seedance2.0用の絵コンテ作成のスキルができました！</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/4a76e9c0-0171-4b2a-a74d-90f3e59f80e8" width="240" controls></video>
<br/><a href="https://x.com/RYD232210555420/status/2051847984053469424"><b>@RYD232210555420</b></a>
<br/><sub>朋友设计的无人驾驶公交车 Sumgo，我帮它做了条 AI 概念宣传片。</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/ac2e370f-6986-4ac1-b2ec-9580901d9483" width="240" controls></video>
<br/><a href="https://x.com/Lart_AI/status/2051838590016241772"><b>@Lart_AI</b></a>
<br/><sub>🎮 Built with GPT Image 2 × Seedance 2.0 on LartAI!</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/ad9b0494-b689-4aad-8a50-bcd278110c8b" width="240" controls></video>
<br/><a href="https://x.com/Jake_Joseph/status/2051774091108155844"><b>@Jake_Joseph</b></a>
<br/><sub>Wait, you can put real screenshots inside AI-generated UGC…</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/661be30d-946d-42f6-888c-fc19d8ab6e9d" width="240" controls></video>
<br/><a href="https://x.com/KimAkiyama81/status/2051768139566714958"><b>@KimAkiyama81</b></a>
<br/><sub>Choreographing a hallway action scene using GPT Image 2 and…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/6735dd89-bc7d-462e-8f5f-69fab82158e7" width="240" controls></video>
<br/><a href="https://x.com/ChangningL29508/status/2051743657980748119"><b>@ChangningL29508</b></a>
<br/><sub>Use the same storyboard to generate a realistic character r…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/d3d201fc-0813-4d08-aab0-eb0d7a27f708" width="240" controls></video>
<br/><a href="https://x.com/aiseomastery/status/2051733667106734129"><b>@aiseomastery</b></a>
<br/><sub>THIS AI WORKFLOW TURNS A RAMEN RECIPE INTO A STUNNING ANIME…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/ae6c44a0-8e6a-4ff1-ab1f-99b7aa49af01" width="240" controls></video>
<br/><a href="https://x.com/simplissimus_/status/2051714965485039897"><b>@simplissimus_</b></a>
<br/><sub>Quer dominar a Força e ver sua própria versão Jedi ganhar v…</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/67479af0-384f-471f-a8ef-4ee4727289f0" width="240" controls></video>
<br/><a href="https://x.com/azed_ai/status/2051693299376021888"><b>@azed_ai</b></a>
<br/><sub>Studios sell this as pre-production</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/1800bbc0-e6f2-4289-9d41-ef07c15be380" width="240" controls></video>
<br/><a href="https://x.com/fy360593/status/2051686764054790504"><b>@fy360593</b></a>
<br/><sub>Been seeing a lot of people doing this "Fan cam" content la…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/954dc98f-ab00-4fd5-9106-8671310958ef" width="240" controls></video>
<br/><a href="https://x.com/indrawan_ape/status/2051680370429685963"><b>@indrawan_ape</b></a>
<br/><sub>GPT Image 2 × Seedance 2.0 on @higgsfield is insane.</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/fbf50a8f-459b-47a9-8ab1-3cc89b91d239" width="240" controls></video>
<br/><a href="https://x.com/floopers966/status/2051678374750203983"><b>@floopers966</b></a>
<br/><sub>また最安値入札ミサイルかよ！</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/c793c91a-d280-4c2d-b1fd-d64271f467a8" width="240" controls></video>
<br/><a href="https://x.com/Xaroon_x/status/2051656676441293172"><b>@Xaroon_x</b></a>
<br/><sub>Made with GPT Image 2 + Seedance 2.5 by @yapper_so</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/998a71a7-0481-4e93-a717-36295181449c" width="240" controls></video>
<br/><a href="https://x.com/MonetizationDon/status/2051644080803750092"><b>@MonetizationDon</b></a>
<br/><sub>I decided to create my own Afrobeats Mortal Kombat-style sh…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/eaadef33-8db9-4aad-9c2e-a455fcf896ad" width="240" controls></video>
<br/><a href="https://x.com/roomA708/status/2051639024574697952"><b>@roomA708</b></a>
<br/><sub>GPT-Image-2 × Seedance 2.0で、Osmo Pocket 4の“架空CM”を作ってみました。</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/6a66e25d-2ae1-469f-896c-3f0593a79f8f" width="240" controls></video>
<br/><a href="https://x.com/vkuoo/status/2051637837951615142"><b>@vkuoo</b></a>
<br/><sub>Using Midjourney to generate the original images, GPT Image…</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/b6fdbff6-23c8-4c6e-9642-7c7fca112b35" width="240" controls></video>
<br/><a href="https://x.com/RadineerE10/status/2051622937808318654"><b>@RadineerE10</b></a>
<br/><sub>「YouMind」が世界最大級の無料AIプロンプトライブラリとして存在感を増している。</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/0fc459c5-03bc-4fce-928c-40ff34acf989" width="240" controls></video>
<br/><a href="https://x.com/aivoxyy/status/2051621547518083130"><b>@aivoxyy</b></a>
<br/><sub>GPT Image 2 + Seedance 2.5 a police chase of new 2026 Chevr…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/ec1de9ac-97a4-4648-bab6-5ae8818377c1" width="240" controls></video>
<br/><a href="https://x.com/aadi29494/status/2051594382437232667"><b>@aadi29494</b></a>
<br/><sub>Made a LEGO build-process video with GPT Image 2 + Seedance…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/cdb64846-fbfc-4b0f-8a18-9a55552eff87" width="240" controls></video>
<br/><a href="https://x.com/mmarch_ai/status/2051591272918299085"><b>@mmarch_ai</b></a>
<br/><sub>Con GPT Image 2 dominas la composición: añade textos largos…</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/c2ca0649-d276-4ae6-9d1f-e68a0907fc20" width="240" controls></video>
<br/><a href="https://x.com/D_studioproject/status/2051580845606191260"><b>@D_studioproject</b></a>
<br/><sub>How to join a cult with GPT Image 2 x Seedance 2.0 Anime St…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/6f206801-4d40-44a0-971b-3500f7619f1b" width="240" controls></video>
<br/><a href="https://x.com/EgeUymaz/status/2051576423089901874"><b>@EgeUymaz</b></a>
<br/><sub>Storyboarded with GPT Image 2.</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/399714ae-3ac1-4540-b1db-be9320051ee0" width="240" controls></video>
<br/><a href="https://x.com/CurieuxExplorer/status/2051536554691334385"><b>@CurieuxExplorer</b></a>
<br/><sub>Quiet Growth 🌱</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/da772e93-8226-4ac6-aff8-6b9786c861ce" width="240" controls></video>
<br/><a href="https://x.com/josepho/status/2051535229161021618"><b>@josepho</b></a>
<br/><sub>My new AI minishort, Dance of destruction, based on an old…</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/acf55ef2-63e7-420a-9d9a-61b97f2165f9" width="240" controls></video>
<br/><a href="https://x.com/iswangwenbin/status/2051528434225234302"><b>@iswangwenbin</b></a>
<br/><sub>我也来交作业了👇 Hyperframes + Mimo TTS + GPT Image 2 + Seedance 2.5</sub>
</td>
<td align="center" valign="top" width="25%"></td>
<td align="center" valign="top" width="25%"></td>
<td align="center" valign="top" width="25%"></td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/4fbcf8e4-c509-4ddd-8961-855881b3c2c9" width="240" controls></video>
<br/><a href="https://x.com/HAL2400AI/status/2050076981702906004"><b>@HAL2400AI</b></a> · <sub>6,721,336 views</sub>
<br/><sub>ドンキで爆速品出しするゲームのプレイ映像。</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/66649bde-1a17-4ea7-92b9-1b06b5e6a5d8" width="240" controls></video>
<br/><a href="https://x.com/0xbisc/status/2050154597340287143"><b>@0xbisc</b></a> · <sub>224,490 views</sub>
<br/><sub>Kitchen Hunt</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/33ef696a-45ff-4a35-84d3-4ee0c65629cc" width="240" controls></video>
<br/><a href="https://x.com/ElevenCreative/status/2049866735898009836"><b>@ElevenCreative</b></a> · <sub>115,974 views</sub>
<br/><sub>Create UGC videos in minutes with ElevenCreative.</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/3c851335-abd7-46bb-9f44-7e5b4ce44d8b" width="240" controls></video>
<br/><a href="https://x.com/Saccc_c/status/2049769037660360897"><b>@Saccc_c</b></a> · <sub>115,759 views</sub>
<br/><sub>用 GPT Image 2 + Seedance 2.5，还原了故宫太和殿的建造全过程🤩</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/d4902050-6912-4ab1-b204-cb373e0eafe3" width="240" controls></video>
<br/><a href="https://x.com/ZaraIrahh/status/2049668274330255388"><b>@ZaraIrahh</b></a> · <sub>55,203 views</sub>
<br/><sub>Created with Gpt Image 2 + Seedance 2.0 on @SJinn_Agent</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/d710c64b-8b05-4848-ae11-16a5ac303416" width="240" controls></video>
<br/><a href="https://x.com/johnAGI168/status/2050190239398781120"><b>@johnAGI168</b></a> · <sub>49,957 views</sub>
<br/><sub>The future of AI video is here, and it is completely mind-b…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/8da15a4b-4f5e-47c7-a97b-891ef8227b52" width="240" controls></video>
<br/><a href="https://x.com/GumVue/status/2050314912094687425"><b>@GumVue</b></a> · <sub>45,606 views</sub>
<br/><sub>Create with a Custom GPT  - Short Film Prompt Generator :…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/b78cdad1-5f5c-4309-880d-6efdadf0a18d" width="240" controls></video>
<br/><a href="https://x.com/seiiiiiiiiiiru/status/2049983823308570686"><b>@seiiiiiiiiiiru</b></a> · <sub>41,147 views</sub>
<br/><sub>Midjourney V8.1 ↓ GPT image 2.0 ↓ Seedance 2.0</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/6f3b85bc-b409-4c1a-8fdb-325d9d6b0291" width="240" controls></video>
<br/><a href="https://x.com/VORTEX_Promos/status/2049614941812863376"><b>@VORTEX_Promos</b></a> · <sub>40,410 views</sub>
<br/><sub>TOP 7 INSANE GPT Image 2 x Seedance 2.0 Prompts You Must Try</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/3cb1548c-59a8-4e80-8969-759e7f6ff7d9" width="240" controls></video>
<br/><a href="https://x.com/ElCopyMaster/status/2049513235121144002"><b>@ElCopyMaster</b></a> · <sub>39,205 views</sub>
<br/><sub>Pollo AI acaba de cambiar la creación de anuncios 🤯</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/e4dbbfac-0b0c-4fed-a9f3-309da015cc0e" width="240" controls></video>
<br/><a href="https://x.com/4111J_/status/2049817671714443561"><b>@4111J_</b></a> · <sub>31,198 views</sub>
<br/><sub>What’s in my bag?</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/a29e9b73-e176-4e46-9377-22bf5c2d4f89" width="240" controls></video>
<br/><a href="https://x.com/AIwithkhan/status/2049732042695623134"><b>@AIwithkhan</b></a> · <sub>28,965 views</sub>
<br/><sub>Here we go GPT Image 2 and Seedance 2.0 is now live on @ins…</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/3e29d94c-a175-4df9-8568-4b0707c5f775" width="240" controls></video>
<br/><a href="https://x.com/rovvmut_/status/2049900959028109567"><b>@rovvmut_</b></a> · <sub>28,036 views</sub>
<br/><sub>GPT Image 2 and Seedance 2.0 on @insmind_com</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/c8919582-b859-4b38-b456-a02683700f1e" width="240" controls></video>
<br/><a href="https://x.com/aimikoda/status/2049589670581874777"><b>@aimikoda</b></a> · <sub>27,837 views</sub>
<br/><sub>Gpt Image 2 + Seedance 2.0 Trailer Workflow</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/aed7449c-40b7-4160-8a6f-2a824b0d95f2" width="240" controls></video>
<br/><a href="https://x.com/HBCoop_/status/2049853870172410026"><b>@HBCoop_</b></a> · <sub>20,844 views</sub>
<br/><sub>Decided to test myself out in the storyboard workflow.</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/028cd6eb-d4cd-4ab3-8484-4d895173d8a6" width="240" controls></video>
<br/><a href="https://x.com/franpradasAI/status/2050168636321440010"><b>@franpradasAI</b></a> · <sub>19,487 views</sub>
<br/><sub>🚨 NOVEDAD: Un anuncio así cuesta $2M</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/6fd777ca-b6d9-43b9-a4a4-3b2b41a4fd04" width="240" controls></video>
<br/><a href="https://x.com/john_my07/status/2049524601471074422"><b>@john_my07</b></a> · <sub>19,165 views</sub>
<br/><sub>Crafted this one by turning a movement sheet as a reference…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/31aef043-4277-4f3e-bcca-d79d6747f9c1" width="240" controls></video>
<br/><a href="https://x.com/MrLarus/status/2050505429529104752"><b>@MrLarus</b></a> · <sub>18,511 views</sub>
<br/><sub>太飒了！ 🤯用ChatGPT+Seedance生成街头篮球1v1，真实感很强！  运球试探、crossover变向、欧…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/8fad0bd0-251f-4602-9573-4d2b2bdd2c53" width="240" controls></video>
<br/><a href="https://x.com/LaTwitchance/status/2050183976657047764"><b>@LaTwitchance</b></a> · <sub>17,313 views</sub>
<br/><sub>Une vidéo de gameplay montre un jeu où il faut réapprovisio…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/741ee092-27aa-40b9-959c-0ec5e2944a62" width="240" controls></video>
<br/><a href="https://x.com/Marco_Exito/status/2050219814678098028"><b>@Marco_Exito</b></a> · <sub>14,156 views</sub>
<br/><sub>💥ÚLTIMA HORA:  ¡GPT-IMAGE-2 y Seedance 2.0 ya están disponi…</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/a410a383-9744-4f1f-8ba6-92eba2cdbec4" width="240" controls></video>
<br/><a href="https://x.com/JoyLi629/status/2049740242085667272"><b>@JoyLi629</b></a> · <sub>13,056 views</sub>
<br/><sub>GPT image2 + Seedance 2.0 做产品爆炸视频💥太香了</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/a6b9b482-32fa-41e7-bfb2-f97b2cf46722" width="240" controls></video>
<br/><a href="https://x.com/doctorwasif/status/2050244639253569886"><b>@doctorwasif</b></a> · <sub>12,897 views</sub>
<br/><sub>Chatgpt GPT-2 & Seedance 2 on @yapper_so</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/c00ed740-192d-4d5b-a981-a6664c9bce07" width="240" controls></video>
<br/><a href="https://x.com/code_bykuti/status/2049852139112182181"><b>@code_bykuti</b></a> · <sub>10,592 views</sub>
<br/><sub>We’re not generating images anymore…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/af52163e-dab5-4c14-8531-c3e9f4fcf2d8" width="240" controls></video>
<br/><a href="https://x.com/igus_ai/status/2049527468143329284"><b>@igus_ai</b></a> · <sub>9,010 views</sub>
<br/><sub>Ahora puedes crear wallpapers de cualquier jugador o equipo…</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/98001464-cbf5-4dd8-8161-a8d7a86d0afd" width="240" controls></video>
<br/><a href="https://x.com/Diplomeme/status/2049752171474993460"><b>@Diplomeme</b></a> · <sub>8,011 views</sub>
<br/><sub>Makeup tutorial (ft.</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/e14db781-59cf-4ad2-8cbc-41fa99bbbebc" width="240" controls></video>
<br/><a href="https://x.com/XMonetizationC_/status/2049527585269551150"><b>@XMonetizationC_</b></a> · <sub>7,509 views</sub>
<br/><sub>GRWM (ft.</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/0b0e902b-325e-42e5-98f1-57177f73124e" width="240" controls></video>
<br/><a href="https://x.com/nrqa__/status/2049836461755949357"><b>@nrqa__</b></a> · <sub>7,319 views</sub>
<br/><sub>GPT-IMAGE-2 &amp; Seedance 2.0 is now officially available…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/acba4f2e-b8aa-47ea-8a08-e05d44523d45" width="240" controls></video>
<br/><a href="https://x.com/IqraSaifiii/status/2049845664880955862"><b>@IqraSaifiii</b></a> · <sub>7,004 views</sub>
<br/><sub>Create your own Influencer live stream 🔥</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/f952740e-5a89-442e-a45a-38fd496acdef" width="240" controls></video>
<br/><a href="https://x.com/IntLab0000/status/2050227050502639625"><b>@IntLab0000</b></a> · <sub>6,444 views</sub>
<br/><sub>【Seedance 2.0でSora2を目指すテスト】Seedanceに直接長文のプロンプトで依頼する代わりに、gpt…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/ef66fa7a-c595-4b42-88e0-bd81464caa6b" width="240" controls></video>
<br/><a href="https://x.com/weiinberg/status/2049867302309707927"><b>@weiinberg</b></a> · <sub>6,126 views</sub>
<br/><sub>GPT Image 2 x Seedance 2.0 on @insmind_com</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/c21ebea6-629e-494c-b8ea-b8fb5b6b2d87" width="240" controls></video>
<br/><a href="https://x.com/angeldot_/status/2049528144256737579"><b>@angeldot_</b></a> · <sub>6,114 views</sub>
<br/><sub>Puedes crear wallpapers animados como este en segundos</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/9c0fcc5d-b76e-4b6d-b123-9d65837b1263" width="240" controls></video>
<br/><a href="https://x.com/Just_sharon7/status/2050430486548447502"><b>@Just_sharon7</b></a> · <sub>6,084 views</sub>
<br/><sub>Are you ready to buy this necklace??</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/f4171c4c-923a-4af1-aeb2-11ec47174f17" width="240" controls></video>
<br/><a href="https://x.com/Sheldon056/status/2049832802078838857"><b>@Sheldon056</b></a> · <sub>5,910 views</sub>
<br/><sub>GPT Image 2 and Seedance 2.0 are now live on @insmind_com</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/bc924494-934c-4175-a32d-8b8ef66fc07e" width="240" controls></video>
<br/><a href="https://x.com/nicos_ai/status/2049526583212327013"><b>@nicos_ai</b></a> · <sub>5,776 views</sub>
<br/><sub>Ahora puedes crear Wallpapers animados en segundos</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/1e2860b3-802e-4d5d-953d-a81c1e5e8d03" width="240" controls></video>
<br/><a href="https://x.com/promptsref/status/2050489527475507706"><b>@promptsref</b></a> · <sub>5,635 views</sub>
<br/><sub>Create a short film like this in just 1 minute with GPT Ima…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/7205e175-7e35-44a2-9b3e-3e0d65e0ca72" width="240" controls></video>
<br/><a href="https://x.com/AIwithSynthia/status/2049818475846332898"><b>@AIwithSynthia</b></a> · <sub>5,248 views</sub>
<br/><sub>Excited to inform you that GPT Image 2 and Seedance 2.0 are…</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/b6a422ee-1bf8-4098-b463-b393c2d449f5" width="240" controls></video>
<br/><a href="https://x.com/wanerfu/status/2050457318194815166"><b>@wanerfu</b></a> · <sub>5,165 views</sub>
<br/><sub>我用动作参考图来制作舞蹈动画，使用了 Seedance 2.0 + GPT Image 2.0</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/dcec0956-895f-4ab8-80e8-889f4efb2e7f" width="240" controls></video>
<br/><a href="https://x.com/FinanceYF5/status/2049672873888116956"><b>@FinanceYF5</b></a> · <sub>4,039 views</sub>
<br/><sub>有人用 GPT Image 2 × Seedance 2.0 在 OpenArt 上制作一支万宝路广告。</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/31ffd0f8-273c-460b-acd3-3e3fea5ef3fc" width="240" controls></video>
<br/><a href="https://x.com/meng_dagg695/status/2049739564630307176"><b>@meng_dagg695</b></a> · <sub>3,885 views</sub>
<br/><sub>GPT image 2 × Seedance 2.0 combo 🔥 on @yapper_so</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/9d4a97cf-c95b-495b-bf62-34b8b95c6d4b" width="240" controls></video>
<br/><a href="https://x.com/AI_Arabic1/status/2049534174646940051"><b>@AI_Arabic1</b></a> · <sub>3,867 views</sub>
<br/><sub>شوفوا الإبداع 😱!!</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/fc83dd63-3809-47e9-9578-c97f235327f2" width="240" controls></video>
<br/><a href="https://x.com/AIwithSarah_/status/2049838433582067838"><b>@AIwithSarah_</b></a> · <sub>3,566 views</sub>
<br/><sub>GPT Image 2 and Seedance 2.0 is now available on @insmind_c…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/af16374f-c77b-4929-9ede-9ea6f15551ed" width="240" controls></video>
<br/><a href="https://x.com/MatiasSchrank/status/2050185710561276382"><b>@MatiasSchrank</b></a> · <sub>3,564 views</sub>
<br/><sub>Así lo hice con Smart Shot de @openart_ai:</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/04043531-d981-4798-ade7-87e1bcd70144" width="240" controls></video>
<br/><a href="https://x.com/ivnways/status/2050149994691523033"><b>@ivnways</b></a> · <sub>3,303 views</sub>
<br/><sub>ÚLTIMA HORA: ¡GPT-IMAGE-2 y Seedance 2.0 ya disponibles gra…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/a7734353-2509-4b77-96cc-6b42e6fd4699" width="240" controls></video>
<br/><a href="https://x.com/SwayamShrma/status/2049970629450088960"><b>@SwayamShrma</b></a> · <sub>2,908 views</sub>
<br/><sub>From rough Idea to short film just by using a workflow that…</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/fd1436bc-ebaf-4706-82d7-7ee4e5056963" width="240" controls></video>
<br/><a href="https://x.com/Alex_Inspira/status/2050210855242084796"><b>@Alex_Inspira</b></a> · <sub>2,888 views</sub>
<br/><sub>Así es exactamente como lo hice.</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/7f246962-7346-4e52-9049-6f7cc31e1f3f" width="240" controls></video>
<br/><a href="https://x.com/oggii_0/status/2049859002398556580"><b>@oggii_0</b></a> · <sub>2,655 views</sub>
<br/><sub>I tested a full AI food commercial workflow using ONE promp…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/3dcc955f-6441-4c57-bf77-371c5d51ebb7" width="240" controls></video>
<br/><a href="https://x.com/Ciri_ai/status/2049861486575747436"><b>@Ciri_ai</b></a> · <sub>2,603 views</sub>
<br/><sub>One prompt → full cinematic sequence all generated inside @…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/fa0834a6-a585-492a-b92f-22ed8e9d155b" width="240" controls></video>
<br/><a href="https://x.com/Taaruk_/status/2049702491768684839"><b>@Taaruk_</b></a> · <sub>2,485 views</sub>
<br/><sub>GPT IMAGE 2 + seedance 2.0</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/27c79a49-058b-45d9-ae76-8bb9d0612571" width="240" controls></video>
<br/><a href="https://x.com/noahsolomon/status/2050145785891914119"><b>@noahsolomon</b></a> · <sub>2,477 views</sub>
<br/><sub>I love using fal to make developing fal easier.</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/043c67b9-c0a6-450e-a061-0173ddde350b" width="240" controls></video>
<br/><a href="https://x.com/harboriis/status/2050083212664426882"><b>@harboriis</b></a> · <sub>2,389 views</sub>
<br/><sub>A complete dance sequence mapped frame by frame</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/8f1842af-4ea2-46a5-9719-64aafc14d512" width="240" controls></video>
<br/><a href="https://x.com/techyoutbe/status/2049819747597029627"><b>@techyoutbe</b></a> · <sub>2,354 views</sub>
<br/><sub>One workspace.</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/e6b408d1-888f-47d5-bb70-2aa4d041d666" width="240" controls></video>
<br/><a href="https://x.com/ZetoGroovin/status/2050176480861094147"><b>@ZetoGroovin</b></a> · <sub>2,298 views</sub>
<br/><sub>『神降ろし』- AI MUSIC VIDEO - 和の雰囲気の曲と映像でMV作ってみました。</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/dd6544dc-4107-4bd1-a7ea-35e6bf23f0a0" width="240" controls></video>
<br/><a href="https://x.com/0xtonixie/status/2050449563773981106"><b>@0xtonixie</b></a> · <sub>2,165 views</sub>
<br/><sub>GPT的images2 ＋seedance2.0绝对是制作AI漫剧的最佳组合：</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/49846a04-64a8-4bff-bac8-b193f62256d3" width="240" controls></video>
<br/><a href="https://x.com/iamrealsnow/status/2049770674886152232"><b>@iamrealsnow</b></a> · <sub>1,764 views</sub>
<br/><sub>GRWM (Male Minimal Editorial) Using GPT image 2.0 + Seedanc…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/26160c30-a15b-4de8-b946-df6573d70c0d" width="240" controls></video>
<br/><a href="https://x.com/budgetpixel/status/2049684059278676332"><b>@budgetpixel</b></a> · <sub>1,754 views</sub>
<br/><sub>GPT Image 2.0 + Seedance 2.0 = a powerful dance workflow</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/f070db63-ea05-41bb-8b55-9f697ab6844a" width="240" controls></video>
<br/><a href="https://x.com/0kncn/status/2050264466852368557"><b>@0kncn</b></a> · <sub>1,720 views</sub>
<br/><sub>Tesla vs Einstein Tekken evreninde</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/1ff92c6d-0131-4147-840b-82322df72bb7" width="240" controls></video>
<br/><a href="https://x.com/iX00AI/status/2050356236814885066"><b>@iX00AI</b></a> · <sub>1,673 views</sub>
<br/><sub>実際の流れ👇  1文入力 → Shot Plan（設計図）生成 → そのまま映像生成  プロンプトの工夫も編集も不要。…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/b57613c4-0838-410c-9a33-785b6002b34e" width="240" controls></video>
<br/><a href="https://x.com/ashen_one/status/2049601589573292154"><b>@ashen_one</b></a> · <sub>1,608 views</sub>
<br/><sub>GPT 2.0 + Seedance 2.0 = Brand Goldmine</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/92da6dee-b575-4ba9-a405-d94a3572b18f" width="240" controls></video>
<br/><a href="https://x.com/obrunookamoto/status/2050156722086461498"><b>@obrunookamoto</b></a> · <sub>1,338 views</sub>
<br/><sub>A Higgsfield conectou 30+ modelos de geração de imagem e ví…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/6a4f6292-f7fe-4a20-a6f1-4eee47e5ccad" width="240" controls></video>
<br/><a href="https://x.com/Kashberg_0/status/2050117126397329698"><b>@Kashberg_0</b></a> · <sub>1,291 views</sub>
<br/><sub>GPT IMAGE 2 and Seedance 2.0</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/ed99f828-225c-4b28-a667-879290c4838a" width="240" controls></video>
<br/><a href="https://x.com/sara4ai/status/2050189053979496926"><b>@sara4ai</b></a> · <sub>1,229 views</sub>
<br/><sub>مرحبا يا أصدقاء  خلال هذا الأسبوع لاحظت أعمالًا مبهرة باستخ…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/9718f4a9-8466-4622-af0a-03788c2b27ae" width="240" controls></video>
<br/><a href="https://x.com/bmx_ai13/status/2050432594647642414"><b>@bmx_ai13</b></a> · <sub>1,220 views</sub>
<br/><sub>A super simple workflow: 2 character images → GPT Image 2.0…</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/14da241f-97fb-4162-ad1c-77e54ab3c29c" width="240" controls></video>
<br/><a href="https://x.com/ChillaiKalan__/status/2049833865825632522"><b>@ChillaiKalan__</b></a> · <sub>1,196 views</sub>
<br/><sub>GPT Image 2 and Seedance 2.0 on @insmind_com</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/ab068907-e9b7-4762-846e-2d0ca3adb48d" width="240" controls></video>
<br/><a href="https://x.com/suji_pop/status/2050135943294878035"><b>@suji_pop</b></a> · <sub>1,173 views</sub>
<br/><sub>Subway Surfer in a post apocalyptic world, with the graphic…</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/5207f874-d9a2-47c2-afe9-6c0b07b87e47" width="240" controls></video>
<br/><a href="https://x.com/densancar/status/2050210215237173629"><b>@densancar</b></a> · <sub>1,148 views</sub>
<br/><sub>Claude Code + GPT 2 + Seedance 2.0 Makes VIRAL AI UGC Videos</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/681faaa8-d52f-427d-b192-b4ac8b12ebc0" width="240" controls></video>
<br/><a href="https://x.com/nexudotio/status/2049775355586576758"><b>@nexudotio</b></a> · <sub>1,128 views</sub>
<br/><sub>Open Design now ships images AND videos.</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/a9a2a2e0-ab3f-45e1-8eeb-903c2e72bccf" width="240" controls></video>
<br/><a href="https://x.com/OiiOii_AI/status/2049777567193043420"><b>@OiiOii_AI</b></a> · <sub>1,108 views</sub>
<br/><sub>OiiOiiで、話題のプロンプトを GPT Image 2 × Seedance 2.0 で試してみました。</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/70b7d00f-a84a-4b96-b53f-9ffc3cf25a67" width="240" controls></video>
<br/><a href="https://x.com/QingQ77/status/2050201770320949363"><b>@QingQ77</b></a> · <sub>1,051 views</sub>
<br/><sub>cool 使用 GPT Image 2 + Seedance 2.5 创建游戏界面的视频动画</sub>
</td>
</tr></table>

<table><tr>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/d9a22507-f0b6-4186-886c-33129a23d651" width="240" controls></video>
<br/><a href="https://x.com/Parul_Gautam7/status/2050184972942946328"><b>@Parul_Gautam7</b></a> · <sub>1,044 views</sub>
<br/><sub>Here’s how it actually works.</sub>
</td>
<td align="center" valign="top" width="25%">
<video src="https://github.com/user-attachments/assets/a77e53bb-5764-4fd7-b44e-82b369195a83" width="240" controls></video>
<br/><a href="https://x.com/joshesye/status/2049715911838355739"><b>@joshesye</b></a> · <sub>1,020 views</sub>
<br/><sub>茶叶品牌 TVC《一口春山》</sub>
</td>
<td align="center" valign="top" width="25%"></td>
<td align="center" valign="top" width="25%"></td>
</tr></table>

<a id="parameters"></a>
## 參數與實際檢查

Seedance 2.5 I2V 接受 1–2 張 `image_urls`，作為首幀或首尾幀，比例僅接受 `aspect_ratio: "adaptive"`，請預先準備目標比例圖片；單次生成 4–30 秒，較短鏡頭在剪輯時裁切，超過 30 秒的成片拆段組合或延展；目前 API 輸出為 480p／720p／1080p，其他產品的 4K 宣傳不能視為 EvoLink API 支援；提示詞寫 24fps 不等於設定幀率參數；逐項檢查產品細節、身份、動作與聲音，網格、提示詞長度或限制皆不保證一致性；依真實任務帳單比較成本，不預設固定倍數

[@Iancu_ai — community prompt experiment](https://x.com/Iancu_ai/status/2047882924679168083)

[API / errors / recovery](docs/api-workflow.md) · [Maintenance](docs/maintenance.md)

<a id="related-resources"></a>
## 相關資源

- [GPT Image 2 prompts](https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=image_prompts)
- [Seedance 2.5 prompts](https://github.com/EvoLinkAI/awesome-seedance-2.5-prompts)
- [Seedance 2.5 guide](https://github.com/EvoLinkAI/awesome-seedance-2.5-guide)
- [GPT Image 2 Skill](https://github.com/EvoLinkAI/gpt-image-2-gen-skill) — GPT Image 2
- [Legacy Seedance Skill](https://github.com/EvoLinkAI/seedance2-video-gen-skill-for-openclaw) — **Seedance 2.0**, `npx evolink-seedance`; [Seedance 2.5 → MCP / CLI](https://evolink.ai/mcp?utm_source=github&utm_medium=readme&utm_campaign=GPT-Image-2-Seedance-2.5-Workflow&utm_content=current_video_route)

## 🙏 致謝

本儲存庫的靈感來自優秀的開放工作流程合集與社群分享的實驗。

感謝以下公開分享作品、使這些案例研究成為可能的創作者與貢獻者：
[@szounft](https://x.com/szounft) · [@Toshi_nyaruo_AI](https://x.com/Toshi_nyaruo_AI) · [@ponyodong](https://x.com/ponyodong) · [@servasyy_ai](https://x.com/servasyy_ai) · [@YaReYaRu30Life](https://x.com/YaReYaRu30Life) · [@fukaborichannel](https://x.com/fukaborichannel) · [@Shin_Engineer](https://x.com/Shin_Engineer) · [@ai_mitosan](https://x.com/ai_mitosan) · [@kiyoshi_shin](https://x.com/kiyoshi_shin) · [@AbleGPT](https://x.com/AbleGPT) · [@patata1216](https://x.com/patata1216) · [@peter6759](https://x.com/peter6759) · [@hibi_ai__](https://x.com/hibi_ai__) · [@heygentlewhale](https://x.com/heygentlewhale) · [@ai_gezgini](https://x.com/ai_gezgini) · [@Tz_2022](https://x.com/Tz_2022) · [@old_pgmrs_will](https://x.com/old_pgmrs_will) · [@0xbisc](https://x.com/0xbisc) · [@Iancu_ai](https://x.com/Iancu_ai) · [@Jake_Joseph](https://x.com/Jake_Joseph) · [@venturetwins](https://x.com/venturetwins) · [@0xInk_](https://x.com/0xInk_) · [@markgadala](https://x.com/markgadala) · [@Ankit_patel211](https://x.com/Ankit_patel211) · [@Ciri_ai](https://x.com/Ciri_ai) · [@nimentrix](https://x.com/nimentrix) · [@insmind_com](https://x.com/insmind_com) · [@kingofdairyque](https://x.com/kingofdairyque) · [@Kashberg_0](https://x.com/Kashberg_0) · [@airina_xyz](https://x.com/airina_xyz) · [@CoffeeVectors](https://x.com/CoffeeVectors) · [@mdmadeit](https://x.com/mdmadeit) · [@Morph_VGart](https://x.com/Morph_VGart) · [@MEnesKirca](https://x.com/MEnesKirca) · [@MrLarus](https://x.com/MrLarus) · [@AYi_AInotes](https://x.com/AYi_AInotes) · [@8fstudioz](https://x.com/8fstudioz) · [@_DAntunes_](https://x.com/_DAntunes_) · [@promptsref](https://x.com/promptsref) · [@Just_sharon7](https://x.com/Just_sharon7) · [@wanerfu](https://x.com/wanerfu) · [@AIwithkhan](https://x.com/AIwithkhan) · [@0xtonixie](https://x.com/0xtonixie) · [@doctorwasif](https://x.com/doctorwasif) · [@HAL2400AI](https://x.com/HAL2400AI) · [@bmx_ai13](https://x.com/bmx_ai13) · [@ZaraIrahh](https://x.com/ZaraIrahh) · [@iX00AI](https://x.com/iX00AI) · [@GumVue](https://x.com/GumVue) · [@adriansolarzz](https://x.com/adriansolarzz) · [@0kncn](https://x.com/0kncn) · [@john_my07](https://x.com/john_my07) · [@XMonetizationC_](https://x.com/XMonetizationC_) · [@harboriis](https://x.com/harboriis) · [@IntLab0000](https://x.com/IntLab0000) · [@Marco_Exito](https://x.com/Marco_Exito) · [@Alex_Inspira](https://x.com/Alex_Inspira) · [@densancar](https://x.com/densancar) · [@QingQ77](https://x.com/QingQ77) · [@johnAGI168](https://x.com/johnAGI168) · [@sara4ai](https://x.com/sara4ai) · [@MatiasSchrank](https://x.com/MatiasSchrank) · [@Parul_Gautam7](https://x.com/Parul_Gautam7) · [@LaTwitchance](https://x.com/LaTwitchance) · [@ZetoGroovin](https://x.com/ZetoGroovin) · [@franpradasAI](https://x.com/franpradasAI) · [@obrunookamoto](https://x.com/obrunookamoto) · [@ivnways](https://x.com/ivnways) · [@noahsolomon](https://x.com/noahsolomon) · [@OiiOii_AI](https://x.com/OiiOii_AI) · [@suji_pop](https://x.com/suji_pop) · [@SuguruKun_ai](https://x.com/SuguruKun_ai) · [@aimikoda](https://x.com/aimikoda) · [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru) · [@SwayamShrma](https://x.com/SwayamShrma) · [@IqraSaifiii](https://x.com/IqraSaifiii) · [@rovvmut_](https://x.com/rovvmut_) · [@ashen_one](https://x.com/ashen_one) · [@weiinberg](https://x.com/weiinberg) · [@ElevenCreative](https://x.com/ElevenCreative) · [@SunNeverSetsX](https://x.com/SunNeverSetsX) · [@oggii_0](https://x.com/oggii_0) · [@HBCoop_](https://x.com/HBCoop_) · [@code_bykuti](https://x.com/code_bykuti) · [@AIwithSarah_](https://x.com/AIwithSarah_) · [@nrqa__](https://x.com/nrqa__) · [@ChillaiKalan__](https://x.com/ChillaiKalan__) · [@Sheldon056](https://x.com/Sheldon056) · [@techyoutbe](https://x.com/techyoutbe) · [@AIwithSynthia](https://x.com/AIwithSynthia) · [@4111J_](https://x.com/4111J_) · [@hrrcnes](https://x.com/hrrcnes) · [@nexudotio](https://x.com/nexudotio) · [@iamrealsnow](https://x.com/iamrealsnow) · [@Saccc_c](https://x.com/Saccc_c) · [@Raul_IA_Prod](https://x.com/Raul_IA_Prod) · [@Diplomeme](https://x.com/Diplomeme) · [@JoyLi629](https://x.com/JoyLi629) · [@meng_dagg695](https://x.com/meng_dagg695) · [@bindureddy](https://x.com/bindureddy) · [@FinanceYF5](https://x.com/FinanceYF5) · [@joshesye](https://x.com/joshesye) · [@Taaruk_](https://x.com/Taaruk_) · [@budgetpixel](https://x.com/budgetpixel) · [@VORTEX_Promos](https://x.com/VORTEX_Promos) · [@AI_Arabic1](https://x.com/AI_Arabic1) · [@angeldot_](https://x.com/angeldot_) · [@igus_ai](https://x.com/igus_ai) · [@nicos_ai](https://x.com/nicos_ai) · [@ElCopyMaster](https://x.com/ElCopyMaster)

*我們無法保證每個案例都歸屬於原始創作者。如有任何需要更正之處，請與我們聯繫，我們會進行更新。*

如果你有更多有趣的工作流程案例想分享，歡迎聯繫我們，幫助我們擴展 Evolink 工作流程庫。

[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/GPT-Image-2-Seedance-2.5-Workflow&type=Date)](https://www.star-history.com/#EvoLinkAI/GPT-Image-2-Seedance-2.5-Workflow&Date)
