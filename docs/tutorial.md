# Gemini 4 Carbon tutorial: from prompt to video

English · [简体中文](zh-CN/tutorial.md) · [← Back to the collection](../README.md)

From a prompt to an MP4 in four steps. Carbon writes a web page; you play it and record it.

## 1. Start from a video you like

Open any title in the [collection](../README.md) to reach its page on [SandBase Lab][lab]: the video, the original post and, when the creator shared one, the prompt. Press **Recreate**. Lab opens the text arena with the post loaded and Gemini 4 Carbon selected. Sign in, run it, and you get the HTML back, with a live preview.

No prompt shared? Write one with the [prompt guide](prompt-guide.md). It has a fill-in template.

## 2. Compare models on the same prompt

This collection was built on comparisons — 39 of the 98 videos are same-prompt head-to-heads, most of them against Claude Opus 5.5. To run your own: in the [text arena][arena], add one or two more models next to Carbon (for example `anthropic/claude-opus-5.5`, `openai/gpt-6-astra` or `deepseek/deepseek-v4.1-flash`) and run once. Every model gets the same words, and each result shows its cost and time. That is the quickest way to check a claim from the [comparison page](model-comparison.md) on your own task — one prompt, one shot each, then record both pages the same way.

## 3. Or call the API

Gemini 4 Carbon is `google/gemini-4-argon` on SandBase, OpenAI-compatible — the Carbon checkpoint is served under the Argon model id.

1. Create a key in the [console][keys] and export it: `export SANDBASE_API_KEY=sk-sb-...`
2. Save your prompt as `prompt.txt`.
3. Run:

```bash
jq -n --rawfile prompt prompt.txt '{
  model: "google/gemini-4-argon",
  max_tokens: 65536,
  messages: [{role: "user", content: $prompt}]
}' |
curl -sS --max-time 900 https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d @- > response.json

jq -r '.choices[0].message.content' response.json | sed '/^```/d' > gemini-carbon.html
jq '.usage' response.json
```

- `max_tokens: 65536`: thinking is always on for this model and the hidden reasoning tokens come out of the same budget. The pages in this collection are long single files — a comparable four-model run had the rival writing 1,634 parts in code ([@0xPorterio][shark]) — and 65,536 is the maximum the API accepts. With a tight limit you get a truncated page and still pay for the tokens.
- `--max-time 900`: one long page can take several minutes. Arena runs reported in this collection took 24 to 85 minutes per page.
- `sed '/^```/d'` removes Markdown fences if the model added them.
- `usage` shows the tokens you were billed for, including reasoning. Reasoning bills at the output rate ($20 per million), input at $4 per million, cached input at 0.05x; prices are on the [model page][model].
- There is no `reasoning_effort` parameter on this model — the API accepts `max_tokens`, `temperature`, `top_p`, `stop`, `seed` and the tool/response fields, and the model picks its own effort. When a post says "low effort", that was an Arena-side setting.
- Images, video, audio and PDF work as input: the model is multimodal, so you can put a reference frame or clip in `messages[].content` instead of describing it.

Open `gemini-carbon.html` in a browser. If it is blank, open the developer console: the usual causes are a truncated file (raise `max_tokens`) or a CDN that did not load (ask for everything inline). If the scene works but a control does nothing, check the interactions next — the posts here judge pages by whether every tool works, not just by the render.

### With the SandBase CLI

The same call through the [SandBase CLI](https://www.npmjs.com/package/@sandbaseai/cli), which reads `SANDBASE_API_KEY` as well:

```bash
npx -y @sandbaseai/cli@latest inspect google/gemini-4-argon   # input fields and price, free
jq -n --rawfile prompt prompt.txt '{max_tokens: 65536, messages: [{role: "user", content: $prompt}]}' > input.json
npx -y @sandbaseai/cli@latest run sandbase_google_gemini_4_argon -f input.json --timeout 900 -o result.json
```

`-o result.json` saves the response; the page is in the assistant message, as with the API.

## 4. Turn the page into a video

Most creators screen-record the page — the comparison posts here record two pages side by side at the same length. To get the same clip every time, record it headlessly with [`scripts/record.mjs`](../scripts/record.mjs):

```bash
npm i -D playwright@1.56.1
npx playwright install chromium          # or use your installed Chrome: export RECORD_CHANNEL=chrome
node scripts/record.mjs gemini-carbon.html gemini-carbon.mp4 12 1920 1080   # 12 seconds at 1080p
```

It opens the page at the size you give, records for that many seconds, and converts to H.264 MP4 with ffmpeg. For a clean result, ask in the prompt for an autoplay sequence or a fixed-length loop (see [prompt guide §4](prompt-guide.md#4-describe-what-the-camera-should-catch)), so nothing depends on a mouse.

Want sound? The recording is picture only, so add audio in the edit — or ask the page for Web Audio sound and capture the tab audio, not the microphone.

Many videos in this list came out of an Arena session rather than a single API call, and at least one creator iterated: three follow-up turns took a castle scene from "fire is 9 orange cubes" to "fire you can almost feel" ([@semichenkko][dragon]).

## Run generated code safely

The HTML is code you haven't read. Opening it from disk is usually fine for a single-file page, but it can still load scripts and make network requests. For anything you don't trust, or to run many pages automatically, use a [SandBase Sandbox][sandbox]: an isolated environment with a time limit and no access to your files or keys.

## Share it

Post your video on X with the prompt and mention Gemini 4 Carbon. To have it added here, [submit it](https://github.com/sandbase-lab/awesome-gemini-4-carbon/issues/new?template=submit-video.yml); accepted posts go into the Lab collection and show up in this list on the next daily sync.

[lab]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[arena]: https://www.sandbase.ai/lab/x/llm-arena?models=google%2Fgemini-4-argon&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[keys]: https://www.sandbase.ai/console/keys?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[model]: https://www.sandbase.ai/model/google/gemini-4-argon?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[sandbox]: https://www.sandbase.ai/landing/sandbox?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[shark]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116548548334321967?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[dragon]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116198626187706722?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
