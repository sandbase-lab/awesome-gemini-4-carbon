# Gemini 4 Carbon 提示词写法：如何为视频提示 Carbon

[English](../prompt-guide.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

Gemini 4 Carbon 不直接输出视频。它写代码——通常是用 Three.js、Canvas 或 SVG 的单文件 HTML 页面——作者再把页面播放过程录下来。本合集大部分帖子是竞技场运行：同一个提示词、每个模型一次生成、两个页面并排录屏。下面的写法来自作者随视频公开的提示词，每条都链接到它产出的视频。

有一点会影响所有提示词：这个模型的思考始终开启，隐藏的推理 token 算在你的 `max_tokens` 里。API 上没有 `reasoning_effort` 参数——强度由模型自己决定（[`sandbase inspect`](https://www.sandbase.ai/model/google/gemini-4-argon?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon)）。在 SandBase 上，Carbon 检查点通过 `google/gemini-4-argon` 这个 ID 提供。

## 1. 点名单文件和渲染方式

第一句就说清交付物是什么、用什么渲染。这里效果最好的作品都做到了：

- "A freestyle swimmer doing the front crawl using Three.js (single HTML file)"（用 Three.js 做一个自由泳泳者，单个 HTML 文件）（[@AI_Screening][swimmer]）——括号里同时交代了渲染器和文件数。
- "build 3d cycle riding cow using three.js"（用 three.js 做一个骑牛的 3D 自行车）（[@TimJayas][cow]）——十一个词、一次生成，后来的帖子里这个成果还压过了 Grok 4.7。
- "build an interactive 3D webpage where you can pour beer into a glass"（做一个可交互的 3D 网页，能把啤酒倒进杯子）（[@HIX_AI_][beer]）——交互和文件一起点名。
- 当格式本身就是规格时，更短也行："640x360 pixel art of cheetah running (thats the whole prompt)"（640x360 像素画风的奔跑猎豹，这就是全部提示词）（[@duke_mv][cheetah]）。

## 2. 要爆炸视图或剖面

Carbon 在本合集中的招牌作品，是可以被拆开的物体。作者反复用同一组动词——X-ray（透视）、cut in half（切开）、explode（炸开）、lay out（逐件摆开）——因为模型把它们当成场景状态，而不是滤镜：

- "a café racer you can X-ray, cut in half, explode and lay out part by part"（一辆可以透视、切开、炸开并逐件摆开的咖啡骑士摩托）（[@dromexa][bike]）——每个模型各一次生成；作者的结论是 Carbon 的车"像是从真正的车间里推出来的"。
- "a mechanical watch you can X-ray, cut in half, explode and lay out part by part"（同样写法的第二轮，换成机械表）（[@dromexa][watch]）——"摆轮真的在走，每个齿轮转速都对"。
- "a robotic eye that blinks, focuses, then explodes into every part"（一只会眨眼、对焦，然后炸成所有零件的机械眼）（[@noclipepe][eye]）——单次 30 分钟。
- "a robotic great white I can take apart piece by piece"（一条我可以逐件拆开的机械大白鲨）（[@0xPorterio][shark]）——这场对比是 Opus 靠内部结构赢的，何时要追问见 §6。
- "an animated cutaway of an airplane engine"（飞机发动机的动画剖面）（[@olezhavich][engine]）——九缸星形发动机，"四个模型的机械都做对了（我核过点火顺序）"。
- "a cartoon liner that sails, splits open and shows life on every deck"（一艘卡通邮轮，先航行、再裂开、展示每一层甲板上的生活）（[@olezhavich][ship]）——切开本身就是动画的一段，而不是一个模式。

这个写法之所以有效，是因为它一条提示词给出三个场景：完整的物体、分离的过程、标注好的零件。三个都写上，并说清炸开时什么还要保持运转（走动着的摆轮、点火着的活塞）。

## 3. 写清阵容、道具和结局

这里传播最广的帖子读起来像舞台指令：N 个角色、M 个真能用的道具、一个写死的结尾。这些数字就是考点——每个模型都在同一组数字上见分晓：

- "9 capybaras in a hot spring, 6 tools that all have to work, and a finale where a baby capybara floats up in a bubble and plops back into the water"（温泉里 9 只水豚、6 件都必须能用的工具，以及结局：一只小水豚坐在泡泡里浮上来、扑通落回水里）（[@ottollm][onsen]）——"Opus 读懂了需求，Carbon 造出了温泉"。
- "9 tiny troublemakers, a dock full of tools, and one of them has to pop at the end"（9 个小捣蛋、一码头工具，最后必须有一个爆开）（[@0xPorterio][troublemakers]）。
- "a zombie hand claws out of a grave and rots down to the bone"（一只僵尸手从坟里抓出来、一路腐烂到骨头）（[@noclipepe][zombie]）——结局是页面必须自己到达的第二种状态。
- "rainbow jelly you can cut, nail and torch"（可以切、钉、烧的彩虹软糖）（[@0xRhinoX][jelly]），以及续作 "a rainbow jelly pumpkin you can carve and light up"（可以刻、可以点亮的彩虹软糖南瓜）（[@0xRhinoX][pumpkin]）——每个动词都需要一段不同的物理。

阵容清单也让对比更好看：Carbon 把九只水豚摊满了整个温泉，而 Opus 把它们挤成"中间一坨毛茸茸的交通堵塞"——是数量让差异一眼可见。

## 4. 说清镜头要捕捉什么

这些帖子是视频，所以提示词必须产出一个能自己表演的页面——不靠鼠标、没有第二次机会：

- 自动播放的序列或定长循环，让录屏能一次收全。"make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out"（做一段 15 秒的动态动效视频，展示你作为动效设计师有多强，就当是你的求职 showreel，全力以赴）（[@leo114119][showreel]）把时长写进了提示词；"Create a professional motion graphics 30 seconds"（做一段 30 秒的专业动效）（[@Genysis_Ai_26][thirty]）同理。
- 有时间线的变化：先眨眼再炸开（[机械眼][eye]）、先航行再裂开（[邮轮][ship]）、先抓出再腐烂（[僵尸手][zombie]）。
- 在小屏上也站得住的细节：邮轮那条说 Carbon "在手机上也看得清"（[@olezhavich][ship]），孔雀那场是在信息流尺寸下评的"动画"和"写实"（[@srikanthvaluri][peacock]）。这里预览图宽 400 px——细线条和小字会消失。
- SVG 要的是连续运动："behold superman in continuous animation in different art style"（看超人以不同画风连续动下去）（[@Inmerson][superman]）；以及自行车骑牛 SVG，"每个细节都完美同步在同一运动里"（[@TimJayas][svg]）。

## 5. 一次生成就是一次生成——写明白

这个合集之所以成立，是因为作者把同一段文字同时喂给两个或更多模型、不做修补。帖子里把这点写明，因为它本身就是论点的一部分：

- "same prompt, one shot each"（同一提示词，各一次生成）（[@dromexa][bike]、[@Haleeeemahh][oneshot]）。
- "same prompt, one shot, no testing, no second tries"（同一提示词，一次生成，不测试，不重来）（[@ottollm][onsen]）。
- "same prompt, both low effort"（同一提示词，两边都低强度）（[@ValencianaAbel][trex]）。
- "same prompt, 4 models"（同一提示词，四个模型）（[@srikanthvaluri][peacock]）；"I gave four models a 9-cylinder radial engine… one try each"（给四个模型同一台 9 缸星形发动机……各试一次）（[@olezhavich][engine]）。

要做公平的对决，就把模型以外的一切固定：同一提示词、同一强度、各跑一次，再用同样方式录下两个页面。要的不是公平测试而是最好看的页面，就迭代——一位作者展示了同一个城堡场景三条追问之后，火从"9 个橙色方块"变成"几乎能感受到温度"（[@semichenkko][dragon]）："差距不在模型，在追问。"

## 6. 定好预算，检查内部

Carbon 是旗舰定价——SandBase 上每百万输入 token $4、输出 $20——而这些页面跑得久。本合集报告的竞技场运行一次 $3.20 到 $14、24 到 85 分钟。按这个做预算：

- `max_tokens` 就是全部预算：思考始终开启并占用它，API 输出上限 65,536 token。页面被截断，token 照样计费。一次生成的页面给满上限。
- 长单文件在这里是常态——鲨鱼对比里注明 Opus 在同一 29 秒窗口内写了"1,634 个零件，全部是代码写出来的"（[@0xPorterio][shark]）。
- 那条鲨鱼帖的教训：Carbon "赢了速度和特效"，而 Opus "赢下了你真正能看到的内部"——77 比 90。如果需求是机械深度，就写清里面必须有什么（零件数、关节、标注的系统），而不只是"会炸开"。
- 走 record.mjs 路线时，让页面铺满视口、无需输入即可运行（§4），然后照[教程](tutorial.md#4-把页面录成视频)操作。

## 可以直接用的提示词

```text
把 [主题] 做成一个从磁盘直接打开就能跑的独立 HTML 文件。

场景：[阵容——N 个角色/物体，各自在做什么]，[环境、光照、氛围]。
交互：[动词：环绕、透视、切开、炸开、喂食、雕刻……]——每个操作都必须能用。
结局：[页面自己到达的状态：爆开、裂开、腐烂]。
运动：加载后自动播放一段 [10–30] 秒的序列，然后循环，不需要输入。

技术：
- 用 CDN import map 以 ES module 引入 Three.js，不要其他库。
- 不要外部图片、字体、音频：贴图用代码生成。
- 铺满视口、不出现滚动条、笔记本上 60 fps、缩到 400 px 宽仍可读。
- 完成前自检：页面加载零 console 错误，每个操作都可用。
- 只返回完整的 HTML，从 <!DOCTYPE html> 到 </html>，不要省略。
```

可以到 [Lab 文本竞技场][arena] 里，把这段同时跑在 Carbon 和其他模型上对比；用 API 的方式见[教程](tutorial.md)。

## 参数设置

- **输出预算。** 思考始终开启并占用 `max_tokens`，API 上限 65,536。本合集里的一次生成页面在竞技场跑了 24–85 分钟；`max_tokens` 给到 65,536，避免页面写到一半被截断。
- **没有 reasoning_effort。** API 没有这个旋钮——`sandbase inspect google/gemini-4-argon` 只列出 `max_tokens`、`temperature`、`top_p`、`stop`、`seed` 和工具/响应字段。强度由模型自己选（描述里写 low、medium 或 high）。对比帖里说的 "low effort" 是竞技场一侧的设置，不是你能在 API 里传的。
- **花费。** 每百万输入 token $4、每百万输出 token $20，缓存命中输入按 0.05 倍计，推理按输出计费。作者实际花了多少见[模型对比](model-comparison.md)。

---

引文均为短摘录并注明作者，完整提示词和视频请点链接。外文原文的翻译为我们所做。

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
