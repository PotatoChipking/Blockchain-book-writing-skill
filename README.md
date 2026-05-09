# Book Skills

这个仓库保存用于中文技术书稿生产的 Codex skills。目前包含两个 skill：

- `blockchain-book-writing`：用于编写、扩写、润色、重构和检查中文区块链技术书籍章节。
- `text-to-word-formatting`：用于把文本、章节草稿或类 Markdown 文稿生成带指定排版格式的 Word `.docx` 文件。

当前这些 skills 还没有发布到 SkillHub，因此需要先在本地安装或在当前仓库中手动引用。

## 目录结构

```text
.
├── blockchain-book-writing/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   └── references/
│       ├── chapter-types.md
│       ├── terminology-and-domain-rules.md
│       ├── fact-checking-and-risk.md
│       └── style-and-quality.md
├── text-to-word-formatting/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   ├── references/
│   │   └── format-spec.md
│   └── scripts/
│       └── text_to_docx.py
├── book_skill.md
├── LICENSE
└── README.md
```

其中：

- 每个 skill 目录下的 `SKILL.md` 是 Codex 识别和加载 skill 的入口文件。
- `agents/openai.yaml` 是可选的界面元数据。
- `references/` 保存 skill 使用时按需读取的规则、模板或格式说明。
- `scripts/` 保存可直接执行的辅助脚本。
- `book_skill.md` 是 `blockchain-book-writing` 整理前的原始单文件版本，保留用于追溯。

## 本地安装

克隆仓库：

```bash
git clone git@github.com:PotatoChipking/Blockchain-book-writing-skill.git
cd Blockchain-book-writing-skill
```

把需要使用的 skill 目录复制到 Codex 本地 skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R blockchain-book-writing ~/.codex/skills/
cp -R text-to-word-formatting ~/.codex/skills/
```

安装后，本地路径应类似：

```text
~/.codex/skills/blockchain-book-writing/SKILL.md
~/.codex/skills/text-to-word-formatting/SKILL.md
```

如果只是想在当前工作区临时使用，也可以不复制到 `~/.codex/skills`，直接让 Codex 读取当前仓库中的对应 `SKILL.md`。

## blockchain-book-writing

这是一个用于编写中文区块链技术书籍章节的 Codex skill。它适合根据章节标题、目录、摘要或写作要求，生成书籍级章节正文，也可以用于扩写、润色、重构和检查区块链相关章节。

### 适用场景

- 编写区块链技术书籍章节
- 扩写章节标题或目录
- 统一章节写作风格
- 润色、重构已有草稿
- 编写联盟链、公链、稳定币、RWA、隐私计算、可信存储、跨链、共识、智能合约、金融基础设施等内容
- 对 Arc、Tempo、Plasma、Kinexys、Canton Network 等项目进行书籍化分析

不适合用于投资建议、实时行情分析、营销文案或短句解释。

### 使用方式

安装到本地 skills 目录后，可以显式调用：

```text
使用 $blockchain-book-writing，帮我写 9.5.1 Arc：稳定币原生 Layer-1，约 2500 字。
```

也可以给出更完整的章节要求：

```text
使用 $blockchain-book-writing，编写 9.5.1 Arc（2500字）。

上级章节：9.5 面向下一代金融基础设施的联盟链

内容摘要：
介绍 Circle Arc 作为稳定币原生 Layer-1 的诞生背景、Circle 战略定位及 USDC 深度集成理念。详细解析其 Layer-1 核心架构、USDC 原生 Gas 支付、模块化设计与隐私机制，结合机构支付和 DeFi 落地案例进行分析。最后总结其技术优势、面临挑战及对传统联盟链的借鉴价值。
```

如果还没有安装到本地 skills 目录，可以这样和 Codex 交互：

```text
请读取当前仓库的 blockchain-book-writing/SKILL.md，并按这个 skill 的规则帮我写下面的小节：

9.5.1 Arc（2500字）
……
```

### 推荐工作流

1. 先提供章节标题、上级目录和内容摘要。
2. 如果有前后章节边界，也一起提供，避免重复基础概念。
3. 对 2024 年之后的新项目、政策、性能数据、上线状态和合作方，要求 Codex 先做事实核查。
4. 生成正文后，再让 Codex 按 `style-and-quality.md` 做一次章节质量检查。
5. 对全书多个章节连续写作时，提供目录结构，保持术语和分析维度一致。

### 事实核查提醒

这个 skill 会要求 Codex 对较新的区块链项目和金融基础设施信息保持谨慎。涉及以下内容时，不应只凭记忆写成确定事实：

- 当前上线状态
- 主网上线时间
- 生态合作方
- 融资信息
- TPS、延迟、最终性等性能指标
- 监管进展
- 最新落地案例
- 机构角色或项目归属

优先参考官方文档、官方博客、白皮书、技术文档、GitHub 仓库、监管文件和权威研究报告。

## text-to-word-formatting

这是一个用于将文本写入 Word 并按指定格式排版的 Codex skill。它适合把章节草稿、书稿正文、类 Markdown 文本或整理后的内容生成 `.docx` 文件。

### 适用场景

- 将纯文本或类 Markdown 文稿转换为 Word `.docx`
- 按指定字体、字号、页边距、行距、缩进、标题层级排版
- 为书稿章节、报告、内部审阅稿生成 Word 文件
- 根据 JSON 格式说明统一多个文档的排版

当前脚本用于创建新的 `.docx` 文件，不用于编辑已有 Word 文件。

### 命令行使用

直接生成 Word 文件：

```bash
python3 text-to-word-formatting/scripts/text_to_docx.py \
  --input draft.txt \
  --output draft.docx \
  --title "章节标题"
```

使用格式配置文件：

```bash
python3 text-to-word-formatting/scripts/text_to_docx.py \
  --input draft.txt \
  --output draft.docx \
  --spec format.json
```

格式配置字段见：

```text
text-to-word-formatting/references/format-spec.md
```

### Codex 调用示例

```text
使用 $text-to-word-formatting，把下面这章内容生成 Word 文件：

- 输出文件：chapter-9-5-1.docx
- 页面：A4
- 正文：宋体，小四，1.5 倍行距，首行缩进 2 字符
- 一级标题：黑体，三号，居中
- 二级标题：黑体，四号，左对齐
- 页脚：第 PAGE 页

正文如下：
……
```

## 组合工作流：先写章节，再生成 Word

实际使用时可以连续调用两个 skill：

1. 使用 `blockchain-book-writing` 生成或润色章节正文。
2. 将生成后的正文保存为临时文本文件，例如 `chapter-9-5-1.txt`。
3. 使用 `text-to-word-formatting` 按指定格式生成 `.docx`。

推荐在调用时明确说明两个阶段的目标，例如：

```text
请连续使用两个 skill 完成任务：

1. 使用 $blockchain-book-writing 编写 9.5.1 Arc：稳定币原生 Layer-1，约 2500 字，书籍风格。
2. 使用 $text-to-word-formatting 将生成的正文写入 Word 文件。

Word 排版要求：
- 输出文件：chapter-9-5-1.docx
- 页面：A4
- 正文：宋体，小四，1.5 倍行距，首行缩进 2 字符
- 一级标题：黑体，三号，居中
- 二级标题：黑体，四号，左对齐
- 页脚：第 PAGE 页
```

如果这个组合流程会被频繁使用，可以继续新增一个编排型 skill，例如 `book-chapter-to-word`，专门负责协调“章节生成 → 文本落盘 → Word 排版 → 输出检查”。当前仓库暂时保持两个基础 skill 分离，便于单独维护和复用。

## License

See [LICENSE](LICENSE).
