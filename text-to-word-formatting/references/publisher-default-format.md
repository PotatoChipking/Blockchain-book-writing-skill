# Publisher Default Format

These rules were summarized from `区块链技术-作者著书须知.doc`. Apply them as the default Word/manuscript style unless the user supplies a different style guide.

## Direct Word Formatting Defaults

- Body Chinese font: 宋体 / SimSun.
- Body English and numbers: Times New Roman.
- Body font size: 五号 / 10.5 pt.
- Body paragraph: first-line indent of 2 Chinese characters.
- Body alignment: justify both sides.
- Body text: avoid unnecessary spaces between Chinese characters.
- Long code blocks: 小五号 / 9 pt when possible.
- Page setup: keep one unified page setup across the whole manuscript; use A4 with standard margins when no exact margin is provided.
- Header: omit by default. If explicitly requested and the tooling supports odd/even headers, use chapter name on odd pages and book name on even pages.
- Table of contents: may be generated automatically; do not include page numbers unless the user requests them.

## Heading and Numbering Rules

- Prefer no more than 5 structural levels.
- Default chapter and section numbering:
  - `第1章`
  - `1.1`
  - `1.1.1`
  - `1.1.1.1` only when needed
  - `1.`
  - `1)`
  - `(1)`
  - `①`
- Avoid Chinese numerals, Roman numerals, and Latin letters as structural numbering.
- Chapter/section numbers and titles should be separated by one Chinese-character space.
- Item numbers such as `1)`, `(1)`, and `①` should use half-width parentheses where applicable.
- Do not use Word automatic numbering when matching this publisher style; prefer explicit/manual numbering in the text.
- Heading text should be concise, usually no more than 15 Chinese characters.
- Headings should not end with punctuation, including question marks or exclamation marks.
- English letters and numbers in headings should use the same font as the Chinese heading text.
- Second-level headings: 楷体_GB2312, 四号 / 14 pt, left aligned.
- Third-level headings: 黑体 / SimHei, 小四 / 12 pt, bold, left aligned.

## Figures and Tables

- Number figures and tables by chapter with `x-xx`, such as `图1-1` and `表1-1`; numbering must be continuous within each chapter.
- Figures and tables should be referenced in the body before they appear.
- Do not refer to figures or tables using vague directional words such as `如下` or `以下`.
- Use references such as `如图X-Y所示`, `见图X-Y`, `列于表X-Y`, or `见表X-Y`.
- Figure caption: 小五号宋体, centered.
- Table caption: 五号仿体, centered.
- Table body text: 六号宋体.
- Tables should be closed tables, centered as a whole, with the outer border slightly thicker than inner lines.
- Figure and table titles should be short and should not end with punctuation.

## UI, Terms, and Inline Expression

- Chinese screen UI names, such as windows, menus, dialogs, and controls, should be enclosed in `【】`.
- Do not use `【】` for content that is not Chinese screen UI text.
- English UI names are written directly followed by the type, such as `File菜单` or `OK按钮`.
- Menu paths use `|`, for example `【文件】|【另存为】` or `File | Save As`.
- Mouse operations: use `单击`, `双击`, `拖动`, `右击`; avoid `点击`, `拖拽`, and `右单击`.
- Keyboard operations: use `按某某键`; combination keys use `+`, ordered as `Shift`, `Ctrl`, `Alt`.
- Use one term consistently across the full manuscript.

## Special Blocks

- `注意`, `技巧`, and `提示` may use icons or plain text, but the style must be consistent across the book.
- Do not add a colon after `注意`, `技巧`, or `提示`.
- Leave one Chinese-character space after the label, then continue the explanation.
- Use 五号楷体 for the special-block text when possible.
- Wrapped lines in such blocks should align to the left margin used by the block.

## Scope Notes

- The bundled `text_to_docx.py` script applies the core defaults for body text, headings, page setup, and simple headers/footers.
- Complex features such as automatic table of contents, odd/even headers, detailed table borders, images, icons, and true Word template binding may require follow-up editing in Word or a richer document library.
