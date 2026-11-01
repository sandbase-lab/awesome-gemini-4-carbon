# Gemini 4 Carbon prompt guide: how to prompt Carbon for video

English · [简体中文](zh-CN/prompt-guide.md) · [← Back to the collection](../README.md)

Gemini 4 Carbon doesn't output video. It writes code — usually a single HTML page with Three.js, Canvas or SVG — and the creator records that page playing. Most posts in this collection are Arena runs: one prompt, one shot per model, both pages recorded side by side. The patterns below come from prompts creators posted with their videos. Each example links to the video it produced.

One thing that shapes every prompt: thinking is always on for this model, and the hidden reasoning tokens come out of your `max_tokens`. There is no `reasoning_effort` parameter on the API — the model picks its effort itself ([`sandbase inspect`](https://www.sandbase.ai/model/google/gemini-4-argon?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon)). On SandBase the Carbon checkpoint is served under the `google/gemini-4-argon` id.

## 1. Name one file and the renderer

Say what the deliverable is and what draws it, in the first line. The strongest pieces here all do it:

- "A freestyle swimmer doing the front crawl using Three.js (single HTML file)" ([@AI_Screening][swimmer]) — the renderer and the file count in one parenthesis.
- "build 3d cycle riding cow using three.js" ([@TimJayas][cow]) — eleven words, one shot, and the result held up against Grok 4.7 in the follow-up post.
- "build an interactive 3D webpage where you can pour beer into a glass" ([@HIX_AI_][beer]) — the interaction is named with the file.
- Even shorter works when the format is the spec: "640x360 pixel art of cheetah running (thats the whole prompt)" ([@duke_mv][cheetah]).

## 2. Ask for an exploded view or a cutaway

Carbon's signature pieces in this collection are objects you can take apart. Creators keep using the same verbs — X-ray, cut in half, explode, lay out — because the model treats them as a scene state, not a filter:

- "a café racer you can X-ray, cut in half, explode and lay out part by part" ([@dromexa][bike]) — one shot per model; the creator's verdict was that Carbon's bike "looks like it came out of a real workshop".
- "a mechanical watch you can X-ray, cut in half, explode and lay out part by part", round two of the same prompt ([@dromexa][watch]) — "the balance wheel actually ticks and every gear turns at the right speed".
- "a robotic eye that blinks, focuses, then explodes into every part" ([@noclipepe][eye]) — a 30-minute single run.
- "a robotic great white I can take apart piece by piece" ([@0xPorterio][shark]) — the comparison Opus won on internals, so see §6 on when to push back.
- "an animated cutaway of an airplane engine" — a 9-cylinder radial where "all four got the mechanics right (pistons fire in the correct order)" ([@olezhavich][engine]).
- "a cartoon liner that sails, splits open and shows life on every deck" ([@olezhavich][ship]) — the cut is part of the animation, not a mode.

The pattern works because it gives the model three scenes in one: the intact object, the separation, and the labeled parts. Say all three and what should still be running during the explode (the ticking wheel, the firing pistons).

## 3. Write the cast, the props and the finale

The most-watched posts here read like a stage direction: N characters, M working props, and one scripted ending. The numbers are the test — every model gets the same count to fail on:

- "9 capybaras in a hot spring, 6 tools that all have to work, and a finale where a baby capybara floats up in a bubble and plops back into the water" ([@ottollm][onsen]) — "Opus read the brief. Carbon built the onsen."
- "9 tiny troublemakers, a dock full of tools, and one of them has to pop at the end" ([@0xPorterio][troublemakers]).
- "a zombie hand claws out of a grave and rots down to the bone" ([@noclipepe][zombie]) — the finale is a second state the page has to reach on its own.
- "rainbow jelly you can cut, nail and torch" ([@0xRhinoX][jelly]) and the follow-up "a rainbow jelly pumpkin you can carve and light up" ([@0xRhinoX][pumpkin]) — verbs that each need a different piece of physics.

A cast list also makes the comparison readable: when Carbon spread nine capybaras across the spring and Opus piled them into "one furry traffic jam", the count is what made the difference visible.

## 4. Describe what the camera should catch

These posts are videos, so the prompt has to produce a page that performs on its own — no mouse, no second take:

- An autoplay sequence or a loop of fixed length, so a screen recording catches everything. "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out" ([@leo114119][showreel]) puts the runtime in the prompt; "Create a professional motion graphics 30 seconds" ([@Genysis_Ai_26][thirty]) does the same.
- A transformation with a timeline: blinking then exploding ([eye][eye]), sailing then splitting ([ship][ship]), clawing then rotting ([zombie][zombie]).
- Detail that survives a phone screen: the cruise ship post notes Carbon "reads perfectly on a phone" ([@olezhavich][ship]), and the peacock run was judged on "animation" vs "real" at feed size ([@srikanthvaluri][peacock]). Previews here are 400 px wide — thin lines and small labels vanish.
- Continuous motion for SVG: "behold superman in continuous animation in different art style" ([@Inmerson][superman]), and the bicycle-riding-cow SVG where "everything is perfectly synced in one motion" ([@TimJayas][svg]).

## 5. One shot means one shot — say so

This collection exists because creators ran the same words through two or more models with no repairs. The post says it explicitly because it is part of the claim:

- "same prompt, one shot each" ([@dromexa][bike], [@Haleeeemahh][oneshot]).
- "same prompt, one shot, no testing, no second tries" ([@ottollm][onsen]).
- "same prompt, both low effort" ([@ValencianaAbel][trex]).
- "same prompt, 4 models" ([@srikanthvaluri][peacock]); "I gave four models a 9-cylinder radial engine… one try each" ([@olezhavich][engine]).

If you want a fair head-to-head, fix everything but the model: same prompt, same effort setting, one run each, then record both pages the same way. If you want the best page instead of a fair test, iterate — one creator showed the same castle scene go from "fire is 9 orange cubes" to "fire you can almost feel" in three follow-ups ([@semichenkko][dragon]): "the gap isn't the model. it's the follow-ups."

## 6. Set the budget and check the inside

Carbon prices like a flagship — $4/M input, $20/M output on SandBase — and these pages run long. Reported Arena runs in this collection cost $3.20 to $14 and took 24 to 85 minutes each. Plan for it:

- `max_tokens` is the whole budget: reasoning is always on and shares it, and the API caps output at 65,536 tokens. A truncated page still bills the tokens. Give the full cap for one-shot pages.
- Long single files are normal here — the shark comparison notes Opus wrote "1,634 parts, every one written in code" in the same 29-second window ([@0xPorterio][shark]).
- The lesson from that shark post: Carbon "won speed and FX" while Opus "won everything you can actually see inside" — 77 to 90. If the brief is mechanical depth, say what has to be inside (parts count, joints, labeled systems), not just that it explodes.
- For the record.mjs route, ask the page to fill the viewport and run without input (§4), then follow the [tutorial](tutorial.md#4-turn-the-page-into-a-video).

## A prompt to start from

```text
Build [subject] as ONE self-contained HTML file that opens directly from disk.

Scene: [the cast — N characters/objects, what each does], [setting, lighting, mood].
Interaction: [the verbs: orbit, X-ray, cut, explode, feed, carve…] — every control must work.
Finale: [the state the page reaches on its own: the pop, the split, the rot].
Motion: autoplay a [10–30]-second sequence on load, then loop. No input needed.

Technical:
- Use Three.js as an ES module from a CDN import map. No other libraries.
- No external images, fonts or audio: generate textures in code.
- Fill the viewport, no scrolling, 60 fps on a laptop, readable at 400 px wide.
- Before you finish, check that the page loads with zero console errors and that every control works.
- Return only the complete HTML, from <!DOCTYPE html> to </html>. Do not abbreviate.
```

Try it on the [Lab text arena][arena] to run it on Carbon and other models side by side, or with the API in the [tutorial](tutorial.md).

## Settings

- **Output budget.** Thinking is always on and shares `max_tokens`, capped at 65,536 by the API. One-shot pages in this collection ran 24–85 minutes in the Arena; set `max_tokens` to the full 65,536 so the page is not cut off mid-file.
- **No reasoning_effort.** The API has no effort knob — `sandbase inspect google/gemini-4-argon` lists only `max_tokens`, `temperature`, `top_p`, `stop`, `seed` and the tool/response fields. Effort is the model's own choice (its description says low, medium or high). If a comparison post says "low effort", that was an Arena-side setting, not something you can pass here.
- **Cost.** $4 per million input tokens, $20 per million output tokens, cached input at 0.05x; reasoning bills as output. See what creators actually paid in the [comparison](model-comparison.md).

---

Quotes are short excerpts credited to their authors; follow the links for full prompts and videos. Translations are ours.

[swimmer]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2113144877257248816?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[cow]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2112950910892789979?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[beer]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115699353675354307?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[cheetah]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2113018068981182659?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[bike]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115802517942497491?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[watch]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116518366919667775?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[eye]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115556254101692515?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[shark]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116548548334321967?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[engine]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116606788241969445?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[ship]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116527640479662179?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[onsen]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116577106238873765?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[troublemakers]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116108534051905642?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[zombie]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116445289468850366?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[jelly]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115891194383200515?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[pumpkin]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116301725951013180?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[showreel]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115823149849714738?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[thirty]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2112909613788230013?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[superman]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115721948886155726?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[svg]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115512016811307487?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[peacock]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2114748807464546689?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[oneshot]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2113243268569870459?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[trex]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115918611676041698?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[dragon]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116198626187706722?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[arena]: https://www.sandbase.ai/lab/x/llm-arena?models=google%2Fgemini-4-argon&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
