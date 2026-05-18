# Fact Checking and Risk Control

## When to Verify

Verify facts before making current or definite claims about:

- Post-2024 projects.
- Current project status.
- Mainnet launch time.
- Partners.
- Financing.
- Transaction volume.
- TPS, latency, finality, and other performance metrics.
- Protocol versions.
- Technical route changes.
- Regulatory policies.
- Official roadmaps.
- Ecosystem data.
- Latest cases.
- Current leaders, institutional roles, or project ownership.

## Source Priority

Prefer sources in this order:

1. Official documentation.
2. Official blog.
3. White paper.
4. Technical documentation.
5. GitHub or open-source repositories.
6. Regulatory or standards-organization documents.
7. Authoritative media reports.
8. Research institution reports.

## Distinguish Facts, Judgments, and Speculation

Facts are confirmed by reliable material.

Use expressions such as:

- "该项目由……提出"
- "该协议采用……"
- "该系统由……组成"
- "该项目将……作为核心设计"

In book prose, do not routinely begin sentences with source-preface expressions such as "据公开资料显示", "据官方说明", "根据官方说明", "从现有资料看", or "从公开资料看". These expressions are acceptable only when the information is early, uncertain, disputed, or source-limited.

Judgments are analysis based on facts and technical logic.

Use expressions such as:

- "这意味着……"
- "从架构角度看……"
- "其核心价值在于……"

Speculation concerns future trends or possible effects.

Use expressions such as:

- "未来可能……"
- "如果该模式进一步成熟……"
- "这一方向仍有待验证……"

Never write speculation as fact.

## Cautious Language

Use cautious expressions for uncertain or emerging topics:

- "其设计目标是……"
- "如果该路线能够落地……"
- "这一方向仍处于早期阶段……"
- "目前更适合作为趋势观察，而非成熟范式……"
- "相关能力仍需在生产环境中验证……"

Avoid these claims unless strongly supported:

- "已经证明……"
- "必然成为……"
- "完全解决……"
- "彻底替代……"
- "没有风险……"
- "确定会……"

## Citation Handling

By default, provide footnote-style citations for source-backed writing that depends on GitHub repositories, official documentation, papers, regulatory documents, standards, or authoritative data sources. Do this even if the user does not explicitly ask for citations. Omit citations only when the user explicitly requests citation-free prose.

Keep the main prose readable and book-like. Mark the supported sentence or clause with a footnote number, and place the source note at the bottom of the page. Do not repeatedly start sentences with source-preface expressions.

Use citation notes for:

- Official documentation: protocol versions, architecture, module behavior, APIs, governance process, roadmap, or product status.
- GitHub repositories: source-code implementation, license, release status, module ownership, branch/tag/release, or actual code behavior.
- Papers: algorithms, cryptographic assumptions, formal proofs, consensus properties, complexity, security model, or benchmark methods.
- Authoritative data: transaction volume, asset size, TPS, latency, finality, market data, regulatory dates, adoption data, or ecosystem statistics.
- Regulatory and standards documents: compliance requirements, legal definitions, supervisory rules, technical standards, and implementation guidelines.

Preferred footnote content:

```text
参见 Hyperledger Fabric v2.x 官方文档中关于背书策略、通道和私有数据的说明，URL。
参见项目 GitHub 仓库 owner/repo 的 release notes 或对应模块源码，建议标明 tag/commit。
参见原论文对共识安全模型、复杂度和故障假设的论证，作者、题名、会议/期刊或 arXiv、年份。
参见监管机构发布的正式文本或标准文件，建议标明发布日期和条款位置。
```

For smooth chapters, do not cite every general claim. Cite where the source materially supports a specific fact, number, protocol behavior, or policy statement.

If working in plain text before Word conversion, use `（批注：source note）` immediately after the supported sentence. The Word formatting step should convert these markers into true footnotes so the final `.docx` body contains only footnote numbers and the source notes appear at the bottom of the page.

If exact URLs are needed, place them in footnotes or a reference list. Avoid inserting long URLs in body prose unless requested.

For uncertain facts, add a short "待核查事实" or "表述风险" section when appropriate.
