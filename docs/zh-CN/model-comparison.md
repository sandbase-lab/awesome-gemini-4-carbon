# Gemini 4 Carbon 对比 Claude Opus 5.5、GPT-6 Astra 和 Gemini 4 Argon

[English](../model-comparison.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

两类证据，分开呈现：

1. **我们测到的。** Lab [Evals 榜单][evals] 展示 Artificial Analysis 的数据；Lab [Pelican Test][pelican] 用同一份固定提示词跑每个模型并给结果打分。样本不大，但所有人的条件一致。
2. **创作者报告的。** 发在 X 上的同提示词对比，附他们自己的花费和耗时。有参考价值，但我们没有验证。

有一个命名问题贯穿两类证据：Carbon 是 Gemini 4 的最新检查点，最初在竞技场里以代号 "Gemini 4 Argon" 出现。Artificial Analysis 把两个检查点列为两个模型，本合集里也有好几位作者拿 Carbon 对比 Argon 本人。在 SandBase 上，Carbon 检查点通过同一个 ID 提供——`google/gemini-4-argon`——所以 Lab Pelican Test 里这个 ID 的那一行就是本列表的实测行。

## 我们测到的：Lab Evals 榜单

榜单读取的是 **2026-10-29** 的 Artificial Analysis 快照（智能指数第 5 版，716 个模型）。榜单按推理强度分行；本次快照的语言模型榜只有三项指标——没有编码榜和智能体榜。

| 模型（榜单上的行） | [智能指数][b-intel] | [输出速度][b-speed] | [单任务成本][b-cost] |
|---|---|---|---|
| **Gemini 4 Carbon (High)** | **59.4（第 1）** | **102 tok/s（373 中第 172）** | **$7.76（73 中第 67）** |
| Claude Opus 5.5 (Max) | 58.4（第 2） | 98 tok/s（第 182） | $10.04（第 71） |
| GPT-6 Astra (Max) | 56.9（第 4） | 76 tok/s（第 245） | $6.24（第 61） |
| GPT-6.1 Sol (Max) | 54.5（第 7） | 81 tok/s（第 231） | $1.27（第 34） |
| Gemini 4 Argon (High) | 50.4（第 13） | 82 tok/s（第 228） | $7.68（第 66） |
| Kimi K3.1 Pro | 46.0（第 22） | 37 tok/s（第 353） | $3.68（第 53） |
| Claude Haiku 5.5 (Max) | 36.2（第 32） | 241 tok/s（第 21） | $0.41（第 23） |
| DeepSeek V4.1 Flash 1017 (Max) | 32.5（第 39） | 182 tok/s（第 57） | $0.60（第 28） |

这说明什么、不说明什么：

- **Carbon 拿下了头条榜单。** 59.4 比 Opus 5.5 Max 高一分，比它自己的上一检查点（Argon，50.4）高九分。这是本列表里唯一与创作者"新王登基"说法相符的实测证据——但它也只是一套基准、一个强度档位，不代表所有任务。
- **价格和速度也是旗舰档。** 单任务 $7.76 让 Carbon 与 Argon（$7.68）、Opus 5.5 Max（$10.04）同处榜单最贵的一端——flash 档对手每任务便宜 10–20 倍（DeepSeek V4.1 Flash 1017 为 $0.60，Haiku 5.5 为 $0.41）。速度上 102 tok/s 居中，快于 Argon（82）和 Astra（76），远慢于 flash 模型（Haiku 241、DeepSeek 182）。
- **榜单测的是推理，不是渲染。** 这里没有一项指标在给 Three.js 场景或 SVG 打分。下文的视觉结论全部来自创作者。

## 我们测到的：Lab Pelican Test

[Pelican Test][pelican] 让每个模型画一只骑自行车的鹈鹕，一次静态、一次动画（轮子转、腿蹬踏板，只用 CSS/SMIL）。页面渲染成 PNG，由一个 LLM 裁判按四个问题打 0–5 分：能认出是鹈鹕、真的在骑、自行车结构成立、好看。成本是 SandBase 上的实际计费金额。

2026-11-01 读取的[实时榜单][pelican]（22 个模型）：

| 排名 | 模型 | 结果数 | 得分 | 成功渲染 | 动画有效 | 平均成本 |
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

这说明什么：

- **Argon 这个 ID 占着榜首——3.81，当前 SOTA。** 它是 Carbon 检查点在 SandBase 上实际运行的 ID；但这 4 条计分结果记录在 10 月 14–20 日之间，早于 Artificial Analysis 在 10 月 28 日把 Carbon 检查点单列。所以 3.81 应读作"Gemini 4 旗舰的鹈鹕"，而不是 Carbon 专属的分数。
- **四张图、两位测试者。** 样本很小，[自己跑一次][pelican-run] 就能加数据。
- **价格也符合旗舰定位。** 每张约 $0.12，约为 DeepSeek 鹈鹕的 7 倍、Haiku 的 20 倍、Opus 5.5 的六成。

## 创作者报告的

发在 X 上的同提示词对比。本合集大部分就是对比——98 条里 39 条——对手通常是 Claude Opus 5.5，其余是 GPT-6 Astra、Gemini 4 Argon、Grok 和 Fable。数字按创作者自述，来自竞技场或 Antigravity 运行，往往只跑一次。点进链接可以两边一起看。

| 创作者 | 任务 | Carbon | 对手 | 创作者结论 |
|---|---|---|---|---|
| [@0xRhinoX][jelly] | 可以切、钉、烧的彩虹软糖 | $4.30，32 分钟 | Opus 5.5：$14.00，1 小时 20 分 | "便宜 3 倍，快 2 倍，发布才 1 天"——Carbon 的软糖把彩虹影子投到桌上，Opus "发白" |
| [@0xRhinoX][pumpkin] | 可以刻、可以点亮的彩虹软糖南瓜 | $3.20，31 分钟 | Opus 5.5：$28.73，1 小时 50 分 | "便宜 9 倍，快 3 倍" |
| [@0xPorterio][troublemakers] | 9 个小捣蛋、工具码头、结局一个爆开 | $4.10，34 分钟 | Opus 5.5：$12.80，1 小时 12 分 | "Carbon 看起来真的好……Opus 更有生气" |
| [@noclipepe][zombie] | 僵尸手抓出坟墓、腐烂到骨头 | 1 小时 23 分，$10.20 | Opus 5.5：1 小时 6 分，$8.10 · GPT-6 Astra：24 分，$5.70 | "Carbon 直接上了恐怖片……Astra 做了一个放着一只手的落地页" |
| [@noclipepe][dino] | Chrome 小恐龙游戏 | 34 分 41 秒，$5.20 | Opus 5.5：38 分 55 秒，$8.53 · Astra：15 分，$4.61 · GPT-6.1 Terra：4 分，$0.17 | "Carbon 连翼龙的飞行动画都做了" |
| [@noclipepe][eye-test] | 机械眼：眨眼、对焦、炸开 | 29 分 49 秒 | Opus 5.5：43 分 21 秒，$9.25 · Astra：22 分 54 秒，$3.28 | "Gemini 让其他模型看起来老了" |
| [@dromexa][bike] | 可透视、切开、炸开的咖啡骑士摩托 | 各一次生成 | Opus 5.5 | "Carbon 的车像是从真正的车间推出来的……3D 上 Carbon 刚夺走王冠" |
| [@dromexa][watch] | 同一提示词，换成机械表 | 各一次生成 | Opus 5.5 | "摆轮真的在走……2 比 0，Carbon 是当下的 3D 之王" |
| [@0xPorterio][shark] | 机械大白鲨，逐件拆开 | "建得最快……特效最炫" | Opus 5.5：1,634 个代码写成的零件、球节脊柱、泵动的液压杆 | "Gemini 赢了速度和特效，Opus 赢下了你真正能看到的内部。总分 77 比 90"——判给 Opus |
| [@olezhavich][engine] | 9 缸星形发动机剖面，四款模型 | "干净利落……最精致" | Opus 5.5：进气歧管绕进每个气缸、排气管、编号缸盖——"工程奖给它" · Argon：最有氛围但不够锐利 · Sol：干净但火苗太小太暗 | 各有所长——精致对工程 |
| [@olezhavich][ship] | 卡通邮轮剖面，三款模型 | "每个房间有自己的颜色……在手机上也看得清" | Fable 5.1：燃料舱、轮机控制室、锚链——"最真实的一艘" · Astra：苍白、最平 | "我会研究 Fable，但登上 Carbon" |
| [@ottollm][onsen] | 9 只水豚、6 件可用工具、泡泡结局 | 九只摊满整个温泉，各做各的 | Opus 5.5："挤成中间一坨毛茸茸的交通堵塞" | "Opus 读懂了需求，Carbon 造出了温泉"——这里最挺 Carbon 的一条 |
| [@TimJayas][cow-vs] | Three.js 自行车骑牛 | — | Grok 4.7："牛看起来像刚从火星来的" | 判给 Carbon |
| [@TimJayas][cow] | 同一场景，单独跑 | "3D 产出相当惊人" | （发问：这是 Opus 5.5 的水平吗？） | — |
| [@srikanthvaluri][peacock] | 机械印度孔雀，四款模型 | "最真实" | Opus 5.5：动画最好 · Astra：干净但苍白 · Sol：细节更少 | "Carbon 是我的赢家" |
| [@ValencianaAbel][trex] | Three.js 奔跑霸王龙，两边都低强度 | "像是做出来的实物" | Opus 5.5："还像个玩具" | 判给 Carbon |
| [@keydol123][haunted] | "做一个闹鬼的房子网站" | "真的闹鬼" | Opus 5.5："做成了可爱风" | 让观众选 |
| [@leo114119][showreel] | 15 秒动效 showreel | 效果更好 | Opus 5.5 | "在 Opus 曾经最有优势的地方，实实在在超越了" |
| [@leo114119][oxford] | Three.js 可交互牛津 3D 城市 | 每栋建筑细节明显更多，阳光效果更好 | Fable 5.1 High | 判给 Carbon |
| [@olezhavich][football] | 等距街头足球场，三款模型 | "最有生气的场景……氛围最好" | Kimi K3.1：结构剖面感，整体打磨更少 · Grok 4.6：最干净也最空 | "这场我选 Gemini 4 Carbon" |
| [@Haleeeemahh][oneshot] | 同一提示词，各一次生成 | — | Opus 5.5 (High) | "Google 是放出了一个 Opus 5.5 级的模型吗？" |
| [@marcthecreatorr][ps5] | PS5 手柄 SVG；Opus 在 Claude Code 里开 xhigh | 用的是"较早的 Carbon 检查点" | Opus 5.5 | "很难判"——并指出 Opus 在 SVG 上一直很难被打败 |
| [@blueemi99][opus-win] | 同一提示词跑在竞技场 "Gemini 4（可能是 carbon）"和 Opus 5.5 | — | Opus 5.5 | "Gemini 这边不太行，Opus 好一百倍"——最反 Carbon 的一条 |

对它自己的上一检查点，创作者大多、但不是一致地选 Carbon：

- [@leo114119][pelican-svg] 用鹈鹕骑车 SVG 一次生成对比两款："Carbon 在所有细节上都比 Argon 上了一个等级；Argon 在色彩和动态交互上更活泼"。
- [@abhinavflac][voxel] 评 voxelbench："我见过这个提示词下最惊艳的输出……比 Argon 慢 2–3 倍，但视觉质量的飞跃完全值得"。
- [@Adidotdev][macro] 两款各一次生成：Carbon 在竞技场约 4 分钟，Argon 在 Antigravity 约 10 分钟——"Carbon 在 4 分钟内加了大量宏观交互"。
- [@Inmerson][superman] 把超人多元宇宙动画左右分屏，左 Carbon 右 Argon。
- [@glitch_catAI][argon-win] 唱反调："同一提示词，argon >>> carbon"。
- [@pankajkumar_dev][temple] 做了体素风的日本寺庙山谷："明显好过 Gemini 4 Argon……是清楚的代际提升"。
- [@pankajkumar_dev][lantern] 评灯笼河夜景："Carbon-H 在设计质量上可以和 Opus 5.5 相比"。

没有对手的单次运行和质量评价：

- [@duke_mv][cheetah-solo] 评 640×360 像素猎豹："到目前为止所有前沿模型里，我用这个提示词拿到的最好结果"。
- [@DrstaOne][motorbike] 评摩托骑鹈鹕 SVG："Gemini 4 Carbon 在 SVG 上杀疯了"。
- [@Genysis_Ai_26][thirty] 评 30 秒 showreel："好得离谱……考虑到只是第一个检查点，能掀翻 Opus 5.5"。
- [@semichenkko][dragon] 对同一个城堡场景迭代了四轮：火从"9 个橙色方块"变成"几乎能感受到温度"——"差距不在模型，在追问"。

两类来源合起来的规律：实测榜单和多数创作者都认为 Carbon 是第一梯队——智能指数第 1、Pelican 在其运行 ID 下第 1，并且在有纵深和细节的 3D 场景上是人气最高的选择。分歧也很一致：Opus 仍在内部工程结构上赢（鲨鱼的代码零件、发动机的管路）以及动画的"活"感；Carbon 一页要花旗舰的钱和旗舰的时间；也有少数帖子在同一提示词下就是更喜欢 Argon 或 Opus。发布那一周竞技场的检查点路由也不稳定——[@marcthecreatorr][ps5] 说他拿到的 Carbon 输出其实是更早的检查点，[@blueemi99][opus-win] 也不确定跑的到底是哪个 Gemini。

## 重跑一次再相信对比

设置一变结果就变：竞技场、Antigravity 还是 API；竞技场当天实际给的是哪个检查点；强度档位；作者有没有修补输出。这里好几条帖子正是在这一点上留了余地（[@marcthecreatorr][ps5]、[@olezhavich][football]、[@blueemi99][opus-win]）。自己跑一遍：把提示词粘到 [Lab 文本竞技场][arena]，选两三个模型；或者按[教程](tutorial.md)用 API。

## 更多实测

- [Lab Evals 榜单][evals]——Artificial Analysis 数据，2026-10-29 快照。
- [Lab Pelican Test][pelican]——同一提示词、同一评分方式，画作直接展示。
- [SandBase Lab 上的全部 AI 视频合集][collections]——其他模型的同类列表。

---

Lab 数据：[Evals 榜单][evals]（Artificial Analysis，2026-10-29 快照）与 [Pelican Test][pelican]（2026-11-01 读取）。创作者数据：他们本人的帖子，已附链接，未经我们独立验证。

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
