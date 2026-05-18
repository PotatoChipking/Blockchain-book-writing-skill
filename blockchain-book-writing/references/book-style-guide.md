# Book Style Guide

Use this guide when writing, expanding, polishing, or unifying chapters for a multi-author Chinese blockchain technical book. This file defines the common prose style, terminology discipline, tone, and chapter-level writing habits that should remain consistent across chapters.

## 1. Overall Voice

- Use formal Chinese technical book prose.
- Use an objective third-person voice. Avoid expressions such as "我们认为", "笔者认为", "大家都知道", "显而易见", and "不难看出" unless the user explicitly requests a more essay-like style.
- Write for technically literate readers, not complete beginners and not only domain experts.
- Keep language steady, analytical, and restrained.
- Do not write like product marketing, investment analysis, news commentary, social-media posts, encyclopedia entries, or internal meeting notes.
- Explain why a technology matters, how it works, where it applies, and where its boundary lies.

## 1.1 Preserve Draft Voice and Format

When polishing, unifying, fact-checking, or adding citations to an existing draft, preserve the original manuscript by default.

- Do not restructure the chapter, reorder paragraphs, merge sections, split sections, or change heading levels unless the user explicitly asks for restructuring.
- Do not force the draft into the default chapter template if the author has already supplied a usable structure.
- Do not replace the author's readable prose with generic, over-balanced, AI-sounding expressions.
- Do not overuse formulaic transitions such as "从……角度看", "其核心价值在于", "这一设计意味着", or "其局限也较为清晰". These are optional tools, not required sentence patterns.
- Preserve author-specific examples, comparisons, emphasis, and narrative rhythm when they are accurate and suitable for a technical book.
- Apply only the minimum necessary edits for factual accuracy, terminology consistency, citation placement, obvious grammar problems, and clearly inappropriate tone.
- If major restructuring, compression, expansion, or tone rewriting would improve the draft, mention it as a recommendation instead of silently rewriting the manuscript.
- When the user asks to "按规范统一", interpret it as light editing and normalization by default, not full rewriting.

The goal is to make the chapter publishable while keeping it recognizably the same manuscript. Style rules should improve clarity and reliability; they must not flatten the writing into a mechanical template.

## 2. Chapter Logic

For technical, platform, or project chapters, prefer this progression unless the user provides a different structure:

1. Background problem: What real problem creates the need for this topic.
2. Technical or project positioning: What the technology, platform, or project is meant to solve.
3. Core mechanism: Architecture, protocol, workflow, key components, or implementation logic.
4. Application context: Where it is useful and what conditions make it useful.
5. Advantages and limits: Strengths, applicable boundaries, risks, and trade-offs.
6. Connection to the book: How the section relates to adjacent chapters or the book's main argument.

Do not merely list features. Each section should show a causal chain:

```text
problem -> mechanism -> engineering implication -> application value -> limitation
```

For existing drafts, use this progression as a diagnostic checklist rather than a mandatory rewrite template. If a draft already covers the required logic in a different order, keep the author's order unless the user asks for structural rewriting.

## 3. Paragraph Style

- Each paragraph should have one clear central point.
- Start important paragraphs with a topic sentence or analytical judgment, then explain the mechanism or evidence.
- Avoid very short fragmented paragraphs unless they are headings or transition paragraphs.
- Avoid excessively long paragraphs that mix background, architecture, examples, and conclusions without structure.
- Avoid starting many adjacent paragraphs with the same pattern, especially "首先", "其次", "最后".
- When writing new text from scratch, varied transitions may include:
  - "从架构角度看……"
  - "进一步看……"
  - "与此相对……"
  - "在工程实现中……"
  - "这一设计的意义在于……"
  - "其局限也较为清晰……"
- Do not insert these transitions mechanically into an existing draft. If the original transition is clear, keep it.

## 4. Tone and Judgment

- Avoid absolute claims unless strongly supported.
- Avoid marketing-style words and slogans.
- Do not write a project as an unconditional success case.
- Do not present roadmaps, design goals, ecosystem expectations, or commercial visions as implemented facts.
- For emerging projects, use cautious language and include uncertainty or remaining validation points.
- For financial, data, privacy, security, and regulatory topics, always mention relevant constraints or risks when making positive claims.

Prefer bounded expressions:

- "在……场景下更具适用性"
- "其核心价值在于……"
- "这一设计有助于……"
- "仍需在生产环境中验证……"
- "其长期影响取决于……"
- "更适合作为趋势观察，而非成熟范式"

Avoid using source-preface expressions as routine sentence openings in book prose:

- "据公开资料显示……"
- "据官方说明……"
- "根据官方说明……"
- "从现有资料看……"
- "从公开资料看……"
- "根据项目披露的信息……"

