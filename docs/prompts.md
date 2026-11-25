# Gemini 4 Carbon prompts

English · [简体中文](zh-CN/prompts.md) · [← Back to the collection](../README.md)

85 Gemini 4 Carbon videos whose creators shared the prompt. Open one to read the prompt, watch the video and **Recreate** it with Carbon on SandBase Lab. New to prompting Carbon? Start with the [prompt guide](prompt-guide.md).

Each entry quotes the creator's post as published on X, where the prompt is shared. Some creators describe the task rather than pasting the whole prompt, and some put the full text in a reply: open the post on X to read the thread. Posts keep the creator's language.

- [3D scenes](#3d-scene) (6)
- [Motion graphics](#motion-graphics) (13)
- [Games](#game) (3)
- [Product UI](#ui-demo) (2)
- [Particles & shapes](#particles) (1)
- [Charts & diagrams](#data-viz) (1)
- [Explainers](#explainer) (1)
- [Anime](#anime) (1)
- [Tests & comparisons](#comparison) (54)
- [Model showcases](#showcase) (3)

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

### Solo piano concert film rendered in Three.js

[@IamEmily2050](https://x.com/IamEmily2050/status/2120716006884786498) · 3:00 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2120716006884786498/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2120716006884786498?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon High/Antigravity 

Build a deterministic, real time capable 3 minute (180.000s, 10,800 frames at 60fps) solo piano concert film titled "PERF-01 // SYMPHONY NO. 7 IN A MAJOR, OP. 92 (II. ALLEGRETTO)" (Franz Liszt solo piano concert transcription S.464/7 of Beethoven's Allegretto) using Three.js 0.187.0 (native WebGPURenderer + three/tsl), headless Blender 5.2+ (Cycles GPU 4K OIDN baking + anatomical sculpting), AI texture lookdev, and multi-velocity grand piano synthesis.
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

### Showcase video generated with Gemini 4 Carbon

[@husky__create](https://x.com/husky__create/status/2120698249644536114) · 1:00 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2120698249644536114/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2120698249644536114?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbonにも動画を作ってもろた
Antigravityから簡単な指示を出すだけで完成🐺

プロンプト：
あなたができるようになったことを、最大限アピールするような動画を見せてください。その動画自体も、あなたができる最強の動画を見せてほしいです。GSAPやThree.jsを使用してリッチなアニメーションにするもよし。Blenderを操作して細部まで作り込まれた３Dアニメーションを作るもよし。 1分。16:9。作った動画はMP4で書き出してください。
```

### Project demo created with Gemini 4 Carbon

[@IamEmily2050](https://x.com/IamEmily2050/status/2122530276182274435) · 1:00 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2122530276182274435/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2122530276182274435?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon 
Antigravity 

It was fun working on this project, I will put everything on GitHup later this weekend, also I attached the prompt.
```

### SVG animation of Qin Shi Huang riding a bicycle

[@GKev1n](https://x.com/GKev1n/status/2122837186047553933) · 0:36 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2122837186047553933/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2122837186047553933?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon 是吧？干了 36 分钟是吧？

我 GPT 从今天开始打的就是精锐！

找 GPT 6.2 Astra 画了一下，提示词就一句话，做一个秦始皇骑单车巡视六国的 svg 动画，我觉得比 Carbon 好多了，还是老实做哈基米吧！

另外，不得不吐槽一句，Astra 确实慢啊，在 Codex 里只能跑到 9～14 tps，看来以后急活还真不能找他做了呀，哈哈哈
```

### Motion graphics concept short film by Gemini Neon

[@walter201230pro](https://x.com/walter201230pro/status/2123367292042203600) · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2123367292042203600/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2123367292042203600?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
谷歌疯了，发模型的速度快的惊人。

一度怀疑这发布的是大模型吗？发布大模型的节奏是这样的？  

总体体验下来，neno 很不错，速度快，不像 carbon 那么龟速，干活质量也可以，达到了综合平衡，主要还有就是量足，感觉怎么用都用不完。推荐。  

下面这个视频也是 neno 一键出的，也把提示词给到大家，后面新模型出来了，想看这个模型的视频能力怎么样，直接可以用这句提示词测试。  

提示词：请从零创作并导出一部约 20 秒的 16:9（1920×1080，60fps）Motion Graphics 概念短片，主题围绕你作为「Gemini 4  Neon」的视觉与动效表达力，具体创意、分镜和音乐编排由你自主导演。
```

### Custom video created for Leviwoyun

[@ChrisHKAI](https://x.com/ChrisHKAI/status/2124835361591263335) · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2124835361591263335/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2124835361591263335?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
这次帮 @Leviwoyun 云哥做了个视频， 
用Gemini 4 Carbon High 做的， 
喜望云哥喜欢～  

Skill 地址：   
https://github.com/ChrisHKAI/ChrisHKAI-Video     

用法请看下面文章
```

<a id="game"></a>

## Games

### A Flappy Bird style platformer game

[@SimonasLTU1](https://x.com/SimonasLTU1/status/2120186826451288182) · 0:40 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2120186826451288182/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2120186826451288182?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon. Yes, I'm this professional and serious. Prompt: "Create a game called pooperman, basically it's a flappy bird, but with a guy that poops on clicks, should be three.js graphics, but platformer style." It took 14 minutes to create this game.
```

### Simulated GTA 6 highway driving gameplay

[@p0lybender](https://x.com/p0lybender/status/2121314170557612245) · 0:51 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2121314170557612245/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2121314170557612245?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
one prompt to Gemini Carbon: “make GTA 6 gameplay.” it came back with this.

not a leak. not a trailer. not a dev build. one sentence in, and a model that has seen enough of the real game to fill in everything else.

Jason is behind the wheel on a highway. the camera sits just behind the car, the road stretches ahead, traffic moves around him, the HUD glows in the corner. it looks like a clip Rockstar could have put on a loading screen.

nobody wrote the mission. nobody modeled the road. nobody rigged the car. the model guessed what GTA 6 should feel like, and it guessed close enough that you’d pause before calling it fake.

it used to work in one direction. a team spent months building a game, and only then could anyone show it.

now the footage can show up before the game does. the video isn’t proof that a game exists anymore, it’s just what a sentence looks like when a model finishes it.

and the real GTA 6 is still on its way. a prompt just got the first impression in ahead of Rockstar.

so when the next official trailer drops, how will you tell which one people made?
```

### Playable Counter-Strike style shooter game

[@VaibhavSisinty](https://x.com/VaibhavSisinty/status/2123144283197002116) · 1:42 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2123144283197002116/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2123144283197002116?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Logan typed one line.

Make me a CS clone.

One shot. No iteration. No fixes.

A playable Counter-Strike-style shooter, built live in front of us.

This is Gemini 4 Carbon. Logan said it is the best one-shot build he has seen.

One line in. A whole game out.
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

### UI kit frost box 3D animation

[@onuro](https://x.com/onuro/status/2123411939359609266) · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2123411939359609266/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2123411939359609266?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Made in @fountible of the day: UI Kit Frost Box 3D Animation. Made using Bro. Model: Gemini 4 Carbon.

See live and remix https://go.fountible.com/amberbox

PS: Static shader/code layer is also in the file. Cheers
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

<a id="data-viz"></a>

## Charts & diagrams

### Interactive DFT epicycle visualization in Three.js

[@c0tanpoTesh1ta](https://x.com/c0tanpoTesh1ta/status/2121589168996544584) · 0:12 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2121589168996544584/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2121589168996544584?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini Carbonで、

実際の複素離散フーリエ変換（DFT）と回転するエピサイクル（周転円）の重ね合わせ計算のみで「山の上にいるごじにゃ」を一筆書き描画する、Three.js インタラクティブ数理ビジュアライゼーションを作成して。
```

<a id="explainer"></a>

## Explainers

### Video reverse engineering and prompt replication

[@leaf_sanren](https://x.com/leaf_sanren/status/2123687539642933402) · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2123687539642933402/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2123687539642933402?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
妈呀！😮 Antigravity 逆向视频的能力恐怖如斯！！
到底还有多少人不知道Gemini 4是视频界的 REA 啊！！👏

我都觉得不需要 Gemini 4系列最牛的 Neon或Carbon，Hydrogen 就直接完成了原片的拆解、提示词逆推，然后自行调用 Omni 1.2 Flash 去生成了。

我给你们看看他自己写的提示词，几乎就是专门针对Google Omni模型特质（全能参考多模态）写的非常讨巧的提示词👇，可以自己复用下：

 接口与参数：
      • POST https://generativelanguage.googleapis.com/v1beta/interactions
      • model: "gemini-omni-1.2-flash"，background: true
      • response_modalities: ["video"]
      • response_format: {"type": "video", "aspect_ratio": "16:9", "resolution": "360p", "duration": "8s"}
      • input 数组顺序：[无声参考视频(8.08s)] → Image 1（08_浅奶白圆脸异瞳_v3定妆照.jpg）→ Image
      2（02_shot02_t5.5s.jpg 红衣机车追兵帧）→ [下方 Prompt]

  1. 前半段（cat_p1，输入 0 ~ 8.08s）原提示词：

    Replicate the EXACT 8-second multi-shot camera cuts, framing, speed, lighting, highway overpass
    environment, and red armored cyber-biker pursuit (matching Image 2) from the reference video 1-to-1,
    replacing ONLY the white cat with the chubby pale cream-white heterochromia cat from Image 1 (one
    bright blue eye, one warm amber eye, round chubby cheeks). Keep the cat's exact mid-air levitating
    invisible-motorcycle pose — paws raised forward, feet NEVER touching the ground. Keep every camera cut
    and background detail identical to the reference video.

  2. 后半段（cat_p2，输入 7.0 ~ 15.08s，含结尾张嘴“叮叮”特写）原提示词：

    Replicate the EXACT 8-second multi-shot camera cuts, framing, speed, lighting, highway overpass
    environment, wide rear overpass chase with the red biker, and the final close-up of the cat's face
    opening its mouth at the end from the reference video 1-to-1, replacing ONLY the white cat with the
    chubby pale cream-white heterochromia cat from Image 1 (one bright blue eye, one warm amber eye, round
    chubby cheeks). Keep the cat's exact mid-air levitating invisible-motorcycle pose — paws raised
    forward, feet NEVER touching the ground — and match the final mouth-opening expression.

补充一下，因为 omni 模型输入（<10s）和输出（<15s）是有上限的，所以当时是先把原视频的 18 秒加倍速压缩到了 15 秒以内，生成之后再放回原速的。
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

### Pelican riding a bicycle SVG animation benchmark

[@KOF97AI](https://x.com/KOF97AI/status/2120199278203449383) · 0:14 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2120199278203449383/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2120199278203449383?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
用最简单的基准测试测出模型真实代码生成能力，省去长提示词调试成本

对标模型：Gemini 4 Carbon 对决 Gemini 4 Argon
测试方式：统一通过 Vertex AI API 调用，零微调无二次修正，纯 One-shot 直出
测试提示词：
创建经典的鹈鹕骑车 SVG 动画
评估重点：首版代码的 SVG 结构完整度、运动轨迹计算与矢量动画流畅度

#Gemini #AI测评
```

### Oboe concerto sheet music generated in LilyPond

[@aug5thmusic](https://x.com/aug5thmusic/status/2120304508278632806) · 2:36 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2120304508278632806/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2120304508278632806?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
I gave Gemini 4 Carbon the same oboe concerto prompt I gave to Opus 5.5 on the Baroque AI Music Quiz. I think Opus 5.5’s version is better, but Carbon’s is better than I expected.

Prompt: “In LilyPond, write the opening movement of an oboe concerto in the virtuosic style of Vivaldi, C minor, 2/4 time, allegro. Give the music a serious and regal character, with a variety of runs and dotted rhythms. Use two staves for the basso continuo and one for the oboe. Use the ritornello form, and do not introduce the soloist until the second section. Make the basso continuo part as dynamic and interesting as the oboe.” (High effort)
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

### Flipping an iceberg with Fable and Carbon

[@AIMind_Ai](https://x.com/AIMind_Ai/status/2120921919427891335) · 0:30 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2120921919427891335/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2120921919427891335?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
~30x cheaper. Claude Fable 5.2 vs Gemini 4 Carbon, same prompt: flip an iceberg.

Claude Fable 5.2 - ~$10
Gemini 4 Carbon - ~$0.30

One prompt each, no edits.

Can you tell which one costs $10?
```

### Interactive SVG of a juggling biking lion

[@SahilPanhotra](https://x.com/SahilPanhotra/status/2120978349967458704) · 0:48 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2120978349967458704/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2120978349967458704?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
GEMINI 4 HYDROGEN VS GEMINI 4 CARBON

same interactive svg prompt: lion biking, juggling across 4 seasons + web audio sfx.

Carbon (bottom) actually nailed the crossing juggling arcs and even added winter breath puffs. 

Hydrogen (top) straight up faked the juggling by floating the balls in place though its season wipes and container clipping are way cleaner.

Carbon for raw detail & physics. Hydrogen for fast UI logic.
```

### Seven models compared across three prompts

[@ediz_mercan](https://x.com/ediz_mercan/status/2121275714213203985) · 0:41 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2121275714213203985/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2121275714213203985?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
google vs anthropic: 7 models, the same 3 prompts, zero human code

istanbul at sunset, a phoenix in svg, a glass of turkish tea 🇹🇷

gemini 4 hydrogen, argon, carbon vs claude haiku, sonnet, opus, fable. then i pushed them to max effort

cheapest: $0.37. most expensive: $34

who did it best? 👇

#Gemini4 #Claude
```

### Copper red octopus moving in reef ravine

[@teddyaisi](https://x.com/teddyaisi/status/2121800606406885880) · 0:20 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2121800606406885880/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2121800606406885880?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon vs Gemini 4 Argon vs Gemini 4 Hydrogen

The Three.js task: a copper-red octopus reaches out, grips a rocky ledge and pulls itself forward in a turquoise reef ravine.

Which octopus makes the arm grip and body pull feel most connected? 👇
```

### Pelican riding a bicycle across nine models

[@Emproof31825](https://x.com/Emproof31825/status/2121838448940286326) · 4:07 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2121838448940286326/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2121838448940286326?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
同一个提示词，9 个顶级大模型同台手搓「鹈鹕骑自行车」2D SVG 动画！🚲🦩 不吹不黑，全是本地 CLI 实跑数据👇

⚡ 速度之王：Grok 4.7 (low-fast) 只用 32.2 秒 交卷（162行），Opus 5.5 74.8 秒紧随其后；
 🎨 体量卷王：Gemini 4 Argon 直接干出 950 行（双腿+翅膀逆向运动学 IK + 5层视差 + 变速按铃）；Gemini 4 Carbon 也写了 829 行；
 🖥️ 全栈装修王：阿里新出的 Qwen 4-Max-Preview 写了 633 行，直接给你整了个带毛玻璃导航和 HUD 仪表盘的小应用（而且我实测它逻辑推理比 Qwen 3.8 快了 3.75 倍，写 Python 并发缓存一次跑通单测！）；
 📰 极简海报派：GPT-6-Astra（330行）走莫兰迪绿画报风，克制又高级。

👉 评论区投票：你觉得 9 宫格里哪只鹈鹕骑得最像真的？扣编号我把测试详情发你！

#AI大模型 #千问4 #Qwen4 #GPT6 #ClaudeOpus #Gemini4 #程序员 #AI编程 #前端动画 #科技测评
```

### Tuareg portrait video recreation comparison

[@leaf_sanren](https://x.com/leaf_sanren/status/2121896725103407413) · 0:10 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2121896725103407413/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2121896725103407413?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
我的妈😮！现在用好Gemini 4真是红利啊！

我震撼于 Gemini 的复刻能力，真的是视频界的 rea 啊！
尤其是新的 Gemini 4 更是恐怖如斯。Argon和Hydrogen都这么强，难以想象Carbon啊！

大家可以看一下原片和复刻效果，反推的提示词交给 muse 生成的。

大家也可以试试prompt（直接来自Gemini4输出的文件）👇：

   - **生图**：`Intimate candid documentary close-up portrait in warm Sahara desert sunlight, 9:16 vertical. A weather-tanned Tuareg young man wrapped tightly in coarse faded dusty indigo-blue cotton turban and face veil covering nose and mouth, fine desert sand dust grains speckled naturally across brow creases and eyelashes, eyes lowered/closed gently against blowing wind, 85mm telephoto lens f/2.8, blurred sunlit ochre dune horizon behind, raw skin pores, unretouched 35mm documentary realism.`
   - **Muse**：`85mm 中长焦贴近人文纪录片固定特写微晃，粗犷干燥的沙漠风把细沙粒吹过青年紧裹着的褪色靛蓝粗布头巾与额间沙尘皮肤，他闭眼承受风沙片刻后缓缓睁开平静深邃的双眼微微偏头避风。严格一镜到底，不要过度磨皮、不要商业广告打光。`
   - **Seedance**：`Documentary telephoto close-up in windy desert daylight; fine golden sand dust drifts across dusty indigo cotton turban and weathered brow as man slowly opens calm eyes.`
```

### Lava flow comparison in Three.js across models

[@teddyaisi](https://x.com/teddyaisi/status/2121977175612219870) · 0:20 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2121977175612219870/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2121977175612219870?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon vs Gemini 4 Argon vs Gemini 4 Hydrogen

The Three.js task: thick lava swells, splits its dark crust and folds down rock steps in a violet basalt gorge at twilight. 

Which version best conveys the lava’s weight as it bulges and spills over each ledge? 👇
```

### Comparison of four AI models generating icy cathedral

[@EnvolDev](https://x.com/EnvolDev/status/2122105333887934810) · 0:25 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2122105333887934810/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2122105333887934810?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Hydrogen vs Gemini 4 Carbon vs GPT-6.1 Sol vs Muse Spark 1.3 🧊

Google vs OpenAI vs Meta. One prompt. 🤯

Same prompt: Cathedral of Ice
Gemini 4 Hydrogen: $4.27 · 1h 23m 40s
Gemini 4 Carbon: $8.83 · 2h 39m 10s
GPT-6.1 Sol: $3.11 · 54m 19s
Muse Spark 1.3: $5.56 · 2h

GPT-6.1 Sol was the cheapest and the fastest of all four. 😱

Almost 3x cheaper and almost 3x faster than Gemini 4 Carbon.

Which one would you pick? 👀
```

### Wizard versus stone golem in a night forest

[@0xMitto](https://x.com/0xMitto/status/2122371382449184989) · 0:25 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2122371382449184989/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2122371382449184989?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
gemini 4 carbon is f*cking insane for 3D scenes.

its FIRST prompt looks as good as claude fable 5.2's FINAL version..

> same prompt, same scene, side by side
> wizard vs stone golem in a night forest
> fireball, lava cracks, the golem burns into particles
> top row = 1 prompt. bottom row = every fix after it

Find the full prompt below ↓

then judge for yourself which one you'd pay for.
```

### Four models generating a cathedral of ice

[@realdrovex](https://x.com/realdrovex/status/2122424452885717358) · 0:25 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2122424452885717358/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2122424452885717358?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Hydrogen vs Gemini 4 Carbon vs GPT-6.1 Sol vs Muse Spark 1.3 🧊

Google vs OpenAI vs Meta. One prompt. 🤯

Same prompt: Cathedral of Ice
Gemini 4 Hydrogen: $4.27 · 1h 23m 40s
Gemini 4 Carbon: $8.83 · 2h 39m 10s
GPT-6.1 Sol: $3.11 · 54m 19s
Muse Spark 1.3: $5.56 · 2h

GPT-6.1 Sol was the cheapest and the fastest of all four. 😱

Almost 3x cheaper and almost 3x faster than Gemini 4 Carbon.

Which one would you pick? 👀
```

### Four model comparison of Three.js humpback whale breach

[@teddyaisi](https://x.com/teddyaisi/status/2122544449968373997) · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2122544449968373997/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2122544449968373997?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Claude Fable 5.2 vs Gemini 4 Carbon vs GPT-6-Astra vs Gemini 4 Hydrogen

Same prompt. Build a 20-second Three.js humpback whale breach off Icelandic basalt stacks, from bursting out of the swell and rolling mid-air to a broadside slam and final tail lift.

Claude Fable 5.2 (Top left): $19.07 · 71m29s · xhigh
Gemini 4 Carbon (Top right): $13.11 · 163m18s · high
GPT-6-Astra (Bottom left): $11.10 · 72m45s · xhigh
Gemini 4 Hydrogen (Bottom right): $4.27 · 37m27s · xhigh

Fable 5.2 runs 4.5x Hydrogen's API spend for better lighting and a cleaner final beat. 

Which one would you actually pay for?👇
```

### Side-by-side comparison of peacock generations

[@ValencianaAbel](https://x.com/ValencianaAbel/status/2122880061908910432) · 0:08 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2122880061908910432/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2122880061908910432?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
GEMINI 4 CARBON really showed up looking like it got lost in the FOG

Same prompt for both: a SUPER REALISTIC peacock in a garden with its tail fully fanned

GPT 6.2 ASTRA built a SHIMMERING iridescent fan in a sunlit stone courtyard and every eye feather is CRISP 

GEMINI 4 CARBON gave me a DULL bronze fan in a misty forest that looks WASHED OUT 

Judge yourself
```

### Monet inspired Three.js Tetris game comparison

[@SimonasLTU1](https://x.com/SimonasLTU1/status/2122962883403260262) · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2122962883403260262/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2122962883403260262?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Carbon (Medium) VS. Astra 6.2 (Medium) Ultrafast. Prompt: "Create me a visually stunning Three.js tetris game inspired by the art of Monet". I'd pick Gemini 4 Carbon, but it took over 6 minutes. Astra took seconds, but of course that's just because I wanted to try it on Ultrafast mode, so there's no fair speed comparison here.
```

### Comparison of 3D scenes from two AI models

[@notjazii](https://x.com/notjazii/status/2122974870250356881) · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2122974870250356881/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2122974870250356881?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
GPT 6.2 Sol vs Gemini 4 Carbon  

tested both model with same prompt at highest reasoning available and results came out really different

> sol took 20 mins and used 6M tokens worth ~$1.6 
> carbon took 40 mins and used 6.2M tokens worth ~$2.9  

prompt was simple "surprise me in 3d that makes me feel like you are agi model" and both models decided to go with their own approach  

now you decide which model did better here
```

### Crocodile rising out of the dark

[@realdrovex](https://x.com/realdrovex/status/2123083439171842558) · 0:30 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2123083439171842558/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2123083439171842558?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
this is f*cking menacing - one of these crocs cost way more to make than the other.

same prompt, two models, a crocodile rising out of the dark.

Claude Fable 5.2 · Gemini 4 Carbon
```

### Google Earth style visualization in Three.js

[@analogalok](https://x.com/analogalok/status/2123183353436475636) · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2123183353436475636/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2123183353436475636?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Gemini 4 Neon vs. Gemini 4 Carbon.

One prompt. One HTML file. Pure Three.js.

Genuinely looks like Google Earth until you remember an LLM just one shotted the code.

And the new Artificial Analysis numbers just dropped

Gemini 4 Neon just hit 61 on the Artificial Analysis Intelligence Index (up from Carbon's 60) beating Claude Opus 5.5 (59) and sitting right behind GPT-6.2 Astra (62) and Claude Fable 5.2 (65).

The real story is the cost chart:

Claude Fable 5.2 Max: $26.54
Claude Opus 5.5 Max: $10.04
Gemini 4 Neon: $6.44
GPT 6.2 Astra Max: $4.00

Higher score than Opus 5.5 for 36% less. Over 4x cheaper than Fable. Check out the replies for benchmarks.

Prompt: 
Create a very realistic high quality earth as seen from the space. camera should auto zoom in to the statue of liberty. Make sure the entire zoom is smooth, the earth, clouds, city and the statue is highly detailed and realistic. single html file. use any libs via cdn.

Are we even going to need game engines in 2 years or is it already over?
```

### Stick figure fight animation model comparison

[@xiax0603](https://x.com/xiax0603/status/2123198294528811087) · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2123198294528811087/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2123198294528811087?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
🚨火柴人打斗动画实测对比！Gemini 4 Neon表现直逼Carbon

用户同Prompt横向实测Gemini 4系列四款模型的火柴人打斗动画生成效果

结果显示Neon的动作连贯性、画面完成度优于Argon，整体视觉表现与旗舰Carbon差距不大，几乎处于同一水准
```

### Pelican riding a bike in Three.js

[@YFarmX](https://x.com/YFarmX/status/2123375881443782819) · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2123375881443782819/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2123375881443782819?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
We gave 4 Gemini 4 models the same one-shot prompt: build a detailed 3D pelican riding a bike in Three.js 🚲

Time · cost · output tokens · $ per 1M in/out

Carbon: 9m52s · $0.53 · 52.5k · $2/$10
Neon: 5m09s · $0.77 · 51.1k · $3/$15
Hydrogen: 5m08s · $0.31 · 40.5k · $1.5/$7.5
Argon: 5m27s · $0.26 · 25.3k · $2/$10

Carbon looks best. It thought the longest (17.8k reasoning tokens) and didn't start coding until 4m17s in. The result: a textured, winding road with shadows and the most finished pelican.

Neon is the odd one. It's listed as "a fast, mid-priced model", yet it costs 50% more per token than Carbon. It thought less (13k), started coding at 1m54s and wrote the most code, but its road faces down, so it's invisible.

Hydrogen was the only one that worked untouched with everything visible. Argon, Google's flagship reasoning model, reported zero reasoning tokens. It was the cheapest, but its road faces down too.

Same one 5.2k-character prompt, no follow-ups.
```

### Iced Americano Three.js model comparison

[@TabbitBrowser](https://x.com/TabbitBrowser/status/2123852190741856596) · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2123852190741856596/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2123852190741856596?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
All four Gemini 4 models are live in Tabbit, so we gave each the same order 🧊

“One 3D iced Americano in Three.js, please.”

Argon · 6m 51s · ~$0.87
Neon · 11m 57s · ~$3.44
Carbon · 38m 42s · ~$7.98
Hydrogen · 21m 05s · ~$5.42 (2 runs)

Which cup are you grabbing? Coffee’s on us ☕
```

### Iterative web page redesign comparison across models

[@DesignArena](https://x.com/DesignArena/status/2125322475798192177) · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2125322475798192177/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2125322475798192177?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Today’s frontier models claim to fix AI slop in one edit. However, when asked to improve a page again, @GoogleDeepMind's Gemini 4 Carbon kept redesigning it up to edit 10, whereas @AnthropicAI's Claude Fable 5.2 was confident its page was already the best and barely changed it after edit 3.

Design tools increasingly make use of iterative coding agents, but these loops depend on consistent judgment, so follow-up prompts can improve a page without rewriting working layouts.

We gave four frontier models AI-slop web pages and had each model edit each page ten times in a row. Every edit was a separate call with only the latest HTML and the prompt "Make the below website look less like AI slop. Reply with only the complete HTML file."

After each edit, a separate judge call to the same model scored the page from 0% (no AI slop) to 100% (all AI slop).

Every model's judge deemed its work fixed on edit 1. However, @OpenAI's GPT-6.2 Astra kept making updates on later edits, and the other models' judges gave its output the lowest slop scores. @AIatMeta's Muse Wonder, on the other hand, shifted toward formulaic beige layouts with serif headlines.
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

### Motorbike riding a pelican trying to eat fish

[@DrstaOne](https://x.com/DrstaOne/status/2113373228630704237) · 0:36 · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2113373228630704237/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2113373228630704237?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon&utm_content=prompt-index)

```text
Everyone asked I replied
<Gemini 4 Carbon Cooked  at SVG>

→MOTORBIKE RIDING A PELICAN AND PELICAN TRY TO EAT FISH
```
