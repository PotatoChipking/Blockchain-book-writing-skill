# Format Spec Reference

Pass a JSON file to `scripts/text_to_docx.py --spec format.json`. All fields are optional.

## Example

```json
{
  "page": {
    "size": "A4",
    "margin_top_cm": 2.54,
    "margin_bottom_cm": 2.54,
    "margin_left_cm": 3.0,
    "margin_right_cm": 3.0
  },
  "fonts": {
    "east_asia": "SimSun",
    "latin": "Times New Roman"
  },
  "body": {
    "font_size_pt": 10.5,
    "line_spacing": 1.5,
    "first_line_indent_chars": 2,
    "alignment": "both",
    "space_after_pt": 0
  },
  "title": {
    "font_size_pt": 18,
    "bold": true,
    "alignment": "center",
    "space_after_pt": 18
  },
  "headings": {
    "1": { "font_size_pt": 16, "bold": true, "east_asia_font": "SimSun", "latin_font": "SimSun", "space_before_pt": 12, "space_after_pt": 6 },
    "2": { "font_size_pt": 14, "bold": false, "east_asia_font": "KaiTi_GB2312", "latin_font": "KaiTi_GB2312", "space_before_pt": 10, "space_after_pt": 6 },
    "3": { "font_size_pt": 12, "bold": true, "east_asia_font": "SimHei", "latin_font": "SimHei", "space_before_pt": 8, "space_after_pt": 4 },
    "4": { "font_size_pt": 12, "bold": true, "east_asia_font": "SimSun", "latin_font": "SimSun", "space_before_pt": 6, "space_after_pt": 4 }
  },
  "header": "内部审阅稿",
  "footer": "第 PAGE 页"
}
```

## Supported Fields

- `page.size`: `A4` or `Letter`.
- `page.margin_top_cm`, `page.margin_bottom_cm`, `page.margin_left_cm`, `page.margin_right_cm`: page margins in centimeters.
- `fonts.east_asia`: Chinese font name, such as `SimSun`, `Microsoft YaHei`, `Songti SC`, or `FangSong`.
- `fonts.latin`: Latin font name, such as `Times New Roman`, `Calibri`, or `Arial`.
- `body.font_size_pt`: body font size in points.
- `body.line_spacing`: multiplier such as `1.0`, `1.15`, `1.5`, or `2.0`.
- `body.first_line_indent_chars`: approximate first-line indent in Chinese characters.
- `body.alignment`: `left`, `center`, `right`, or `both`.
- `body.space_before_pt`, `body.space_after_pt`: paragraph spacing in points.
- `title`: same formatting fields as a paragraph plus `bold`, `east_asia_font`, and `latin_font`.
- `headings.1` through `headings.4`: heading formatting by level. Use `latin_font` equal to `east_asia_font` when matching the publisher rule that heading English and numbers use the same font as heading Chinese text.
- `header`: plain header text.
- `footer`: plain footer text. Use `PAGE` to insert a Word page number field.

## Notes

- The script creates new `.docx` files. It does not edit existing Word files.
- The script can append new text to an existing `.docx` with `--append-to existing.docx --output output.docx`. Appending preserves the existing package and inserts new generated paragraphs before the document section properties.
- Inline markers of the form `（批注：source note）` are converted into true Word footnotes when creating a new `.docx`: the body contains a footnote reference number, and `source note` is written into `word/footnotes.xml`. Use these markers for source-backed manuscript references.
- When validating footnote output, inspect `word/document.xml` for `w:footnoteReference` and `word/footnotes.xml` for matching `w:footnote` entries.
- The built-in defaults follow `references/publisher-default-format.md`: 宋体五号 body text, Times New Roman body English/numbers, 1.5 line spacing, first-line indent of 2 Chinese characters, justified body text, 楷体_GB2312 四号 second-level headings, and 黑体小四加粗 third-level headings.
- For complex publisher templates, use this script to create a baseline `.docx`, then apply final template-specific adjustments in Word or with a dedicated document library.
- The script uses WordprocessingML directly, so it does not require `python-docx`.