These expressions may be used sparingly only when the information is early, uncertain, disputed, or source-limited. In normal prose, write the verified fact or bounded judgment directly, and place uncertainty in the predicate or closing clause.

Prefer:

- "Arc 将稳定币原生 Gas 作为核心设计之一。"
- "Tempo 的设计目标之一是提供亚秒级最终性。"
- "该路线仍需要生产环境中的持续验证。"
- "相关案例更适合作为早期探索，而非成熟范式。"

Avoid:

- "据公开资料显示，Arc 采用稳定币原生 Gas 设计。"
- "根据官方说明，Tempo 支持亚秒级最终性。"
- "从现有资料看，该路线仍处于早期。"

Avoid unsupported expressions:

- "彻底颠覆"
- "革命性改变"
- "完美解决"
- "必然取代"
- "唯一答案"
- "最强技术"
- "划时代突破"
- "没有任何风险"
- "毫无疑问会成为未来主流"
- "已经完全成熟"

## 5. Facts, Judgments, and Speculation

Distinguish three levels of statements:

- Facts: confirmed by reliable sources. In book prose, state stable verified facts directly, such as "该协议采用……", "该系统由……组成", or "该项目将……作为核心设计". Do not routinely preface facts with "公开资料显示" or "官方文档说明".
- Judgments: analysis based on facts and technical reasoning. Use expressions such as "这意味着", "从架构角度看", "其核心价值在于".
- Speculation: possible future outcomes. Use expressions such as "未来可能", "如果该路线能够落地", "仍有待验证".

Never write speculation as fact.

For post-2024 projects, current project status, performance indicators, launch schedules, partners, regulatory status, and production use cases, verify before making definite statements.

## 6. Footnote Citations for Sources

By default, provide footnote-style citations when the text relies on GitHub repositories, official documentation, white papers, academic papers, regulatory documents, standards, or authoritative data sources. Keep the body prose book-like; do not turn source names into repetitive sentence openings. Omit citations only when the user explicitly asks for citation-free prose.

The citation style for book manuscripts is:

- Mark a short footnote number at the exact sentence or clause supported by the source.
- Put the source description and URL in the footnote at the bottom of the page.
- Do not leave long citation text inside the body paragraph.
- Do not collect all source notes only at the end of the section when specific facts appear earlier in the body.
- A final reference-link summary may be added for editorial convenience, but it does not replace footnotes at the corresponding body locations.

Use citation notes for:

- Protocol versions, architecture descriptions, and API behavior from official documentation.
- Code implementation, license, release, or repository status from GitHub or other source repositories.
- Consensus, cryptography, formal verification, performance, or security claims from papers.
- TPS, latency, finality, transaction volume, asset size, ecosystem data, or regulatory dates from authoritative data sources.
- Policy, compliance, supervisory, or legal statements from regulators or standards bodies.
- New projects after 2024, especially launch status, roadmap, partners, production use, and performance indicators.

Footnotes should be short and attached to the relevant sentence, clause, table item, or paragraph. Do not overload every general sentence with citations. One footnote can support a paragraph if the paragraph is based on the same source. The default is citation-on for source-backed technical and factual claims.

Preferred source-note content:

```text
参见 Hyperledger Fabric v2.x 官方文档中关于 endorsement policy、channel 与 private data 的说明，URL。
参见 ChainMaker 官方文档中关于“一核多引擎”和 BUDA 架构的介绍，URL。
参见项目 GitHub 仓库 owner/repo 的 release notes、README 或对应模块源码，建议标明 tag/commit。
参见原论文对 HotStuff 三阶段提交和线性通信复杂度的论证，作者、题名、会议/期刊或 arXiv、年份。
参见欧盟 MiCA 正式文本中关于电子货币代币和加密资产服务商的规定，发布日期或条款位置。
```

When precise bibliographic information is available, include enough information for later editorial verification:

```text
作者，论文题名，会议/期刊或 arXiv，年份。
机构名称，文档题名或页面标题，版本号或发布日期，URL。
GitHub 仓库 owner/repo，分支、tag、commit 或 release，访问日期，URL。
```

If the manuscript is still in plain text before conversion to Word, write source notes in the marker form `（批注：source note）` immediately after the supported sentence. The Word conversion tool should convert these markers into true Word footnotes: body text keeps only footnote numbers, and the source notes appear at the bottom of the page.

Example before Word conversion:

```text
Arc 以 USDC 作为原生 Gas 代币。（批注：参见 Arc 官方文档 Gas and fees，https://docs.arc.io/arc-chain。）
```

Expected Word result:

```text
Arc 以 USDC 作为原生 Gas 代币。¹
```

The footnote at the bottom of the page contains the source note.

Avoid:

- Beginning many sentences with "据官方文档", "根据论文", "GitHub 显示", or "数据显示".
- Citing unofficial blogs for protocol facts when official docs, papers, or repositories are available.
- Citing performance numbers without benchmark conditions, date, or source type.
- Using citation notes to support broad value judgments that are actually the author's analysis.
- Leaving citations as visible parenthetical notes in the body of the final Word manuscript.

