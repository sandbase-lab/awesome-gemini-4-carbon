# Gemini 4 Carbon prompts

English · [简体中文](zh-CN/prompts.md) · [← Back to the collection](../README.md)

57 Gemini 4 Carbon videos whose creators shared the prompt. Open one to read the prompt, watch the video and **Recreate** it with Carbon on SandBase Lab. New to prompting Carbon? Start with the [prompt guide](prompt-guide.md).

Each entry quotes the creator's post as published on X, where the prompt is shared. Some creators describe the task rather than pasting the whole prompt, and some put the full text in a reply: open the post on X to read the thread. Posts keep the creator's language.

- [3D scenes](#3d-scene) (5)
- [Motion graphics](#motion-graphics) (9)
- [Games](#game) (1)
- [Product UI](#ui-demo) (1)
- [Particles & shapes](#particles) (1)
- [Anime](#anime) (1)
- [Tests & comparisons](#comparison) (35)
- [Model showcases](#showcase) (4)

<a id="3d-scene"></a>

## 3D scenes

### Robotic eye blinking and exploding into parts

[@noclipepe](https://x.com/noclipepe/status/2115556254101692515) · 0:31 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2115556254101692515/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115556254101692515?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
GOOGLE'S NEW GEMINI 4 CARBON IS SCARY GOOD AT 3D 🥶

One prompt: a robotic eye that blinks, focuses, then explodes into every part.

Gemini 4 Carbon → 29m 49s

Waiting for it on
```

### Lantern river night 3D scene

[@pankajkumar_dev](https://x.com/pankajkumar_dev/status/2116533017934241886) · 0:48 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2116533017934241886/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116533017934241886?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon-H output looks seriously good.

I asked it to build Lantern River Night, an 3D scene with glowing lanterns, water reflections, and a cinematic nighttime atmosphere.

Just look at the aesthetics, the sky colors, the lanterns, the lighting, everything looks so good, man.

I can easily say Carbon-H is comparable to Opus 5.5 in terms of design quality.

Damn, Google really cooked this time.
```

### Three.js scene generated with Gemini 4 Carbon

[@SimonasLTU1](https://x.com/SimonasLTU1/status/2120192174239146417) · 0:35 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2120192174239146417/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2120192174239146417?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Full prompt in the comments. Gemini 4 Carbon - 13 minutes :) Quite nice results with Three.js so far!
```

### Giant mech stomping through New York City

[@simonw](https://x.com/simonw/status/2120258951594037732) · 1:00 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2120258951594037732/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2120258951594037732?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon is good at pelican SVGs, but that's nothing new for Gemini

"Make a three js animation where yonkers stands up as a big mech (cool stand up motion) and stomps around manhattan and queens and Brooklyn, use openstreetmap mapping data"
https://t.co/7hssgBoCMY
```

### Solo violin concert film in moonlit salon

[@IamEmily2050](https://x.com/IamEmily2050/status/2120605361615073681) · 3:00 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2120605361615073681/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2120605361615073681?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon High /Antigravity 

Build a deterministic, seamless-looping 3-minute (180.000 s, 10,800 frames at 1920x1080, 60 fps) solo-violin concert film titled "NOCTURNE IN D MINOR // SOLO VIOLIN" set in a moonlit Parisian Haussmannian salon, using headless Blender (5.2 LTS+ with Cycles GPU baking) for 3D character, cloth, soft-body, luthiery, and architectural assets, Three.js (latest release, WebGL2) + Vite for real-time rendering, Node.js DSP for 24-bit/48 kHz acoustic audio, and Playwright + FFmpeg for parallel 1080p60 master encoding.

1. Seamless Stateless Determinism & Live/Master Parity
- Maintain 1:1 parity between the live 60 fps interactive browser preview (`npm run dev`) and the offline 1080p60 MP4 render.
- Every visual channel, skeletal pose, physics state, particle position, and stereo audio sample must close analytically across the frame 10799 -> frame 0 loop boundary (`|state(0) - state(10800)| < 1e-6`, `< 0.05 mm` scene-graph delta) without a cross-dissolve.
- Expose `O(1)` stateless frame seeking (`__renderFrame(frameIndex)`, `seek(t)`) with zero reliance on prior frame history: rewinding from mid-film to an earlier frame must produce the exact same RGBA pixel hash. Pre-integrate all periodic, forced, damped second-order ODEs across the full 10,800-frame ring at boot, rather than using stateful frame stepping or gate-windowed lookup tables.

2. Musical Score & Click-Free Single-Voice Acoustic Violin Audio
- Compose a 180.000 s solo violin score in D minor across G3, D4, A4, and E5: open with an intimate Nocturne Prelude (sul G and sul D cantilena, slurs, subtle portamento, and periodic human rubato), develop into J.S. Bach's Chaconne in D minor (BWV 1004) with rolled 3- and 4-string chords, high-position cantabile (1st to 7th position), and G-D-A-E bariolage arpeggios, and resolve into a quiet senza-vibrato natural-harmonics (flageolet) coda that loops seamlessly back into frame 0.
- Synthesise `output/perf02_audio.wav` (48 kHz, 24-bit stereo PCM, ~ -18.7 LUFS integrated, <= -1.5 dBTP true peak) strictly from real CC0 studio-recorded solo violin multi-samples (`VSCO-2-CE`), never procedural sawtooth or sine-wave synthesis.
- Calibrate sample pitch with YIN autocorrelation and render through a strict single-voice dual-head equal-power crossfader (18-45 ms legato slurs, 8 ms bow-change fades, dual-head loop crossfades on long sustains) so two recordings never overlap into chorus beating and mid-note loop boundaries never click. Use real bowed upper-register acoustic harmonic recordings in the coda (zero synthetic sine partials or pseudorandom breath hiss).
- Couple the acoustic RMS envelope and 2.5-4.5 kHz bridge-hill spectral tilt directly to the 3D bow's instantaneous contact force, bow velocity, and sounding-point distance ahead of the bridge (`r >= 0.70`), then convolve circularly across the 180 s loop seam with a real stereo chamber salon impulse response.

3. Anatomical Soloist, 10-Digit Contact IK, Soft-Tissue Compliance & Gravity Couture (Blender + Three.js)
- Build the female soloist GLB in headless Blender from CC0 MakeHuman 2-manifold quad anatomy (never procedural lathe/metaball body parts) bound to a continuous `SkinnedMesh` skeleton (`0.000 mm` neck and wrist seam gaps), with 2K/4K PBR dermal maps, Cycles-baked 4K dermal AO/SSS and hair-flow maps (`flipY = false` on glTF UVs), wrapped RGB dermal subsurface scattering, two-shell refractive cornea + iris eyeballs with wet lower-lid tear meniscus, 3D eyebrows and eyelashes, and 10 curved translucent keratin fingernails recessed into refined distal phalanx nail beds.
- Groom a low recital chignon and smooth `SUBSURF` cranial scalp cap with multi-pass soft feathered hairline strand cards (avoid hard `alphaTest` pixel stair-stepping and grazing cranial rim blowouts). Run a headless Blender `SOFT_BODY` simulation pass on the chignon (`ChignonPin` goal falloff) plus temple-wisp sway shape keys, driven at runtime by head angular acceleration (~50 ms …
```

<a id="motion-graphics"></a>

## Motion graphics

### SVG animation of a bicycle riding a cow

[@TimJayas](https://x.com/TimJayas/status/2115512016811307487) · 0:29 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2115512016811307487/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115512016811307487?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon

SVG of a bicycle riding a cow

look at all the attention to details. from cows eye to bicycle’s peddle everything is perfectly synced in one motion
```

### Dynamic motion graphics showreel

[@aeroidesde](https://x.com/aeroidesde/status/2115755454660059626) · 0:15 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2115755454660059626/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115755454660059626?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Prompt: make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it’s your showreel for a résumé. go all out

By Gemini 4 Carbon EAP
```

### A dynamic motion design showreel in SVG

[@leo114119](https://x.com/leo114119/status/2117142662100754825) · 0:15 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2117142662100754825/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2117142662100754825?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon-H 最新的版本测试：

生成一条 15 秒的 motion showreel，百分百 SVG 生成

prompt: make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it’s your showreel for a résumé. go all out

感觉Carbon还在优化中，看看这一周会不会发布给 Pro用户使用吧。。。
```

### Miles Morales vs Green Goblin

[@TimJayas](https://x.com/TimJayas/status/2117646891051889052) · 0:21 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2117646891051889052/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2117646891051889052?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
gemini 4 argon

> miles morales vs green goblin

can't wait to try this same prompt with gemini 4 carbon
```

### Animated SVG of game controller riding a pelican bicycle

[@SongyuKite](https://x.com/SongyuKite/status/2119729206888145162) · 0:07 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2119729206888145162/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2119729206888145162?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini Carbon 还没摸到，又出Gemini Krypton了！

虽然无法使用Gemini 最新的模型 但是GPT 6.2 来了 

GPT-6.2 鹈鹕动画 （GPT6.1 路由过去的）

提示词：

做一个SVG 动画

游戏控制器骑着自行车，骑着鹈鹕，骑着自行车下面有只
鹈鹕。
```

### Pelican riding a bicycle SVG benchmark test

[@RJasonHA](https://x.com/RJasonHA/status/2120143436481265960) · 0:46 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2120143436481265960/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2120143436481265960?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
🚨 Gemini 4 Carbon 疑似提前偷跑！中文区首个鹈鹕单车测评来啦！！🔥

跑 Simon Willison 的经典题：Generate an SVG of a pelican riding a bicycle

成本：静态版每张约 7.6k–9.4k token，耗时 2 分钟左右，按标价每张 $0.15–0.19。整轮 5 次调用一共 $1.07。

不足：3 张构图几乎一样，风格多样性一般。
```

### SVG animation of crabs approaching cycling pelican

[@HarshithLucky3](https://x.com/HarshithLucky3/status/2120236571165368720) · 0:28 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2120236571165368720/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2120236571165368720?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 carbon medium in AI Studio

SVG of "two aggressive crabs approaching pelican riding a bicycle"
```

### Music video for Toxic Perfume

[@diebbCN](https://x.com/diebbCN/status/2120368913087119450) · 0:32 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2120368913087119450/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2120368913087119450?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
这是用 Claude Desktop 加 Gemini 4 Argon 做的 MV，效果已经和 Opus 5.5 差不多了。今天出了 Gemini 4 Carbon，晚点再试试。 

提示词：参考 JohnHeibel/ClaudeAnimationBase 的制作方式和视觉风格，为《香水有毒》这首歌做一支 MV。
```

### Piano sonata movement in Beethoven style

[@aug5thmusic](https://x.com/aug5thmusic/status/2120586376089674180) · 4:19 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2120586376089674180/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2120586376089674180?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon - Piano sonata movement in the style of Beethoven. This is an impressive effort, especially considering how much LLMs have traditionally struggled on the Classical style. I was skeptical at first, but I think Carbon might be on the same level as Astra and Opus when it comes to music.
Prompt: “In LilyPond, write the opening movement of a piano sonata (in sonata-allegro form) in the style of Beethoven. Return only the code block.”
```

<a id="game"></a>

## Games

### A Flappy Bird style platformer game

[@SimonasLTU1](https://x.com/SimonasLTU1/status/2120186826451288182) · 0:40 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2120186826451288182/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2120186826451288182?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon. Yes, I'm this professional and serious. Prompt: "Create a game called pooperman, basically it's a flappy bird, but with a guy that poops on clicks, should be three.js graphics, but platformer style." It took 14 minutes to create this game.
```

<a id="ui-demo"></a>

## Product UI

### Overview demo reel of fourteen vertical apps

[@giyu_codes](https://x.com/giyu_codes/status/2120201582319190381) · 1:25 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2120201582319190381/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2120201582319190381?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
I got early access from Google to test Gemini 4 Carbon and it surpassed all expectations. 

Using my existing public-data apps as architectural guidance, I asked Carbon to find high value underserved industries with publicly available data so we can build full vertical platforms. The goal was to test it's limits on messy multi-source data reconcilation + 3d WebGL physics and I am genuinely impressed with how it handled data reconciliation and delivery on actionable feedback. 

Here is the overview demo reel for all 14 apps, as well as a post for each app with a longer reel for them individually.

Each app was built into a hosted application successfully. Prompts used to build are given below, but it could be deceiving since it used 4 of my existing apps as a reference 🙂
```

<a id="particles"></a>

## Particles & shapes

### A 5,000-drone light show simulation over water

[@sunset_evm](https://x.com/sunset_evm/status/2120275728339964015) · 0:30 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2120275728339964015/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2120275728339964015?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
I gave Gemini 4 Carbon in /swarm mode one prompt:

"Build a 5,000-drone light show over a night waterfront. One HTML file. No external assets."

What came back:
- 5,000 glowing drones in a single InstancedMesh at 60 FPS
- Neon bloom, a city skyline and reflective water
- 4 formations: spinning Earth, twisting DNA helix, rainbow torus knot, and a phoenix that keeps flapping
- Drones swirl between shapes instead of sliding in straight lines
- Live FPS, formation buttons, bloom and swirl sliders

One file. Zero assets and @antigravity
```

<a id="anime"></a>

## Anime

### Pixel art of a cheetah running

[@duke_mv](https://x.com/duke_mv/status/2113018068981182659) · 0:16 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2113018068981182659/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2113018068981182659?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon - 640x360 pixel art of cheetah running(thats the whole prompt)

This is the best output I've got with this prompt compared to all the frontier models till now.
```

<a id="comparison"></a>

## Tests & comparisons

### Comparing 3D cow cycling outputs in Three.js

[@TimJayas](https://x.com/TimJayas/status/2113358260933988655) · 0:50 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2113358260933988655/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2113358260933988655?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
i hate to say this but grok 4.7 is outdated and we need grok 4.8 now

Gemini 4 Carbon vs Grok 4.7

same prompt: build 3d cycle riding cow using three.js

grok 4.7's cow looks like it came straight from mars 😭

we were supposed to get grok 4.8 this months @elonmusk please release the model
```

### Pixel art running cheetah model comparison

[@duke_mv](https://x.com/duke_mv/status/2113616533939466734) · 0:12 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2113616533939466734/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2113616533939466734?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon vs Opus 5.5 vs GPT 6 Astra

In my opinion Gemini 4 Carbon's output is significantly better than the other two, what do you guys think?

Prompt - 640x360 pixel art of cheetah running

Credits - @HarshithLucky3
```

### Four models generating a mechanical Indian peacock

[@srikanthvaluri](https://x.com/srikanthvaluri/status/2114748807464546689) · 0:31 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2114748807464546689/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2114748807464546689?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Same prompt, 4 models: mechanical Indian peacock 🦚

Gemini 4 Carbon → most real 
Opus 5.5 → best animation
Gpt-6 Astra → clean but pale
Gpt-6 Sol → less detail

gemini 4 carbon under the name "Gemini 4 Argon" in arena three days back.

Carbon wins for me! Your pick? 👇
```

### Pouring beer interactive 3D webpage comparison

[@HIX_AI_](https://x.com/HIX_AI_/status/2115699353675354307) · 0:23 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2115699353675354307/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115699353675354307?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Google just dropped Carbon—rumored to be the new coding king dethroning GPT-6 Astra and Claude Opus 5.5. This comes just two weeks after Gemini 4 Argon stole the spotlight.

We gave Gemini 4 Argon and Claude Opus 5.5 on HIX AI the exact same prompt: build an interactive 3D webpage where you can pour beer into a glass.

Here's how they performed. 🍺
```

### Superman multiverse animation comparison

[@Inmerson](https://x.com/Inmerson/status/2115721948886155726) · 0:58 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2115721948886155726/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115721948886155726?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
GEMINI 4 CARBON "Superman Multiverse" 
Left "Carbon", Right: "Argon"
Prompt: behold superman in continuous animation in different art style
```

### Interactive 3D cafe racer bike comparison

[@dromexa](https://x.com/dromexa/status/2115802517942497491) · 0:29 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2115802517942497491/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115802517942497491?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
🚨 Gemini 4 Carbon vs Opus 5.5

Same prompt, one shot each: a café racer you can X-ray, cut in half, explode and lay out part by part.

Carbon's bike looks like it came out of a real workshop.

Opus is still great at games. But for 3D, Carbon just took the crown

Google is cooking
```

### Comparison of motion graphics showreel code

[@leo114119](https://x.com/leo114119/status/2115823149849714738) · 0:15 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2115823149849714738/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115823149849714738?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon Vs Opus 5.5  15 秒前端代码动效视频对比

只能说，在 Opus 5.5 曾经最有优势的地方。。。。。

Carbon 呈现了更好的效果。。。。实实在在的超越了

prompt: 

make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it’s your showreel for a résumé. go all out
```

### Interactive rainbow jelly comparison across models

[@0xRhinoX](https://x.com/0xRhinoX/status/2115891194383200515) · 0:23 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2115891194383200515/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115891194383200515?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon just DESTROYED Opus 5.5. For $4.30

Same prompt: rainbow jelly you can cut, nail and torch.

Gemini 4 Carbon - $4.30, 32 min
Opus 5.5 - $14.00, 1h 20m

Carbon's jelly is bright, sharp and throws rainbow shadows across the table.
Opus looks washed out next to it.

3x cheaper. 2x faster. 1 day old.

Is Opus still worth $14?
```

### Running T-rex in Three.js model comparison

[@ValencianaAbel](https://x.com/ValencianaAbel/status/2115918611676041698) · 0:08 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2115918611676041698/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2115918611676041698?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
🚨 Gemini 4 Carbon vs Opus 5.5

Same prompt, both low effort: running T-rex in Three.js.

Carbon's dino looks built. Opus still looks like a toy.

who's better
```

### Tiny troublemakers benchmark between Carbon and Opus

[@0xPorterio](https://x.com/0xPorterio/status/2116108534051905642) · 0:29 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2116108534051905642/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116108534051905642?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
🚨 Gemini 4 Carbon is 3x cheaper than Opus 5.5. but is it better?

same prompt: 9 tiny troublemakers, a dock full of tools, and one of them has to pop at the end.

Gemini 4 Carbon - $4.10, 34 min
Opus 5.5 - $12.80, 1h 12m

Carbon looks SERIOUSLY good. brighter, shinier, more chaos.
Opus feels more alive. the way they all stare at the one getting squashed got me

watch till the end, the inside of the black one is where it gets interesting.

is Opus still worth 3x the price?
```

### Interactive rainbow jelly pumpkin comparison

[@0xRhinoX](https://x.com/0xRhinoX/status/2116301725951013180) · 0:26 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2116301725951013180/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116301725951013180?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon just ANNIHILATED Opus 5.5. For $3.20

Same prompt: a rainbow jelly pumpkin you can carve and light up.

Gemini 4 Carbon - $3.20, 31 min
Opus 5.5 - $28.73, 1h 50m

Carbon turned it into a full Halloween night: stars, fireflies, a glowing rainbow face and candy you can feed it.

Opus's pumpkin looks washed out. You can barely see the face.

9x cheaper. 3x faster. Opus got nerfed and now everyone is beating it.

Is Opus still worth $28?
```

### Zombie hand animation model comparison

[@noclipepe](https://x.com/noclipepe/status/2116445289468850366) · 0:39 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2116445289468850366/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116445289468850366?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
GEMINI 4 CARBON BURIED OPUS AND ASTRA THIS HALLOWEEN 💀

Same prompt: a zombie hand claws out of a grave and rots down to the bone.

· Gemini 4 Carbon: 1h 23m · $10.2
· Opus 5.5: 1h 6m · $8.1
· GPT-6 Astra: 24m · $5.7

Carbon went full horror movie: candlelit graveyard, labeled anatomy at every stage.
Opus nailed the rot but lost on the scene.
Astra finished first and built a landing page with a hand on it.

Halloween test via
```

### Mechanical watch 3D model comparison

[@dromexa](https://x.com/dromexa/status/2116518366919667775) · 0:30 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2116518366919667775/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116518366919667775?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
🚨 Gemini 4 Carbon vs Opus 5.5, round 2

Same prompt, one shot each: a mechanical watch you can X-ray, cut in half, explode and lay out part by part.

Round 1 was a motorcycle. This time every part is tiny.

Carbon's balance wheel actually ticks and every gear turns at the right speed

2 for 2. Carbon is the 3D king right now
```

### Robotic great white shark model comparison

[@0xPorterio](https://x.com/0xPorterio/status/2116548548334321967) · 0:29 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2116548548334321967/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116548548334321967?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
🚨 Gemini 4 Carbon is the new Opus 5.5 killer. or is it?

I gave both the exact same prompt:
"build a robotic great white I can take apart piece by piece."

Split screen. Same camera. Same 29 seconds.
Here's what came back 

Gemini 4 Carbon:
→ fastest build of the two, by a mile
→ the flashiest FX: a lidar sweep from the eye and a heavy jet wake
→ 7 body links, flat shading, one row of cone teeth
→ blow it apart and you get… a pile of plates

Opus 5.5:
→ 1,634 parts, every one written in code
→ 12 vertebrae with ball joints and coil springs between them
→ 30 blade teeth in two rows, and the upper jaw slides forward like a real great white
→ 0:06 the jaw drops: a glowing throat gear and 6 pumping rams inside
→ 0:17 the hull swings open: a full rib cage, hydraulics, cable looms
→ 0:20 the shell blows off and the whole skeleton stays standing in mid-air

Gemini won speed and FX.
Opus won everything you can actually see inside.

Final score: 77 vs 90.

28.8 seconds. One HTML file. Zero 3D software.
Even the soundtrack is generated in code.

So is Gemini 4 Carbon really the Opus 5.5 killer?
Or did it just finish first? ↓
```

### Haunted house website comparison

[@keydol123](https://x.com/keydol123/status/2116556350130163783) · 0:24 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2116556350130163783/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116556350130163783?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
I gave Gemini 4 Carbon and Opus 5.5 the exact same prompt:
"Build a haunted house website"
One made it cute. The other made it actually haunted. 

Which house are you walking into tonight?
```

### Interactive hot spring with capybaras comparison

[@ottollm](https://x.com/ottollm/status/2116577106238873765) · 0:31 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2116577106238873765/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116577106238873765?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
HOLY F*CK. Gemini 4 Carbon just DESTROYED Opus 5.5. and i say this as the biggest Opus fan on this app.

same prompt, one shot, no testing, no second tries: 9 capybaras in a hot spring, 6 tools that all have to work, and a finale where a baby capybara floats up in a bubble and plops back into the water.

> Carbon: nine capybaras spread across the whole spring, each one doing its own thing. you can read every single one
> Opus: all nine pile into one furry traffic jam in the middle of the pool and basically stay there
> Carbon's spring looks like a game you'd pay for. Opus's looks like a nice demo

wait.

a toy lives or dies on one thing: do you want to keep poking it. i wanted to keep poking Carbon's.

Opus read the brief. Carbon built the onsen.
```

### Animated cutaway of a radial airplane engine

[@olezhavich](https://x.com/olezhavich/status/2116606788241969445) · 0:11 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2116606788241969445/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116606788241969445?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Is Gemini 4 Carbon really that good? I gave four models a 9-cylinder radial engine ⚙️

Same prompt, one try each: an animated cutaway of an airplane engine.

All four got the mechanics right (pistons fire in the correct order, I checked), so it comes down to the details:

>Gemini 4 Carbon: crisp, clean, flames you can read at a glance. The most polished.

>Claude Opus 5.5: intake pipes looping into every cylinder, exhaust stacks, numbered heads. Gets my engineering award.

>Gemini 4 Argon: the most atmospheric, but less crisp.

>GPT-6.1 Sol: a clean blueprint, but the flames are tiny and dim.

Is Carbon the new king, or does Opus still win on engineering?
```

### Three.js mechanical eagle comparison

[@srikanthvaluri](https://x.com/srikanthvaluri/status/2116767284618486044) · 0:27 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2116767284618486044/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116767284618486044?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon VS Gemini 4 Argon.

- Create a 3D mechanical eagle in Three.js

Eagle with steel feathers, intricate gears can has detailed designed it.

Which model actually nailed it?
```

### Nine-cylinder radial engine animation comparison

[@m1lad_az](https://x.com/m1lad_az/status/2116853285617336424) · 0:11 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2116853285617336424/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116853285617336424?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Four models. One prompt. A 9-cylinder radial engine. ⚙️🔧

🔥 Gemini 4 Carbon — Cleanest flames and sharpest overall look
🛠️ Opus 5.5 — Best mechanical detail and piping
🌫️ Gemini 4 Argon — Nice atmosphere, softer edges
☀️ GPT-6.1 Sol — Clean, but the flames feel weak

All of them got the pistons moving ✅

Only one actually feels engineered 🧠

Carbon or Opus — which one wins? 🏆
```

### Two-stroke chainsaw engine cutaway comparison

[@olezhavich](https://x.com/olezhavich/status/2116892619309461745) · 0:11 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2116892619309461745/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116892619309461745?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Round 2: is Gemini 4 Carbon still that good? I gave four models a two-stroke engine ⚙️

Same prompt, one try each: an animated cutaway of the engine inside a chainsaw. The one thing it has to show is the explosion that pushes the piston down.

>Gemini 4 Carbon: crisp lines, nice mist, but the flame is barely there. You have to hunt for the power stroke.

>Gemini 4 Argon: lovely particle flow, but the flame is small.

>Opus 5.5: the clearest story. Blue fresh mix, a big orange burn, grey exhaust leaving the pipe. You understand the engine in 3 seconds.

>6 Astra: the most real-looking hardware. Bolts, fins, a ceramic spark plug and the longest burn of the four.

My pick: Astra for realism. Carbon, this time you lost. Is it still the king?
```

### Interactive running V8 engine model comparison

[@dromexa](https://x.com/dromexa/status/2116927253980594275) · 0:29 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2116927253980594275/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116927253980594275?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
🚨 Gemini 4 Carbon vs Opus 5.5, round 3

Same prompt, one shot each: a running V8 you can X-ray, cut in half, explode and lay out part by part.

A motorcycle, a watch, and now an engine.

3 for 3. Carbon swept it

What should round 4 be? 👇
```

### Giraffe and gorilla boxing comparison

[@ValencianaAbel](https://x.com/ValencianaAbel/status/2117003519832068329) · 0:08 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2117003519832068329/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2117003519832068329?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
I asked for a giraffe and a gorilla boxing 🥊

Claude Opus 5.5 vs Gemini 4 Carbon

Same prompt, both low effort: gloves on, flat ring, fight loop.

who's better
```

### Animated SVG of an octopus making breakfast comparison

[@olezhavich](https://x.com/olezhavich/status/2117323673040568439) · 0:13 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2117323673040568439/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2117323673040568439?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
8 tentacles. 8 jobs. 4 AI models 🐙

Same prompt, one try: an animated SVG of an octopus making breakfast with every single tentacle busy at once.

•Gemini 4 Carbon: the best texture, warm morning lighting, and overall moody kitchen vibe.

•Gemini 4 Argon: best octopus character design and a bright checkered table, though tentacles are a bit stiff.

•Opus 5.5: detailed suckers, great tentacle anatomy, and a pancake caught mid-flip.

•6 Astra: fun acting and sweat-drop panic, but lacks visual depth.

Funny detail: mentioned a cat as an optional gag, and all four models added one.

Carbon takes #1, Argon is a close second. Who's your winner?
```

### Animated radial engine cutaway compared across four models

[@SamgreyAi](https://x.com/SamgreyAi/status/2117363216036536424) · 0:11 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2117363216036536424/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2117363216036536424?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
9 cylinders. 4 AI models. Which engine would you trust to keep a plane in the air? 

Same prompt: an animated cutaway of a 9-cylinder radial airplane engine.

Gemini Carbon · Gemini 4 Argon · Claude Opus 5.5 · GPT-6.1 Sol

Ignore the colors and watch the flames. That’s where the four split.

→ Gemini Carbon: the cleanest of the four. Crisp lines, readable combustion in every cylinder, nothing cluttered
→ Gemini 4 Argon: the warmest. Big amber blasts and a glowing, atmospheric feel, but softer edges
→ Claude Opus 5.5: the most “engineered.” Curved intake pipes into every cylinder, hot orange and cold blue chambers, and the busiest, most mechanical look
→ GPT-6.1 Sol: a clean blueprint, but the flames are small and dim, and it feels the quietest
Same engine, four different answers to “what does fire look like inside a cylinder?”

My eye picks Carbon. My engineer picks Opus.
Which one would you put in a plane?
```

### Octopus making breakfast comparison across four models

[@kinderlayer](https://x.com/kinderlayer/status/2117622619990093952) · 0:13 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2117622619990093952/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2117622619990093952?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
this is f*cking adorable. four models, one prompt: an octopus making breakfast with all eight arms.

Gemini 4 Carbon · Gemini 4 Argon · Claude Opus 5.5 · GPT-6 Astra

eight arms, eight jobs - flipping pancakes, pouring coffee, reading the recipe, frying eggs, all at once. and honestly? they all pulled it off. different vibes, different kitchens, same impossible multitask nailed.

I didn’t touch a thing and I’m not scoring them. so it comes down to taste: whose kitchen would you actually eat breakfast in?

Carbon, Argon, Opus or Astra? drop your pick
```

### Jelly DVD screensaver comparison between two models

[@0xRhinoX](https://x.com/0xRhinoX/status/2117682945116774562) · 0:25 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2117682945116774562/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2117682945116774562?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
WTF Claude. I asked for the DVD screensaver and it made a f*cking ad for itself

Same prompt: the DVD screensaver, but out of jelly.

Gemini 4 Carbon made the DVD logo.

Claude Opus 5.5 said the DVD logo is trademarked and made the Claude logo instead.
```

### Drawing a city sunset with a muscle car

[@olezhavich](https://x.com/olezhavich/status/2117706843799658507) · 0:11 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2117706843799658507/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2117706843799658507?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Is Gemini 4 Carbon still the best? I gave four models a blank page and a pen ✏️

Same prompt, one try each: draw a sunset over a city in about 10 seconds, watch the color flood in, and park an old American muscle car in front.

All four drew it live with a pen (and all four painted the car teal), so it comes down to the details:

>Gemini 4 Carbon: a moody night city, glowing windows and headlight beams across the road. The most cinematic.

>Claude Opus 5.5: the most detailed skyline, with tiny windows, palm trees, a sunburst and birds.

>Gemini 4 Argon: a purple and orange sunset with the sun between the towers, and a nicely drawn car.

>GPT 6 Astra: the cleanest car sketch, but the palest colors.

Is Carbon winning on lighting again, or does Opus still win on detail?
```

### Exploded view of an interactive sewing machine

[@dromexa](https://x.com/dromexa/status/2118072739864989944) · 0:32 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2118072739864989944/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2118072739864989944?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
🚨 Gemini 4 Carbon vs Opus 5.5, round 4

Same prompt, one shot each: a sewing machine you can X-ray, cut in half, explode and lay out part by part. And it has to actually make a stitch.

Carbon made a cool f*cking steel machine.

4 for 4. Carbon is untouchable

What should round 5 be? 👇
```

### A bicycle riding a pelican generation test

[@Haleeeemahh](https://x.com/Haleeeemahh/status/2118316297410810032) · 0:20 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2118316297410810032/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2118316297410810032?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
opus 5.5 vs gemini 4 carbon - bicycle riding a pelican 

same prompt, both one shot 

who did it better ?
```

### Interactive rainbow jelly simulation comparison

[@0xRhinoX](https://x.com/0xRhinoX/status/2118415577299460432) · 0:37 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2118415577299460432/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2118415577299460432?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Fable 5.5 just DESTROYED Gemini 4 Carbon. Its jelly f*cking grows back. I never asked.

Same prompt: rainbow jelly you can cut, nail and torch.

Gemini 4 Carbon - $4.30, 32 min
Fable 5.5 - $48.50, 45 min

Carbon made great jelly. Cut it and it stays cut.
Fable decided that wasn't enough. Cut it, nail it, torch it, and it pulls itself back together like the T-1000.

11x the price. Worth it?

Every new model gets the Rainbow Jelly test. Follow to see who's next.
```

### Comparing three Gemini models on a Blender chase scene

[@HeathIsidr64707](https://x.com/HeathIsidr64707/status/2119384683868012706) · 0:10 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2119384683868012706/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2119384683868012706?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Same Blender prompt across 3 Gemini generations: a supercar chasing a steam train across a forest viaduct.

• 4 Carbon: full night cinema, wet road reflections, volumetric steam (~1h54m, $11.80)
• 3.8 Flash: flat fog + camera flies straight into a tree at 0:07 lol
• 4 Argon: clean golden-hour viaduct & smooth smoke

#b3d #blender #Gemini #LLM
```

### Gemini Carbon versus Claude Opus Blender shark prompt

[@HeathIsidr64707](https://x.com/HeathIsidr64707/status/2119445073352089952) · 0:10 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2119445073352089952/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2119445073352089952?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon (H) vs Claude Opus 5.5 (XHigh) in Blender  

Same Blender Python prompt: What will Sisyphus Shark look like in Hungry Shark:World

• Carbon: [1h 29m] · $[8.82] 
• Opus 5.5: [1h 10m] · $[15.66] 
(only coding)

Which underwater vibe wins for you?

 #b3d #blender #Gemini #Claude
```

### Animated radial aircraft engine across four models

[@0xKenny1st](https://x.com/0xKenny1st/status/2119533338784313413) · 0:11 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2119533338784313413/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2119533338784313413?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon vs Gemini 4 Argon vs Claude Opus 5.5 vs GPT-6.1 Sol

Same prompt: an animated 9-cylinder radial aircraft engine.

All four get the piston mechanics right. The difference is in the execution: flames, intake pipes, exhaust, detail.

Top left: Gemini 4 Carbon. Top right: Gemini 4 Argon. Bottom left: Claude Opus 5.5. Bottom right: GPT-6.1 Sol.

Which one gets the engineering award?
```

### Motor controller PCB design comparison

[@seveibar](https://x.com/seveibar/status/2120531821306032607) · 0:59 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2120531821306032607/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2120531821306032607?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Fable 5.2 High vs Gemini 4 Carbon High

Fable is slightly better but 20x more expensive 😮 ($200 vs $12), not in this video but yea carbon is better than astra at PCB design!

prompt: “Create an SoC linux based motor controller using tscircuit”
```

### World-turtle planet comparison between Gemini and GPT-6

[@camperaigg](https://x.com/camperaigg/status/2120575785161670732) · 0:30 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2120575785161670732/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2120575785161670732?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
🐢⚔️ Google Gemini 4 Carbon vs OpenAI GPT-6 Astra, same prompt, blind head-to-head.

"Build a 30-second pixel-art living World-Turtle planet with rainforest, waterfall, sand dunes, a moving city simulation, and high-quality sound."

Zero code touched. Zero peeking at each other's folders. 🤯

🟦 TOP: CARBON 4 High (Google Gemini 4 Carbon)
⏱️ 16 min
🎨 guided camera tour across rainforest, canal city & desert caravan · 56 citizens, 3 barges, twin waterwheels, anvil sparks & 26 dusk sky-lanterns

🟨 BOTTOM: ASTRA 6 High (OpenAI GPT-6 Astra)
⏱️ 11 min
🎨 wide space diorama · 32 route-following residents, 3 waterfalls, rainforest rain, turning waterwheel, glowing dusk windows & fireflies

Which one did better here??
```

<a id="showcase"></a>

## Model showcases

### Thirty-second professional motion graphics animation

[@Genysis_Ai_26](https://x.com/Genysis_Ai_26/status/2112909613788230013) · 1:13 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2112909613788230013/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2112909613788230013?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
GEMINI 4 CARBON 

Prompt: Create a professional motion graphics 30 seconds.

And honestly it's crazy good just needs little more promoting and definitely it can reach opus 5.5 level.

So yeah, it can dethrone opus 5.5 considering it's just first checkpoint.
```

### A bicycle riding a cow in Three.js

[@TimJayas](https://x.com/TimJayas/status/2112950910892789979) · 0:49 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2112950910892789979/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2112950910892789979?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
gemini-4-carbon is pretty amazing in terms of 3d outputs

i asked carbon to build a 3d bicycle riding a cow using three.js

since many are speculating it's going to be on par with astra, fable and even opus 5.5 so i'll to check how this output performance against them

do you think this is opus 5.5 level?
```

### A freestyle swimmer created using Three.js

[@AI_Screening](https://x.com/AI_Screening/status/2113144877257248816) · 0:15 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2113144877257248816/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2113144877257248816?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon checkpoint in the Arena under the name Gemini 4 Argon:

>A freestyle swimmer doing the front crawl using Three.js (single HTML file)
```

### Motorbike riding a pelican trying to eat fish

[@DrstaOne](https://x.com/DrstaOne/status/2113373228630704237) · 0:36 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2113373228630704237/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2113373228630704237?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Everyone asked I replied
<Gemini 4 Carbon Cooked  at SVG>

→MOTORBIKE RIDING A PELICAN AND PELICAN TRY TO EAT FISH
```
