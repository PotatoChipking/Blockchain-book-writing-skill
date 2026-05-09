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
    "font_size_pt": 12,
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
    "1": { "font_size_pt": 16, "bold": true, "space_before_pt": 12, "space_after_pt": 6 },
    "2": { "font_size_pt": 14, "bold": true, "space_before_pt": 10, "space_after_pt": 6 },
    "3": { "font_size_pt": 13, "bold": true, "space_before_pt": 8, "space_after_pt": 4 },
    "4": { "font_size_pt": 12, "bold": true, "space_before_pt": 6, "space_after_pt": 4 }
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
- `title`: same formatting fields as a paragraph plus `bold`.
- `headings.1` through `headings.4`: heading formatting by level.
- `header`: plain header text.
- `footer`: plain footer text. Use `PAGE` to insert a Word page number field.

## Notes

- The script creates new `.docx` files. It does not edit existing Word files.
- For complex publisher templates, use this script to create a baseline `.docx`, then apply final template-specific adjustments in Word or with a dedicated document library.
- The script uses WordprocessingML directly, so it does not require `python-docx`.
