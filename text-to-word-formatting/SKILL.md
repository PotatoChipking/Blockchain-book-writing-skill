---
name: text-to-word-formatting
description: Create Microsoft Word .docx documents from plain text, Markdown-like drafts, chapter manuscripts, outlines, or edited prose, and apply requested formatting such as Chinese/Latin fonts, font sizes, heading levels, margins, line spacing, paragraph indentation, alignment, page size, title styling, headers, and footers. Use when Codex needs to turn text into a formatted Word file, normalize a manuscript to a style guide, or prepare book/report/chapter text for Word-based review or publication.
---

# Text to Word Formatting

Use this skill to convert text into a formatted `.docx` file, append later sections to an existing `.docx`, or plan reliable Word formatting work. Prefer the bundled script because it uses only the Python standard library and produces portable OOXML Word files.

## Workflow

1. Parse the user's text and formatting requirements.
   Identify title, heading levels, body text, lists, footnote markers, page setup, fonts, font sizes, line spacing, indentation, alignment, headers, footers, and output path.

2. Normalize formatting into a JSON spec.
   Use `references/format-spec.md` for script fields. Use `references/publisher-default-format.md` for the default manuscript rules extracted from `区块链技术-作者著书须知.doc`.

3. Create the Word file.
   Run `scripts/text_to_docx.py` with `--input`, `--output`, and optionally `--spec`. To append a later section to an existing Word file, also pass `--append-to existing.docx`.

4. Validate the result.
   Confirm the `.docx` exists and can be listed with `unzip -l`. If footnote markers were present, confirm `word/footnotes.xml` exists and that the number of `w:footnoteReference` entries in `word/document.xml` matches the number of normal footnotes. For important files, inspect `word/document.xml` or open it if the environment allows.

## Quick Start

Create an input text file, then run:

```bash
python3 text-to-word-formatting/scripts/text_to_docx.py \
  --input draft.txt \
  --output draft.docx \
  --title "章节标题"
```

With a formatting spec:

```bash
python3 text-to-word-formatting/scripts/text_to_docx.py \
  --input draft.txt \
  --output draft.docx \
  --spec format.json
```

Append a later section to an existing Word file:

```bash
python3 text-to-word-formatting/scripts/text_to_docx.py \
  --input section-9-5-2.txt \
  --append-to 9.5.docx \
  --output 9.5.docx
```

When appending, the script inserts new paragraphs before the existing document section properties and preserves the original `.docx` package parts. Use a different `--output` path if you want to keep a backup.

## Text Structure Rules

- Lines starting with `#`, `##`, `###`, or `####` become heading levels 1-4.
- Numbered headings such as `1. 标题`, `1.1 标题`, and `1.1.1 标题` become heading levels based on numbering depth.
- Lines starting with `-`, `*`, or `•` become bullet-style paragraphs.
- Other non-empty lines become body paragraphs.
- Inline markers of the form `（批注：source note）` become Word footnotes. The body text keeps only a footnote number at that location; the source note appears at the bottom of the page in `word/footnotes.xml`.
- Blank lines are preserved as spacing paragraphs.
- If the user provides a true document title, pass it with `--title`.
- For numbered book sections such as `9.5.1` or `9.5.2`, keep the heading as the first line of the input text instead of passing it with `--title`; this preserves the publisher rule that section headings are left aligned.
- For multi-section manuscripts, append each new section to the same `.docx` with `--append-to` instead of creating separate Word files.

## Formatting Guidance

Use the publisher manuscript defaults extracted from `区块链技术-作者著书须知.doc` unless the user gives a more specific format:

- Page: A4, 2.54 cm margins.
- Body Chinese font: SimSun/Songti-style.
- Body English and numbers: Times New Roman.
- Body size: 五号 / 10.5 pt, 1.5 line spacing, first-line indent of 2 Chinese characters, justified.
- Heading English and numbers: use the same font as the heading Chinese text.
- Second-level headings: 楷体_GB2312 四号 / 14 pt, left aligned.
- Third-level headings: 黑体小四 / 12 pt, bold, left aligned.
- Alignment: title centered, headings left, body justified.
- Header: omit by default. If requested, use odd pages for chapter name and even pages for book name when the output tooling supports it.
- Footnotes: use footnote numbers in the body and place source notes at the bottom of the page. Use this for references to official documentation, GitHub repositories, papers, standards, regulatory documents, and authoritative data sources. Do not leave long reference notes as visible parenthetical text in the final body unless the user requests that style.

Do not invent publisher-specific requirements. If a requirement is missing, use defaults and mention which assumptions were applied.

## Resources

- `scripts/text_to_docx.py`: Convert plain text or Markdown-like drafts to `.docx`, convert `（批注：...）` markers into Word footnotes, or append text to an existing `.docx`.
- `references/format-spec.md`: Supported JSON fields and examples.
- `references/publisher-default-format.md`: Default manuscript layout, numbering, figure/table, and expression rules extracted from the supplied author instructions document.
