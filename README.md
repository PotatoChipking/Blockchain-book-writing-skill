# Blockchain Book Writing Skill

这是一个用于编写中文区块链技术书籍章节的 Codex skill。它适合根据章节标题、目录、摘要或写作要求，生成书籍级章节正文，也可以用于扩写、润色、重构和检查区块链相关章节。

当前这个 skill 还没有发布到 SkillHub，因此需要先在本地安装或手动引用。

## 适用场景

- 编写区块链技术书籍章节
- 扩写章节标题或目录
- 统一章节写作风格
- 润色、重构已有草稿
- 编写联盟链、公链、稳定币、RWA、隐私计算、可信存储、跨链、共识、智能合约、金融基础设施等内容
- 对 Arc、Tempo、Plasma、Kinexys、Canton Network 等项目进行书籍化分析

不适合用于投资建议、实时行情分析、营销文案或短句解释。

## 目录结构

```text
blockchain-book-writing/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── chapter-types.md
    ├── terminology-and-domain-rules.md
    ├── fact-checking-and-risk.md
    └── style-and-quality.md
```

其中：

- `SKILL.md` 是 Codex 识别和加载 skill 的入口文件。
- `references/` 保存章节模板、术语规则、事实核查规则和质量检查清单。
- `agents/openai.yaml` 是可选的界面元数据。
- `book_skill.md` 是原始整理前的完整单文件版本，保留用于追溯。

## 本地安装

克隆仓库：

```bash
git clone git@github.com:PotatoChipking/Blockchain-book-writing-skill.git
cd Blockchain-book-writing-skill
```

把 skill 目录复制到 Codex 本地 skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R blockchain-book-writing ~/.codex/skills/
```

安装后，本地路径应类似：

```text
~/.codex/skills/blockchain-book-writing/SKILL.md
```

如果你只是想在当前工作区临时使用，也可以不复制到 `~/.codex/skills`，直接让 Codex 读取当前仓库中的 `blockchain-book-writing/SKILL.md`。

## 使用方式

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

## 推荐工作流

1. 先提供章节标题、上级目录和内容摘要。
2. 如果有前后章节边界，也一起提供，避免重复基础概念。
3. 对 2024 年之后的新项目、政策、性能数据、上线状态和合作方，要求 Codex 先做事实核查。
4. 生成正文后，再让 Codex 按 `style-and-quality.md` 做一次章节质量检查。
5. 对全书多个章节连续写作时，提供目录结构，保持术语和分析维度一致。

## 事实核查提醒

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

## 示例调用

```text
使用 $blockchain-book-writing，帮我扩写这一节：

9.5.5 Canton Network：隐私公共 L1 与机构级 RWA 网络

要求：
- 约 2500 字
- 书籍风格，不要写成项目宣传稿
- 重点讲 need-to-know 隐私模型、互操作机制和 RWA 代币化架构
- 与稳定币基础设施和传统联盟链做衔接
```

## License

See [LICENSE](LICENSE).
