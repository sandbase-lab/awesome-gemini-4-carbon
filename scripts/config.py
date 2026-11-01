"""Every model-specific value for this list. The other scripts are generic and read from here."""
import os

ORIGIN = os.environ.get('LAB_ORIGIN', 'https://www.sandbase.ai').rstrip('/')
SITE = 'https://www.sandbase.ai'  # public links in READMEs and docs always use the canonical host

SLUG = 'gemini-4-carbon'
REPO = 'sandbase-lab/awesome-gemini-4-carbon'

CFG = dict(
    slug=SLUG,
    name='Gemini 4 Carbon',
    short='Carbon',  # how the prose refers to the model after the first mention
    vendor='Google',
    model_id='google/gemini-4-argon',
    kind='code',  # this is a code model: the README Recreate section uses the chat-completions curl
    repo=REPO,
    repo_url=f'https://github.com/{REPO}',
    campaign='awesome-gemini-4-carbon',
    lab_collection=f'{SITE}/lab/ai-videos/{SLUG}',
    lab_data=f'{ORIGIN}/lab/data/ai-videos/{SLUG}.json',
    media_prefix=f'{SITE}/lab/media/x/{SLUG}/',
    model_page=f'{SITE}/model/google/gemini-4-argon',
    arena=f'{SITE}/lab/x/llm-arena?models=google%2Fgemini-4-argon',
    evals=f'{SITE}/lab/evals',
    pelican=f'{SITE}/lab/pelican-test',
    keys=f'{SITE}/console/keys',
    sandbox=f'{SITE}/landing/sandbox',
    lab_home=f'{SITE}/lab/',
    all_collections=f'{SITE}/lab/ai-videos',
    user_agent=f'awesome-gemini-4-carbon-sync/1.0 (+https://github.com/{REPO})',
    html_out='gemini-carbon.html',
    # Output limit for the curl example. Thinking is always on for this model and the hidden
    # reasoning tokens come out of max_tokens. `sandbase inspect google/gemini-4-argon --json`
    # accepts up to 65,536 output tokens, and the pages in this list are long one-shot HTML
    # files, so the example asks for the full budget rather than risk a truncated page.
    max_tokens=65536,
    max_tokens_limit=65536,
    context_length=1048576,
    guide_patterns=6,  # numbered sections in docs/prompt-guide.md
    banner_title='Awesome Gemini 4 Carbon',
    banner_sub='Videos · prompts · tutorial · model comparison',
    # Finished pieces only on the banner: no comparisons or other models' names. 'gemini'
    # and 'carbon' stay off the list — they are this model's own name, and clean posters
    # legitimately carry them.
    banner_skip=('vs', 'versus', 'comparison', 'compar', 'benchmark', 'test', 'opus', 'claude',
                 'sonnet', 'haiku', 'fable', 'gpt', 'deepseek', 'kimi', 'qwen', 'glm', 'minimax',
                 'grok', 'muse'),
    not_affiliated={'en': 'Not affiliated with or endorsed by Google.', 'zh-CN': '与 Google 无隶属或背书关系。'},
    # No SandBase blog post on this model existed when the list shipped. build_readme.py
    # skips the reading section while this is empty — do not invent links here.
    reading=[],
)

