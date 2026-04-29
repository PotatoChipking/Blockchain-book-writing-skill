---
name: blockchain-book-writing
description: Use when writing, expanding, restructuring, polishing, fact-checking, or reviewing Chinese book chapters about blockchain, consortium chains, public chains, stablecoins, RWA, tokenized deposits, privacy computing, trusted data circulation, cross-chain systems, consensus, smart contracts, digital payments, and financial infrastructure. Use for chapter-level book writing rather than short explanations, marketing copy, investment advice, or real-time market analysis.
metadata:
  short-description: Write Chinese blockchain book chapters
---

# Blockchain Book Writing

Use this skill to produce formal Chinese technical book chapters about blockchain and related financial or data infrastructure topics. The output should read like a publishable book chapter, not a blog post, encyclopedia entry, product brochure, or loose technical note.

## Default Reader

Assume readers have some technical background but may not know the specific protocol, project, regulatory term, or engineering implementation being discussed. Explain key concepts when needed, but do not write for complete beginners.

Default audience includes blockchain engineers, architects, fintech practitioners, data and trusted-computing researchers, enterprise blockchain builders, academic readers, and technical managers.

## Use Cases

Use this skill for:

- Writing a full chapter or section from a title, outline, abstract, keywords, or requirements.
- Expanding, restructuring, polishing, or unifying an existing chapter draft.
- Writing about consortium chains, public chains, stablecoins, RWA, tokenized deposits, privacy computing, trusted storage, cross-chain systems, consensus, smart contracts, digital payments, and financial infrastructure.
- Analyzing a blockchain project, protocol, architecture, engineering route, or industry trend in book-chapter form.
- Comparing blockchain architectures, governance models, or technical routes.

Do not use this skill for short one-sentence explanations, social-media articles, marketing copy, investment recommendations, trading advice, or real-time market data analysis.

## Core Workflow

1. Parse the chapter input.
   Identify the chapter title, number, parent section, child sections, abstract, required points, expected length, target style, draft content, and adjacent chapter context when available.

2. Determine the chapter type.
   Choose the primary type from technical principle, architecture design, project case, comparison, trend review, engineering practice, historical evolution, application scenario, policy and compliance analysis, or mixed chapter.

3. Establish the chapter role.
   Decide whether the chapter explains a foundation, introduces a core technology, analyzes a representative project, presents engineering practice, compares routes, summarizes trends, answers a key question, or prepares the next chapter.

4. Form an internal central argument.
   Before writing, identify what the chapter is about, why it matters, what problem it addresses, and how it relates to blockchain, consortium chains, financial infrastructure, or trusted digital economy.

5. Build a progressive structure.
   Prefer this default progression unless the user provides another structure: background problem -> technical or project positioning -> core mechanism -> engineering implementation or architecture -> application scenarios -> advantages and limits -> implication for the book.

6. Write in formal book style.
   Each section should first explain the problem, then the mechanism, then the meaning. Do not merely list terms. Distinguish vision, design goals, implemented capabilities, and future possibilities.

7. Check facts and uncertainty.
   If the chapter involves post-2024 projects, current project status, launch dates, partners, financing, transaction volumes, TPS, latency, finality, protocol versions, roadmap, regulatory progress, ecosystem data, latest cases, or current leaders, verify facts before stating them as current. Prefer official docs, official blogs, white papers, technical docs, GitHub repositories, regulatory or standards documents, authoritative media, and research reports.

8. Apply terminology and style controls.
   Keep terms consistent. Avoid hype, marketing claims, unsupported certainty, and mixing distinct concepts such as stablecoins, tokenized deposits, RWA, CBDC, digital assets, privacy, anonymity, auditability, and public transparency.

9. Run a final quality check.
   Confirm the output answers the title, has a clear progression, uses accurate concepts, keeps book style, includes engineering depth where relevant, fits adjacent chapters, and marks unverified or uncertain claims.

## Default Output

If the user only asks to write from a chapter title and does not specify format, output a ready-to-use book section with this structure:

```md
## 章节标题

### 1. 背景与问题

### 2. 技术或项目定位

### 3. 核心机制与架构

### 4. 关键特点与应用场景

### 5. 局限与挑战

### 6. 对本书主题的启示
```

If key information is missing, write a usable version from available context and list optional information the user can add. Do not block unless there is no title or topic.

## Reference Files

Load only the references needed for the current task:

- `references/chapter-types.md`: chapter-type templates and structure patterns.
- `references/terminology-and-domain-rules.md`: terminology distinctions and domain-specific focus areas.
- `references/fact-checking-and-risk.md`: fact-checking rules, uncertainty language, forbidden claims, and source priorities.
- `references/style-and-quality.md`: writing style, recommended expressions, length rules, and final checklist.
