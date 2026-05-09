---
name: text-to-word-formatting
description: Create Microsoft Word .docx documents from plain text, Markdown-like drafts, chapter manuscripts, outlines, or edited prose, and apply requested formatting such as Chinese/Latin fonts, font sizes, heading levels, margins, line spacing, paragraph indentation, alignment, page size, title styling, headers, and footers. Use when Codex needs to turn text into a formatted Word file, normalize a manuscript to a style guide, or prepare book/report/chapter text for Word-based review or publication.
---

# Text to Word Formatting

Use this skill to convert text into a formatted `.docx` file, append later sections to an existing `.docx`, or plan reliable Word formatting work. Prefer the bundled script because it uses only the Python standard library and produces portable OOXML Word files.

## Workflow

1. Parse the user's text and formatting requirements.
   Identify title, heading levels, body text, lists, page setup, fonts, font sizes, line spacing, indentation, alignment, headers, footers, and output path.

2. Normalize formatting into a JSON spec.
   Use `references/format-spec.md` for script fields. Use `references/publisher-default-format.md` for the default manuscript rules extracted from `区块链技术-作者著书须知.doc`.

3. Create the Word file.
   Run `scripts/text_to_docx.py` with `--input`, `--output`, and optionally `--spec`. To append a later section to an existing Word file, also pass `--append-to existing.docx`.

4. Validate the result.
   Confirm the `.docx` exists and can be listed with `unzip -l`. For important files, inspect `word/document.xml` or open it if the environment allows.

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
- Blank lines are preserved as spacing paragraphs.
- If the user provides a true document title, pass it with `--title`.
- For numbered book sections such as `9.5.1` or `9.5.2`, keep the heading as the first line of the input text instead of passing it with `--title`; this preserves the publisher rule that section headings are left aligned.
- For multi-section manuscripts, append each new section to the same `.docx` with `--append-to` instead of creating separate Word files.

## Formatting Guidance

Use the publisher manuscript defaults extracted from `区块链技术-作者著书须知.doc` unless the user gives a more specific format:

- Page: A4, 2.54 cm margins.
- Body Chinese font: SimSun/Songti-style.
- Body English and numbers: Times New Roman.
- Body size: 12 pt, 1.5 line spacing, first-line indent of 2 Chinese characters, justified.
- Heading English and numbers: use the same font as the heading Chinese text.
- Heading sizes: 16 pt, 14 pt, 13 pt, 12 pt for levels 1-4 unless the user provides a publisher template.
- Alignment: title centered, headings left, body justified.
- Header: omit by default. If requested, use odd pages for chapter name and even pages for book name when the output tooling supports it.

Do not invent publisher-specific requirements. If a requirement is missing, use defaults and mention which assumptions were applied.

## Resources

- `scripts/text_to_docx.py`: Convert plain text or Markdown-like drafts to `.docx`, or append text to an existing `.docx`.
- `references/format-spec.md`: Supported JSON fields and examples.
- `references/publisher-default-format.md`: Default manuscript layout, numbering, figure/table, and expression rules extracted from the supplied author instructions document.
