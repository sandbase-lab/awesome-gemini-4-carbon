# Gemini 4 Carbon vs Claude Opus 5.5, GPT-6 Astra and Gemini 4 Argon

English · [简体中文](zh-CN/model-comparison.md) · [← Back to the collection](../README.md)

Two kinds of evidence, kept apart:

1. **What we measured.** The Lab [Evals boards][evals] show Artificial Analysis data, and the Lab [Pelican Test][pelican] runs the same fixed prompt on every model and scores the result. Small samples, but the same conditions for everyone.
2. **What creators reported.** Head-to-heads posted on X with their own prompts, costs and times. Useful context, not verified by us.

One naming note that runs through both sides: Carbon is the newest Gemini 4 checkpoint, first seen in the Arena under the codename "Gemini 4 Argon". Artificial Analysis lists the two checkpoints as separate models, and several creators in this collection ran Carbon against Argon itself. On SandBase the Carbon checkpoint is served under the same id — `google/gemini-4-argon` — so the Lab Pelican Test row for that id is the measured row for this list.

## What we measured: Lab Evals boards

The boards read the Artificial Analysis snapshot of **2026-10-29** (Intelligence Index v5, 716 models). Rows here are per effort setting; the LLM boards cover three metrics — there is no coding or agentic board in this snapshot.