## 7. Technical Explanation

- Explain concepts before using deep implementation details.
- Do not stack unexplained English abbreviations.
- When an English abbreviation first appears, provide context or a Chinese explanation where useful.
- Separate architecture, protocol, implementation, governance, and business model. Do not mix them as if they were the same thing.
- Do not imply that "putting data on-chain" automatically makes data trustworthy.
- For blockchain systems, explain the trust boundary: who operates nodes, who can write, who can read, who validates, who upgrades, and who audits.
- For performance claims, distinguish design goal, test result, benchmark condition, and production capacity.
- For privacy claims, distinguish privacy, anonymity, confidentiality, selective disclosure, and auditability.

## 8. Terminology Discipline

Use one term consistently within a chapter and across adjacent chapters.

Keep these distinctions:

- "联盟链" emphasizes multi-institution governance.
- "许可链" emphasizes access control. It may overlap with consortium chain but is not identical.
- "隐私" is not the same as "匿名". Financial and government systems usually require regulated privacy, not full anonymity.
- "可审计性" is not the same as "公开透明". Consortium-chain systems often need selective transparency.
- "稳定币", "代币化存款", "RWA", "CBDC", and "数字资产" differ in issuer, balance-sheet treatment, legal status, and settlement logic.
- "支付型 Layer-1" should not be explained only as a faster general-purpose chain; discuss payment finality, stable fees, merchant access, and compliance.
- "数据上链" should usually mean putting hashes, proofs, credentials, status, or audit records on-chain, not storing all raw data on-chain.

## 9. Multi-Author Consistency

When unifying chapters written by different authors:

- Normalize tone to formal technical book prose with minimal necessary edits.
- Remove author-specific oral expressions, rhetorical questions, and subjective comments.
- Align terminology, citation style, heading style, and obvious tone problems, but preserve each author's usable structure and argument flow.
- Avoid making all chapter openings begin with the same formula.
- Make each chapter answer its assigned role in the book instead of repeating general blockchain background, but do not delete context that is necessary for the section's own readability.
- Avoid repeated explanations of the same basic concept across adjacent chapters. Later chapters should briefly refer back or deepen the concept when doing so does not damage the author's argument.
- Use common analytical dimensions, such as background, positioning, architecture, mechanisms, scenarios, limits, and implications, as a review checklist rather than a rigid output format.
- Ensure that each platform chapter has both advantages and limitations, adding boundary sentences where needed rather than rewriting the whole section.
- Ensure that trend chapters summarize from previous cases instead of introducing disconnected claims.
- Keep heading style, paragraph density, and terminology consistent, but do not flatten all chapters into the same sentence rhythm.

## 10. Structure by Section Level

For a third-level numbered section such as `9.5.1`, `9.5.2`, or `2.3.4`:

- Do not add extra internal numbered headings by default.
- Use the section heading followed by substantial paragraphs.
- If a target length is specified, expand paragraph depth rather than creating many subheadings.
- Keep the progression: background and positioning -> mechanism and application -> strengths, limits, and implications.

For a larger section or full chapter:

- Use clear second-level and third-level headings.
- Avoid more than five structural levels.
- Do not create headings that are too long or slogan-like.
- Do not use question-style headings unless explicitly requested.

## 11. Risk and Boundary Writing

Every technical or project analysis should include boundaries when relevant:

- Technical boundary: What the technology cannot solve.
- Governance boundary: Who controls upgrades, membership, and dispute handling.
- Data boundary: Whether the source data is trustworthy and how chain-off-chain consistency is maintained.
- Privacy boundary: Who can see what under what authorization.
- Regulatory boundary: What compliance assumptions are required.
- Adoption boundary: Whether claims are based on production use, pilot projects, design goals, or public announcements.

Use boundary analysis to make the prose more credible, not more pessimistic.

## 12. Preferred Revision Pass

When polishing a chapter, perform these checks:

1. Preserve the original structure, paragraph order, examples, and readable voice unless the user asked for rewriting.
2. Remove hype, slogans, and exaggerated certainty.
3. Normalize terminology and project names.
4. Separate facts, judgments, and future expectations.
5. Add footnote citations at the exact facts supported by official documents, GitHub, papers, regulatory documents, standards, or authoritative data.
6. Add missing engineering mechanisms where the text only lists features, but prefer local insertion over full paragraph rewriting.
7. Add missing limits where the text only praises a technology, but keep the author's main argument intact.
8. Remove repeated background content only when it is clearly redundant and not needed for local readability.
9. Make transitions between sections explicit only where the original transition is unclear.
10. Ensure the chapter reads like part of the same book as adjacent chapters without making all chapters sound identical.