# README and prompt-index copy. Placeholders in {braces} are filled by build_readme.py
# ({name}, {short}, {model_id}, {html_out}, links such as {lab_stats} or {model_page}, counts {n}/{a}/{p}).
# Every fact here is sourced: `sandbase inspect google/gemini-4-argon`, the Lab collection's
# own posts (linked), the Lab Pelican Test leaderboard (read 2026-11-01), and the Lab Evals
# boards (Artificial Analysis snapshot 2026-10-29).
COPY = {
    'en': {
        'switch': 'English · [简体中文](README.zh-CN.md)',
        'tagline': 'A curated list of **Gemini 4 Carbon examples**: videos, prompts and demos made with Gemini 4 Carbon, the newest Gemini 4 checkpoint from Google — tested in the Arena under the codename Gemini 4 Argon and served on SandBase as `google/gemini-4-argon`. Interactive Three.js 3D scenes, cutaways and explode-view models, SVG and canvas animation, motion graphics showreels and product pages, most of them written as one self-contained HTML file from a prompt, each one credited to its creator and linked to the original post.',
        'alt': 'Awesome Gemini 4 Carbon: videos, prompts, tutorial and model comparison',
        'stats': '**{n} videos** from **{a} creators** · **{p}** with the creator\'s prompt · synced daily from [SandBase Lab]({lab_stats})',
        'start': 'Start here',
        'start_rows': [
            ('Watch the videos', '[Browse by category](#contents) below, or [play them full-size on SandBase Lab]({lab_quickstart})'),
            ('Copy a prompt', '[Prompt index](docs/prompts.md): every video that comes with its prompt'),
            ('Write your own prompt', '[Prompt guide](docs/prompt-guide.md): {guide_patterns} patterns and a fill-in template'),
            ('Make a video', '[Tutorial](docs/tutorial.md): prompt → HTML → MP4, with the API, the CLI and a recording script'),
            ('Pick a model', '[Gemini 4 Carbon vs. Claude Opus 5.5, GPT-6 Astra and Gemini 4 Argon](docs/model-comparison.md)'),
            ('Try it now', '[Run Gemini 4 Carbon in the Lab arena]({arena_quickstart}), next to other models'),
        ],
        'goal': 'I want to…', 'where': 'Go to',
        'how': 'Click a preview to play the video. Click a title for the post, the prompt and **Recreate** on SandBase Lab. **@handle** links to the creator\'s post on X.',
        'contents': 'Contents',
        'featured': 'Featured',
        'show_all': 'Show all {n}',
        'recreate': 'Recreate a video with {name}',
        'recreate_body': [
            'Every video page on [SandBase Lab]({lab_recreate}) has a **Recreate** button: it sends the post to {short} in the Lab text arena and returns the code, ready to play in the browser.',
            '',
            'With the API, {name} is `{model_id}` on SandBase (OpenAI-compatible) — the Carbon checkpoint is served under the Argon id. Put a prompt in `prompt.txt`, create a key in the [console]({keys}), and run:',
        ],
        'recreate_after': 'Open `{html_out}` in a browser, or run it in a [SandBase Sandbox]({sandbox}) to keep generated code isolated. Thinking is always on for this model, and the hidden reasoning tokens come out of `max_tokens`, so the call above asks for the full 65,536 the API accepts. Full walkthrough: [tutorial](docs/tutorial.md). Pricing: [model page]({model_page}).',
        'prompt_tag': 'prompt',
        'more': '**[See all {n} on SandBase Lab →]({lab_section})**',
        'faq': 'FAQ',
        'faq_items': [
            ('What is Gemini 4 Carbon?', 'Gemini 4 Carbon is the newest checkpoint of Gemini 4 Argon, Google\'s flagship reasoning model and the first of the Gemini 4 generation, generally available since October 13, 2026. Creators first met it in the Arena under the codename "Gemini 4 Argon"; the newer checkpoint showed up days later and the community named it Carbon. It accepts text, image, video, audio and PDF input, has a 1,048,576-token context window and up to 65,536 output tokens, always reasons before answering (low, medium or high effort), and supports function calling and structured output. On SandBase the Carbon checkpoint is served under the same id: `{model_id}`. Source: `sandbase inspect google/gemini-4-argon`.'),
            ('How are these Gemini 4 Carbon videos made?', 'The model doesn\'t render video. It writes a web page (HTML with Three.js, Canvas or SVG), and the creator records the page playing. Most posts here are Arena runs — creators tested the Carbon checkpoint against Opus 5.5, GPT-6 Astra or Argon itself, one shot each, then recorded both pages side by side. See the [tutorial](docs/tutorial.md).'),
            ('Where do I find the prompt for a video?', 'Videos tagged **prompt** come with the creator\'s prompt on their Lab page. The [prompt index](docs/prompts.md) lists all of them.'),
            ('How do I write a good Gemini 4 Carbon prompt?', 'Name one self-contained HTML file and the renderer you want (Three.js, Canvas or SVG), describe the scene, the interactions and the state a recording should catch, ban external assets, and ask it to test its own page. Leave a large `max_tokens`: thinking is always on and shares that budget. Details and a template: [prompt guide](docs/prompt-guide.md).'),
            ('How do I use the Gemini 4 Carbon API?', 'On SandBase the model id is `{model_id}` on the OpenAI-compatible `/v1/chat/completions` endpoint — the Carbon checkpoint is served under the Argon id. One key works for every model. There is no `reasoning_effort` parameter: the model always reasons at the effort its description picks. See [Recreate](#recreate) and the [model page]({model_page}).'),
            ('Is Gemini 4 Carbon better than Claude Opus 5.5, GPT-6 Astra or Gemini 4 Argon?', 'On the measured side, yes on the headline board: the Lab [Evals boards]({evals}) (Artificial Analysis, snapshot 2026-10-29) put Gemini 4 Carbon (High) at #1 on the Intelligence Index, 59.4 — ahead of Opus 5.5 Max (58.4), GPT-6 Astra Max (56.9) and its own previous checkpoint, Argon (50.4, #13). The Lab [Pelican Test]({pelican}) row is under `google/gemini-4-argon` — the id Carbon runs under — and it is #1 of 22 models, 3.81, at about $0.12 a drawing (read 2026-11-01). Creators agree on 3D quality but not on everything: several crowned Carbon over Opus on explode-view models and interactive scenes, one scored it 77–90 behind Opus on a mechanical shark, and Carbon costs like a flagship — reported runs run $3–$14 against cheaper flash-tier rivals. Details: [model comparison](docs/model-comparison.md).'),
            ('How much does one video cost?', 'Creators report single runs from about $3.20 (a jelly pumpkin scene) to $14 (a rainbow jelly page that Opus priced at $14 and Carbon at $4.30), with most Arena comparisons landing at $3–$10 per page and 24–85 minutes per run. The list price on SandBase is $4 per million input tokens and $20 per million output tokens, and reasoning tokens bill as output; cached input reads at 0.05x.'),
            ('Can I reuse these videos?', 'No, not by default. They belong to their creators. See [MEDIA-RIGHTS](MEDIA-RIGHTS.md).'),
        ],
        'contribute': 'Suggest a video',
        'contribute_body': 'Know a Gemini 4 Carbon creation that should be here? [Open a submission]({repo_url}/issues/new?template=submit-video.yml) with the original X post. Accepted posts are added on SandBase Lab and show up here on the next daily sync. If this list helped you, a ⭐ helps others find it.',
        'credits': 'Credits & rights',
        'credits_body': [
            'Every video, prompt and post belongs to its creator. Cards credit the author and link to the original post. The MIT license covers this repository\'s scripts only. To correct a credit or remove a video, see [MEDIA-RIGHTS](MEDIA-RIGHTS.md).',
            '{not_affiliated}',
        ],
        'footer': 'Maintained by [SandBase Lab]({lab_home}) · [All AI video collections]({all_collections})',
        'p_title': 'Gemini 4 Carbon prompts',
        'p_switch': 'English · [简体中文](zh-CN/prompts.md) · [← Back to the collection](../README.md)',
        'p_intro': '{n} Gemini 4 Carbon videos whose creators shared the prompt. Open one to read the prompt, watch the video and **Recreate** it with {short} on SandBase Lab. New to prompting {short}? Start with the [prompt guide](prompt-guide.md).',
        'p_note': 'Each entry quotes the creator\'s post as published on X, where the prompt is shared. Some creators describe the task rather than pasting the whole prompt, and some put the full text in a reply: open the post on X to read the thread. Posts keep the creator\'s language.',
        'p_watch': 'Watch',
        'p_open': 'Recreate on SandBase Lab',
    },
    'zh-CN': {
        'switch': '[English](README.md) · 简体中文',
        'tagline': '精选 **Gemini 4 Carbon 案例**合集：用 Gemini 4 Carbon（Google 最新的 Gemini 4 检查点，在竞技场里以代号 Gemini 4 Argon 测试，在 SandBase 上以 `google/gemini-4-argon` 提供）做出的视频、提示词和演示。包括可交互的 Three.js 3D 场景、剖面与爆炸视图模型、SVG 与 Canvas 动画、动效 showreel 和产品页面，大多是模型根据提示词写成的单文件网页，均注明作者并链接原帖。',
        'alt': 'Awesome Gemini 4 Carbon：视频、提示词、教程和模型对比',
        'stats': '共 **{n} 条视频**，来自 **{a} 位创作者** · **{p} 条**附作者提示词 · 每天从 [SandBase Lab]({lab_stats}) 同步',
        'start': '从这里开始',
        'start_rows': [
            ('看视频', '在下方 [按分类浏览](#contents)，或 [在 SandBase Lab 大屏播放]({lab_quickstart})'),
            ('复制提示词', '[提示词索引](docs/zh-CN/prompts.md)：所有附带提示词的视频'),
            ('自己写提示词', '[提示词写法](docs/zh-CN/prompt-guide.md)：{guide_patterns} 条写法和一个填空模板'),
            ('做一个视频', '[教程](docs/zh-CN/tutorial.md)：提示词 → HTML → MP4，含 API、CLI 调用和录屏脚本'),
            ('选模型', '[Gemini 4 Carbon 对比 Claude Opus 5.5、GPT-6 Astra 和 Gemini 4 Argon](docs/zh-CN/model-comparison.md)'),
            ('马上试试', '[在 Lab 竞技场运行 Gemini 4 Carbon]({arena_quickstart})，和其他模型并排对比'),
        ],
        'goal': '我想…', 'where': '去这里',
        'how': '点击预览图播放视频；点击标题前往 SandBase Lab 查看原帖、提示词，并一键 **复刻**；**@作者** 链接到 X 原帖。',
        'contents': '目录',
        'featured': '精选',
        'show_all': '展开全部 {n} 条',
        'recreate': '用 {name} 复刻视频',
        'recreate_body': [
            '[SandBase Lab]({lab_recreate}) 的每个视频页都有 **复刻** 按钮：在 Lab 文本竞技场把帖子内容发给 {short}，返回可在浏览器直接播放的代码。',
            '',
            '用 API 的话，{name} 在 SandBase 上的模型 ID 是 `{model_id}`（兼容 OpenAI）——Carbon 检查点通过 Argon 的 ID 提供。把提示词写进 `prompt.txt`，在 [控制台]({keys}) 创建 Key，然后运行：',
        ],
        'recreate_after': '用浏览器打开 `{html_out}`，或在 [SandBase Sandbox]({sandbox}) 中运行，让生成的代码保持隔离。这个模型的思考始终开启，隐藏的推理 token 也占用 `max_tokens`，所以上面的示例给足 API 接受的 65536。完整步骤见 [教程](docs/zh-CN/tutorial.md)，价格见 [模型页]({model_page})。',
        'prompt_tag': '提示词',
        'more': '**[在 SandBase Lab 查看全部 {n} 条 →]({lab_section})**',
        'faq': '常见问题',
        'faq_items': [
            ('Gemini 4 Carbon 是什么？', 'Gemini 4 Carbon 是 Gemini 4 Argon 的最新检查点；Argon 是 Google 的旗舰推理模型、Gemini 4 代的第一款，2026 年 10 月 13 日正式发布。创作者最先在竞技场里以代号 "Gemini 4 Argon" 见到它，几天后出现了更新的检查点，社区称之为 Carbon。它接受文本、图片、视频、音频和 PDF 输入，上下文窗口 1,048,576 token，最多输出 65,536 token；始终先推理再回答（low / medium / high 三档强度），支持函数调用和结构化输出。在 SandBase 上，Carbon 检查点通过同一个 ID 提供：`{model_id}`。来源：`sandbase inspect google/gemini-4-argon`。'),
            ('这些 Gemini 4 Carbon 视频是怎么做出来的？', '模型并不直接渲染视频。它写出一个网页（用 Three.js、Canvas 或 SVG 的 HTML），作者再把页面播放过程录下来。这里的帖子大多是竞技场运行——作者让 Carbon 检查点与 Opus 5.5、GPT-6 Astra 或 Argon 本人同题各跑一次，然后把两个页面并排录下。见 [教程](docs/zh-CN/tutorial.md)。'),
            ('在哪里找到视频的提示词？', '标有 **提示词** 的视频，其 Lab 页面上有作者的提示词。[提示词索引](docs/zh-CN/prompts.md) 列出了全部。'),
            ('怎么写好 Gemini 4 Carbon 提示词？', '指定输出一个独立的 HTML 文件，并说明用哪个渲染方式（Three.js、Canvas 或 SVG）；描述场景、交互，以及录屏需要捕捉的状态；禁止外部素材，并让它自测页面。`max_tokens` 要给足：思考始终开启，也占用这个额度。详细写法和模板见 [提示词写法](docs/zh-CN/prompt-guide.md)。'),
            ('怎么调用 Gemini 4 Carbon API？', '在 SandBase 上模型 ID 是 `{model_id}`，使用兼容 OpenAI 的 `/v1/chat/completions` 接口——Carbon 检查点通过 Argon 的 ID 提供，一个 Key 调用所有模型。这个模型没有 `reasoning_effort` 参数：它始终按自身描述里的强度推理。见 [复刻](#recreate) 和 [模型页]({model_page})。'),
            ('Gemini 4 Carbon 比 Claude Opus 5.5、GPT-6 Astra 或 Gemini 4 Argon 更强吗？', '实测一侧，头条榜单上是：Lab [Evals 榜单]({evals})（Artificial Analysis 数据，2026-10-29 快照）把 Gemini 4 Carbon (High) 放在智能指数第 1 位，59.4 分——领先 Opus 5.5 Max（58.4）、GPT-6 Astra Max（56.9）和它自己的上一检查点 Argon（50.4，第 13）。Lab [Pelican Test]({pelican}) 的那一行记在 `google/gemini-4-argon`——也就是 Carbon 实际运行的 ID——目前是 22 个模型中的第 1 名，3.81 分，每张图约 $0.12（2026-11-01 读取）。创作者在 3D 质量上意见一致，但并非全面胜出：好几位在爆炸视图模型和交互场景上把 Carbon 排在 Opus 前面，也有一位在机械鲨鱼对比里给它打了 77 对 90 的负分；而 Carbon 是旗舰定价——报告的跑一次 $3–$14，比 flash 档对手贵不少。详见 [模型对比](docs/zh-CN/model-comparison.md)。'),
            ('做一个视频要花多少钱？', '创作者报告的单次运行从约 $3.20（一个软糖南瓜场景）到 $14（一个彩虹软糖页面，同题 Opus 花了 $14、Carbon 花了 $4.30）不等，多数竞技场对比落在每页 $3–$10、每次 24–85 分钟。SandBase 标价为每百万输入 token $4、每百万输出 token $20，推理 token 按输出计费；缓存命中的输入按 0.05 倍计。'),
            ('可以转用这些视频吗？', '默认不可以，视频归作者所有。见 [MEDIA-RIGHTS](MEDIA-RIGHTS.md)。'),
        ],
        'contribute': '推荐作品',
        'contribute_body': '发现了应该收录的 Gemini 4 Carbon 作品？附上 X 原帖 [提交给我们]({repo_url}/issues/new?template=submit-video.yml)。通过后会先加入 SandBase Lab，下一次每日同步时出现在这里。觉得有用的话，点个 ⭐ 能让更多人看到。',
        'credits': '致谢与权利',
        'credits_body': [
            '所有视频、提示词和帖子归作者所有。每张卡片都注明作者并链接原帖。MIT 许可证只覆盖本仓库的脚本。更正署名或下架视频请见 [MEDIA-RIGHTS](MEDIA-RIGHTS.md)。',
            '{not_affiliated}',
        ],
        'footer': '由 [SandBase Lab]({lab_home}) 维护 · [全部 AI 视频合集]({all_collections})',
        'p_title': 'Gemini 4 Carbon 提示词',
        'p_switch': '[English](../prompts.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)',
        'p_intro': '共 {n} 条 Gemini 4 Carbon 视频，作者公开了提示词。打开即可查看提示词、观看视频，并在 SandBase Lab 上用 {short} 一键 **复刻**。第一次写 {short} 提示词？先看 [提示词写法](prompt-guide.md)。',
        'p_note': '每条都按 X 上发布的原文引用作者帖子。有的作者描述的是任务而不是完整提示词，有的把全文放在回复里，请打开 X 原帖查看讨论串。帖子原文保留作者语言。',
        'p_watch': '观看',
        'p_open': '在 SandBase Lab 复刻',
    },
}

# Labels mirror shared/ai-videos.ts VIDEO_CATEGORIES in the Lab repo.
CATEGORIES = {
    '3d-scene': ('3D scenes', '3D 场景'),
    'motion-graphics': ('Motion graphics', '动效'),
    'game': ('Games', '游戏'),
    'ui-demo': ('Product UI', '产品界面'),
    'particles': ('Particles & shapes', '粒子与形状'),
    'data-viz': ('Charts & diagrams', '图表图解'),
    'kinetic-type': ('Kinetic type', '文字动效'),
    'explainer': ('Explainers', '讲解'),
    'launch-film': ('Launch films', '发布片'),
    'short-film': ('Short films', '短片'),
    'music-video': ('Music videos', '音乐视频'),
    'anime': ('Anime', '动画'),
    'action': ('Action', '动作'),
    'ad': ('Ads', '广告'),
    'comparison': ('Tests & comparisons', '测试对比'),
    'showcase': ('Model showcases', '模型展示'),
}


def utm(medium, content=None):
    q = f'utm_source=github&utm_medium={medium}&utm_campaign={CFG["campaign"]}'
    return q + (f'&utm_content={content}' if content else '')
