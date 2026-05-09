---
name: text-to-word-formatting
description: Create Microsoft Word .docx documents from plain text, Markdown-like drafts, chapter manuscripts, outlines, or edited prose, and apply requested formatting such as Chinese/Latin fonts, font sizes, heading levels, margins, line spacing, paragraph indentation, alignment, page size, title styling, headers, and footers. Use when Codex needs to turn text into a formatted Word file, normalize a manuscript to a style guide, or prepare book/report/chapter text for Word-based review or publication.
---

# Text to Word Formatting

Use this skill to convert text into a formatted `.docx` file or to plan reliable Word formatting work. Prefer the bundled script for new documents because it uses only the Python standard library and produces a portable OOXML Word file.

## Workflow

1. Parse the user's text and formatting requirements.
   Identify title, heading levels, body text, lists, page setup, fonts, font sizes, line spacing, indentation, alignment, headers, footers, and output path.

2. Normalize formatting into a JSON spec.
   Use `references/format-spec.md` when the user provides detailed or ambiguous style requirements.

3. Create the Word file.
   Run `scripts/text_to_docx.py` with `--input`, `--output`, and optionally `--spec`.

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

## Text Structure Rules

- Lines starting with `#`, `##`, `###`, or `####` become heading levels 1-4.
- Numbered headings such as `1. 标题`, `1.1 标题`, and `1.1.1 标题` become heading levels based on numbering depth.
- Lines starting with `-`, `*`, or `•` become bullet-style paragraphs.
- Other non-empty lines become body paragraphs.
- Blank lines are preserved as spacing paragraphs.
- If the user provides a separate title, pass it with `--title`; otherwise keep the title in the input text.

## Formatting Guidance

Use conservative Chinese manuscript defaults unless the user gives a specific format:

- Page: A4, 2.54 cm margins.
- Chinese font: SimSun or Songti-style body font when unspecified.
- Latin font: Times New Roman.
- Body size: 12 pt, 1.5 line spacing, first-line indent of 2 Chinese characters.
- Heading sizes: 16 pt, 14 pt, 13 pt, 12 pt for levels 1-4.
- Alignment: title centered, headings left, body justified.

Do not invent publisher-specific requirements. If a requirement is missing, use defaults and mention which assumptions were applied.

## Resources

- `scripts/text_to_docx.py`: Convert plain text or Markdown-like drafts to `.docx`.
- `references/format-spec.md`: Supported JSON fields and examples.