| Model (row on the board) | [Intelligence Index][b-intel] | [Output speed][b-speed] | [Cost per task][b-cost] |
|---|---|---|---|
| **Gemini 4 Carbon (High)** | **59.4 (#1)** | **102 tok/s (#172 of 373)** | **$7.76 (#67 of 73)** |
| Claude Opus 5.5 (Max) | 58.4 (#2) | 98 tok/s (#182) | $10.04 (#71) |
| GPT-6 Astra (Max) | 56.9 (#4) | 76 tok/s (#245) | $6.24 (#61) |
| GPT-6.1 Sol (Max) | 54.5 (#7) | 81 tok/s (#231) | $1.27 (#34) |
| Gemini 4 Argon (High) | 50.4 (#13) | 82 tok/s (#228) | $7.68 (#66) |
| Kimi K3.1 Pro | 46.0 (#22) | 37 tok/s (#353) | $3.68 (#53) |
| Claude Haiku 5.5 (Max) | 36.2 (#32) | 241 tok/s (#21) | $0.41 (#23) |
| DeepSeek V4.1 Flash 1017 (Max) | 32.5 (#39) | 182 tok/s (#57) | $0.60 (#28) |

What this says, and what it doesn't:

- **Carbon tops the headline board.** 59.4 puts it a point ahead of Opus 5.5 Max and nine ahead of its own previous checkpoint (Argon, 50.4). This is the only measured evidence in this list that matches the creators' "new king" framing — and it is one benchmark suite at one effort setting, not a verdict on every task.
- **It is a flagship on price and speed too.** $7.76 a task puts Carbon next to Argon ($7.68) and Opus 5.5 Max ($10.04) at the expensive end of the board — flash-tier rivals run 10–20x cheaper per task (DeepSeek V4.1 Flash 1017 at $0.60, Haiku 5.5 at $0.41). At 102 tok/s it sits mid-pack for speed, faster than Argon (82) and Astra (76), far behind the flash models (Haiku 241, DeepSeek 182).
- **The board measures reasoning, not rendering.** Nothing here grades a Three.js scene or an SVG. The visual claims below are all creator-reported.

## What we measured: Lab Pelican Test

The [Pelican Test][pelican] asks each model for an SVG of a pelican riding a bicycle, once static and once animated (wheels spin, legs pedal, CSS/SMIL only). The page is rendered to PNG and scored 0 to 5 by an LLM judge on four questions: recognizable, actually riding, a bike that works, looks good. Cost is the real billed amount on SandBase.

Leaderboard rows from the [live leaderboard][pelican] on 2026-11-01 (22 models):

| Rank | Model | Results | Score | Renders | Animation moves | Avg cost |
|---|---|---|---|---|---|---|
| 1 | **google/gemini-4-argon** | **4** | **3.81** | **100%** | **100%** | **$0.120** |
| 2 | openai/gpt-6.1-sol | 6 | 3.79 | 100% | 100% | $0.027 |
| 3 | google/gemini-3.7-flash | 6 | 3.63 | 100% | 100% | $0.087 |
| 4 | anthropic/claude-opus-5.5 | 6 | 3.46 | 100% | 100% | $0.199 |
| 5 | deepseek/deepseek-v4.1-flash | 8 | 3.44 | 100% | 100% | $0.017 |
| 6 | anthropic/claude-haiku-5.5 | 2 | 3.25 | 100% | 100% | $0.008 |
| 6 | anthropic/claude-sonnet-5.5 | 4 | 3.25 | 100% | 100% | $0.045 |
| 6 | minimax/minimax-m3.1-flash | 4 | 3.25 | 100% | 100% | $0.006 |
| 6 | openai/gpt-6-luna | 2 | 3.25 | 100% | 100% | $0.006 |
| 10 | moonshotai/kimi-k3 | 6 | 3.21 | — | — | $0.089 |
| 11 | openai/gpt-6-astra | 6 | 3.08 | — | — | $0.102 |

What this says:

- **The Argon id holds the top row — 3.81, the current SOTA.** That id is where the Carbon checkpoint is served on SandBase, but the four scored results behind it were logged between October 14 and 20, before Artificial Analysis added the Carbon checkpoint on October 28. Treat 3.81 as "the Gemini 4 flagship's pelican", not as a Carbon-only score.
- **Four drawings, two testers.** A small sample; [run it yourself][pelican-run] to add more.
- **Price fits the flagship story.** At ~$0.12 a drawing it costs about 7x DeepSeek's pelican and 20x Haiku's, roughly 60% of Opus 5.5's.

## What creators reported

Same-prompt comparisons posted on X. Most of this collection is comparisons — 39 of 98 posts — and the rival is usually Claude Opus 5.5, with GPT-6 Astra, Gemini 4 Argon, Grok and Fable making up the rest. Numbers are as the creator stated them, from Arena or Antigravity runs, often one shot. Click through to watch both results.

| Creator | Task | Carbon | Rival | Creator's verdict |
|---|---|---|---|---|
| [@0xRhinoX][jelly] | Rainbow jelly you can cut, nail and torch | $4.30, 32 min | Opus 5.5: $14.00, 1h 20m | "3x cheaper. 2x faster. 1 day old." — Carbon's jelly throws rainbow shadows; Opus "washed out" |
| [@0xRhinoX][pumpkin] | Rainbow jelly pumpkin you can carve and light | $3.20, 31 min | Opus 5.5: $28.73, 1h 50m | "9x cheaper. 3x faster." |
| [@0xPorterio][troublemakers] | 9 tiny troublemakers, tools, one pops at the end | $4.10, 34 min | Opus 5.5: $12.80, 1h 12m | "Carbon looks SERIOUSLY good… Opus feels more alive" |
| [@noclipepe][zombie] | Zombie hand claws out, rots to bone | 1h 23m, $10.20 | Opus 5.5: 1h 6m, $8.10 · GPT-6 Astra: 24m, $5.70 | "Carbon went full horror movie… Astra built a landing page with a hand on it" |
| [@noclipepe][dino] | Chrome Dino game | 34m 41s, $5.20 | Opus 5.5: 38m 55s, $8.53 · Astra: 15m, $4.61 · GPT-6.1 Terra: 4m, $0.17 | "Carbon even animated the pterodactyls' flight" |
| [@noclipepe][eye-test] | Robotic eye: blink, focus, explode | 29m 49s | Opus 5.5: 43m 21s, $9.25 · Astra: 22m 54s, $3.28 | "Gemini just made other models look old" |
| [@dromexa][bike] | Café racer you can X-ray, cut, explode | one shot each | Opus 5.5 | "Carbon's bike looks like it came out of a real workshop… for 3D, Carbon just took the crown" |
| [@dromexa][watch] | Same prompt, mechanical watch | one shot each | Opus 5.5 | "the balance wheel actually ticks… 2 for 2. Carbon is the 3D king right now" |
| [@0xPorterio][shark] | Robotic great white, take apart piece by piece | "fastest build… flashiest FX" | Opus 5.5: 1,634 coded parts, ball-jointed spine, pumping rams | "Gemini won speed and FX. Opus won everything you can actually see inside. Final score: 77 vs 90" — for Opus |
| [@olezhavich][engine] | 9-cylinder radial engine cutaway, 4 models | "crisp, clean… the most polished" | Opus 5.5: intake pipes, exhaust stacks, "gets my engineering award" · Argon: most atmospheric, less crisp · Sol: clean but dim | split — polish vs engineering |
| [@olezhavich][ship] | Cartoon cruise ship cutaway, 3 models | "every room has its own colour… reads perfectly on a phone" | Fable 5.1: fuel tanks, engine control, anchor chain — "the most 'real' ship" · Astra: pale, flattest | "I'd study Fable and board Carbon" |
| [@ottollm][onsen] | 9 capybaras, 6 working tools, bubble finale | all nine spread out, each doing its own thing | Opus 5.5: "one furry traffic jam in the middle" | "Opus read the brief. Carbon built the onsen." — the strongest pro-Carbon post here |
| [@TimJayas][cow-vs] | 3D bicycle riding a cow in Three.js | — | Grok 4.7: "cow looks like it came straight from mars" | for Carbon |
| [@TimJayas][cow] | Same scene, solo | "pretty amazing in terms of 3d outputs" | (asks: is this Opus 5.5 level?) | — |
| [@srikanthvaluri][peacock] | Mechanical Indian peacock, 4 models | "most real" | Opus 5.5: best animation · Astra: clean but pale · Sol: less detail | "Carbon wins for me" |
| [@ValencianaAbel][trex] | Running T-rex in Three.js, both low effort | "looks built" | Opus 5.5: "looks like a toy" | for Carbon |
| [@keydol123][haunted] | "Build a haunted house website" | "actually haunted" | Opus 5.5: "made it cute" | asks viewers which |
| [@leo114119][showreel] | 15-second motion-graphics showreel | better effect (translated) | Opus 5.5 | "real surpass, where Opus had the advantage" |
| [@leo114119][oxford] | Interactive 3D Oxford city in Three.js | clearly more detail per building, better sunlight | Fable 5.1 High | for Carbon (translated) |
| [@olezhavich][football] | Isometric street football court, 3 models | "the most alive scene… best atmosphere" | Kimi K3.1: structural cutaway, less polished · Grok 4.6: cleanest but emptiest | "My pick here: Gemini 4 Carbon" |
| [@Haleeeemahh][oneshot] | Same prompt, both one-shot | — | Opus 5.5 (High) | "WTF did Google just release an opus 5.5 level model?" |
| [@marcthecreatorr][ps5] | SVG of a PS5 controller; Opus on xhigh in Claude Code | "older Carbon checkpoint" output | Opus 5.5 | "a tough one to decide" — notes Opus has been hard to beat on SVG |
| [@blueemi99][opus-win] | Same prompt on Arena "Gemini 4 (might be carbon)" vs Opus 5.5 | — | Opus 5.5 | "It's not looking good for Gemini, Opus looks 100x better here" — the strongest anti-Carbon post |

Against its own previous checkpoint, creators are mostly but not unanimously for Carbon:

- [@leo114119][pelican-svg] ran the pelican-bicycle SVG on both, one shot: "Carbon is a level above Argon on every detail; Argon is livelier on colour and interaction" (translated).
- [@abhinavflac][voxel] on voxelbench: "the most impressive output I've seen with this prompt… it takes 2–3x longer than Argon, totally justified by the leap in visual quality".
- [@Adidotdev][macro] ran both one-shot: Carbon ~4 min in the Arena vs Argon ~10 min in Antigravity — "Carbon added a lot of macro interaction under 4 mins".
- [@Inmerson][superman] split-screened a Superman multiverse animation, Carbon left, Argon right.
- [@glitch_catAI][argon-win] dissents: "Same prompt but argon >>> carbon".
- [@pankajkumar_dev][temple] built a voxel Japanese temple valley: "significantly better than Gemini 4 Argon… a clear step up".
- [@pankajkumar_dev][lantern] on a lantern river night scene: "Carbon-H is comparable to Opus 5.5 in terms of design quality".

Solo runs and quality notes without a rival:

- [@duke_mv][cheetah-solo] on the 640×360 pixel cheetah: "the best output I've got with this prompt compared to all the frontier models till now".
- [@DrstaOne][motorbike] on a motorbike riding a pelican SVG: "Gemini 4 Carbon cooked at SVG".
- [@Genysis_Ai_26][thirty] on the 30-second showreel: "crazy good… can dethrone Opus 5.5 considering it's just first checkpoint".
- [@semichenkko][dragon] iterated one castle scene four turns: fire went from "9 orange cubes" to "fire you can almost feel" — "the gap isn't the model. it's the follow-ups."

The pattern across both sources: the measured boards and most creators agree Carbon is a front-runner — #1 on the Intelligence Index, #1 on the Pelican row under its serving id, and the crowd favourite on 3D scenes with depth and detail. The disagreements are consistent too: Opus keeps winning on internal engineering (the shark's coded parts, the engine's plumbing) and on animation feel, Carbon costs flagship prices and flagship minutes per page, and a minority of posts simply prefer Argon or Opus on the same prompt. The Arena's checkpoint routing was also unstable during launch week — [@marcthecreatorr][ps5] notes his Carbon output was an older checkpoint, and [@blueemi99][opus-win] wasn't sure which Gemini ran.

## Rerun before you trust a comparison

Results move a lot with the setup: Arena vs Antigravity vs API, which checkpoint the Arena actually served that day, effort setting, and whether the creator repaired the output. Several posts here hedge on exactly that ([@marcthecreatorr][ps5], [@olezhavich][football], [@blueemi99][opus-win]). Run the prompt yourself: paste it into the [Lab text arena][arena] with two or three models selected, or see the [tutorial](tutorial.md).

## More measurements

- [Lab Evals boards][evals] — Artificial Analysis data, snapshot 2026-10-29.
- [Lab Pelican Test][pelican] — same prompt on every model, scored the same way, with the drawings on screen.
- [All AI video collections on SandBase Lab][collections] — the same list for other models.

---

Lab data: [Evals boards][evals] (Artificial Analysis, snapshot 2026-10-29) and [Pelican Test][pelican] (read 2026-11-01). Creator data: their posts, linked; not independently verified.

[evals]: https://www.sandbase.ai/lab/evals?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[b-intel]: https://www.sandbase.ai/lab/evals/llm-intelligence?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[b-speed]: https://www.sandbase.ai/lab/evals/llm-speed?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[b-cost]: https://www.sandbase.ai/lab/evals/llm-cost?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[pelican]: https://www.sandbase.ai/lab/pelican-test?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[pelican-run]: https://www.sandbase.ai/lab/pelican-test?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=run
[arena]: https://www.sandbase.ai/lab/x/llm-arena?models=google%2Fgemini-4-argon&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[collections]: https://www.sandbase.ai/lab/ai-videos?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[jelly]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115891194383200515?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[pumpkin]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116301725951013180?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[troublemakers]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116108534051905642?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[zombie]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116445289468850366?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[dino]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115953941808550313?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[eye-test]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115728069398757827?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[bike]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115802517942497491?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[watch]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116518366919667775?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[shark]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116548548334321967?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[engine]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116606788241969445?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[ship]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116527640479662179?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[onsen]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116577106238873765?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[cow-vs]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2113358260933988655?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[cow]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2112950910892789979?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[peacock]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2114748807464546689?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[trex]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115918611676041698?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[haunted]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116556350130163783?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[showreel]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115823149849714738?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[oxford]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115839073701257422?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[football]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2113289049075003839?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[oneshot]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2113243268569870459?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[ps5]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116148349791346698?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[opus-win]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2113371478817399010?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[pelican-svg]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115577725373092274?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[voxel]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2112910206644756745?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[macro]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2113678010754961806?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[superman]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115721948886155726?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[argon-win]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115840921342456062?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[temple]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2113308975437598966?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[lantern]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116533017934241886?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[cheetah-solo]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2113018068981182659?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[motorbike]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2113373228630704237?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[thirty]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2112909613788230013?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[dragon]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116198626187706722?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
