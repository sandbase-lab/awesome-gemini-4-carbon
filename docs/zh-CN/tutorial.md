# Gemini 4 Carbon 教程：从提示词到视频

[English](../tutorial.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

四步把提示词变成 MP4。Carbon 写网页，你来播放并录制。

## 1. 从喜欢的视频开始

在[合集](../../README.zh-CN.md)里点任意标题，进入它在 [SandBase Lab][lab] 的页面：视频、原帖，以及作者公开的提示词（如果有）。点 **复刻**，Lab 会打开文本竞技场，自动填好帖子内容并选中 Gemini 4 Carbon。登录后运行，就能拿到 HTML，并带实时预览。

作者没有公开提示词？照[提示词写法](prompt-guide.md)自己写一条，里面有填空模板。

## 2. 用同一个提示词对比模型

这个合集就是在对比中建起来的——98 条视频里有 39 条是同提示词对决，大多对手是 Claude Opus 5.5。自己跑一场：在[文本竞技场][arena]里，在 Carbon 旁边再加一两个模型（例如 `anthropic/claude-opus-5.5`、`openai/gpt-6-astra` 或 `deepseek/deepseek-v4.1-flash`），跑一次。所有模型拿到同样的文字，每个结果都显示花费和耗时。这是在你自己任务上验证[对比页](model-comparison.md)结论的最快方式——同一提示词、各一次生成，然后用同样的方式录下两个页面。

## 3. 或者直接调用 API

Gemini 4 Carbon 在 SandBase 上的模型 ID 是 `google/gemini-4-argon`，兼容 OpenAI——Carbon 检查点通过 Argon 的模型 ID 提供。

1. 在[控制台][keys]创建 Key 并导出：`export SANDBASE_API_KEY=sk-sb-...`
2. 把提示词保存为 `prompt.txt`。
3. 运行：

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

- `max_tokens: 65536`：这个模型的思考始终开启，隐藏的推理 token 也占用同一份额度。本合集中的页面都是长单文件——一场可比的四个模型对决里，对手用代码写了 1,634 个零件（[@0xPorterio][shark]）——而 65,536 是 API 接受的输出上限。额度给小了，你会拿到被截断的页面，而且照样为这些 token 付费。
- `--max-time 900`：长页面要跑好几分钟，本合集报告的竞技场运行每页 24 到 85 分钟。
- `sed '/^```/d'` 去掉模型可能加上的 Markdown 代码围栏。
- `usage` 显示计费的 token，包括推理部分。推理按输出价（每百万 $20）计费，输入每百万 $4，缓存命中的输入按 0.05 倍计；价格见[模型页][model]。
- 这个模型没有 `reasoning_effort` 参数——API 只接受 `max_tokens`、`temperature`、`top_p`、`stop`、`seed` 和工具/响应字段，强度由模型自己决定。帖子里写的 "low effort" 是竞技场一侧的设置。
- 图片、视频、音频和 PDF 都能作为输入：这个模型是多模态的，可以把参考帧或片段放进 `messages[].content`，而不用费劲描述。

用浏览器打开 `gemini-carbon.html`。如果一片空白，打开开发者工具：常见原因是被截断的文件（加大 `max_tokens`）或 CDN 没加载（要求所有资源内联）。如果场景能跑但某个操作没反应，接着查交互——这里的帖子是按"每件工具是否都能用"来评页面的，不只看渲染。

### 用 SandBase CLI

同一个调用也可以走 [SandBase CLI](https://www.npmjs.com/package/@sandbaseai/cli)，它同样读取 `SANDBASE_API_KEY`：

```bash
npx -y @sandbaseai/cli@latest inspect google/gemini-4-argon   # 输入字段和价格，免费
jq -n --rawfile prompt prompt.txt '{max_tokens: 65536, messages: [{role: "user", content: $prompt}]}' > input.json
npx -y @sandbaseai/cli@latest run sandbase_google_gemini_4_argon -f input.json --timeout 900 -o result.json
```

`-o result.json` 保存响应；页面在 assistant 消息里，和 API 一样。

## 4. 把页面录成视频

大多数作者是直接录屏——对比帖会把两个页面按同样的时长并排录。想每次得到一样的片段，可以用 [`scripts/record.mjs`](../../scripts/record.mjs) 无头录制：

```bash
npm i -D playwright@1.56.1
npx playwright install chromium          # 或使用本机 Chrome：export RECORD_CHANNEL=chrome
node scripts/record.mjs gemini-carbon.html gemini-carbon.mp4 12 1920 1080   # 12 秒，1080p
```

它按你给的尺寸打开页面，录指定秒数，再用 ffmpeg 转成 H.264 MP4。想要干净的效果，就在提示词里要求自动播放的序列或定长循环（见[提示词写法 §4](prompt-guide.md#4-说清镜头要捕捉什么)），让整个画面不依赖鼠标。

想要声音？录制本身只有画面，音频在剪辑里加——或者在提示词里要求用 Web Audio 出声，录制时捕获标签页音频，而不是麦克风。

这个列表里很多视频是竞技场会话的产物，而不是一次 API 调用；也有作者迭代过：三条追问把同一个城堡场景的火从"9 个橙色方块"做到"几乎能感受到温度"（[@semichenkko][dragon]）。

## 安全运行生成的代码

这段 HTML 是你没读过的代码。单文件页面从本地打开通常没问题，但它仍然可以加载脚本、发起网络请求。对于不完全信任的内容，或者要批量运行很多页面，请使用 [SandBase Sandbox][sandbox]：一个有时限、接触不到你的文件和 Key 的隔离环境。

## 分享

把视频发到 X，附上提示词并 @ Gemini 4 Carbon。想被收录，就[提交给我们](https://github.com/sandbase-lab/awesome-gemini-4-carbon/issues/new?template=submit-video.yml)；通过后会先进入 Lab 合集，下一次每日同步时出现在本列表。

[lab]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[arena]: https://www.sandbase.ai/lab/x/llm-arena?models=google%2Fgemini-4-argon&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[keys]: https://www.sandbase.ai/console/keys?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[model]: https://www.sandbase.ai/model/google/gemini-4-argon?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[sandbox]: https://www.sandbase.ai/landing/sandbox?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[shark]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116548548334321967?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
[dragon]: https://www.sandbase.ai/lab/ai-videos/gemini-4-carbon/2116198626187706722?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-carbon
