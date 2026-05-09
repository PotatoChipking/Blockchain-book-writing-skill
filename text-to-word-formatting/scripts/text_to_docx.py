#!/usr/bin/env python3
"""Create a formatted .docx from plain text using only the standard library."""

from __future__ import annotations

import argparse
import html
import json
import re
import zipfile
from pathlib import Path
from typing import Any


NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}


DEFAULT_SPEC: dict[str, Any] = {
    "page": {
        "size": "A4",
        "margin_top_cm": 2.54,
        "margin_bottom_cm": 2.54,
        "margin_left_cm": 2.54,
        "margin_right_cm": 2.54,
    },
    "fonts": {"east_asia": "SimSun", "latin": "Times New Roman"},
    "body": {
        "font_size_pt": 12,
        "line_spacing": 1.5,
        "first_line_indent_chars": 2,
        "alignment": "both",
        "space_before_pt": 0,
        "space_after_pt": 0,
    },
    "title": {
        "font_size_pt": 18,
        "bold": True,
        "alignment": "center",
        "space_before_pt": 0,
        "space_after_pt": 18,
    },
    "headings": {
        "1": {"font_size_pt": 16, "bold": True, "space_before_pt": 12, "space_after_pt": 6},
        "2": {"font_size_pt": 14, "bold": True, "space_before_pt": 10, "space_after_pt": 6},
        "3": {"font_size_pt": 13, "bold": True, "space_before_pt": 8, "space_after_pt": 4},
        "4": {"font_size_pt": 12, "bold": True, "space_before_pt": 6, "space_after_pt": 4},
    },
    "header": "",
    "footer": "",
}


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    result = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def cm_to_twips(value: float) -> int:
    return round(value * 567)


def pt_to_half_points(value: float) -> int:
    return round(value * 2)


def pt_to_twips(value: float) -> int:
    return round(value * 20)


def line_spacing_to_twips(value: float) -> int:
    return round(value * 240)


def chars_to_twips(chars: float, font_size_pt: float) -> int:
    return round(chars * font_size_pt * 20)


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def paragraph_style(name: str, fmt: dict[str, Any], fonts: dict[str, str]) -> str:
    size = pt_to_half_points(float(fmt.get("font_size_pt", 12)))
    bold = "<w:b/>" if fmt.get("bold") else ""
    return f"""
    <w:style w:type="paragraph" w:styleId="{name}">
      <w:name w:val="{name}"/>
      <w:qFormat/>
      <w:rPr>
        <w:rFonts w:ascii="{esc(fonts['latin'])}" w:hAnsi="{esc(fonts['latin'])}" w:eastAsia="{esc(fonts['east_asia'])}"/>
        {bold}
        <w:sz w:val="{size}"/>
        <w:szCs w:val="{size}"/>
      </w:rPr>
    </w:style>"""


def styles_xml(spec: dict[str, Any]) -> str:
    fonts = spec["fonts"]
    styles = [
        paragraph_style("BodyText", spec["body"], fonts),
        paragraph_style("DocTitle", spec["title"], fonts),
        paragraph_style("ListParagraph", spec["body"], fonts),
    ]
    for level in range(1, 5):
        styles.append(paragraph_style(f"Heading{level}", spec["headings"].get(str(level), {}), fonts))
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="{NS['w']}">
  <w:docDefaults>
    <w:rPrDefault>
      <w:rPr>
        <w:rFonts w:ascii="{esc(fonts['latin'])}" w:hAnsi="{esc(fonts['latin'])}" w:eastAsia="{esc(fonts['east_asia'])}"/>
      </w:rPr>
    </w:rPrDefault>
  </w:docDefaults>
  {''.join(styles)}
</w:styles>"""


def run_xml(text: str, fmt: dict[str, Any], spec: dict[str, Any]) -> str:
    size = pt_to_half_points(float(fmt.get("font_size_pt", spec["body"]["font_size_pt"])))
    bold = "<w:b/>" if fmt.get("bold") else ""
    preserve = ' xml:space="preserve"' if text.startswith(" ") or text.endswith(" ") else ""
    fonts = spec["fonts"]
    return f"""<w:r>
      <w:rPr>
        <w:rFonts w:ascii="{esc(fonts['latin'])}" w:hAnsi="{esc(fonts['latin'])}" w:eastAsia="{esc(fonts['east_asia'])}"/>
        {bold}
        <w:sz w:val="{size}"/>
        <w:szCs w:val="{size}"/>
      </w:rPr>
      <w:t{preserve}>{esc(text)}</w:t>
    </w:r>"""


def paragraph_xml(text: str, style: str, fmt: dict[str, Any], spec: dict[str, Any], bullet: bool = False) -> str:
    body = spec["body"]
    align = fmt.get("alignment", body.get("alignment", "left"))
    before = pt_to_twips(float(fmt.get("space_before_pt", body.get("space_before_pt", 0))))
    after = pt_to_twips(float(fmt.get("space_after_pt", body.get("space_after_pt", 0))))
    line = line_spacing_to_twips(float(fmt.get("line_spacing", body.get("line_spacing", 1.0))))
    indent = ""
    if style == "BodyText" and not bullet:
        first = chars_to_twips(float(body.get("first_line_indent_chars", 0)), float(body.get("font_size_pt", 12)))
        if first:
            indent = f'<w:ind w:firstLine="{first}"/>'
    if bullet:
        indent = '<w:ind w:left="720" w:hanging="360"/>'
        text = f"• {text}"
    return f"""<w:p>
      <w:pPr>
        <w:pStyle w:val="{style}"/>
        <w:jc w:val="{align}"/>
        <w:spacing w:before="{before}" w:after="{after}" w:line="{line}" w:lineRule="auto"/>
        {indent}
      </w:pPr>
      {run_xml(text, fmt, spec)}
    </w:p>"""


def empty_paragraph_xml() -> str:
    return "<w:p/>"


def detect_line(line: str) -> tuple[str, int, str]:
    stripped = line.strip()
    md = re.match(r"^(#{1,4})\s+(.+)$", stripped)
    if md:
        return "heading", len(md.group(1)), md.group(2).strip()
    numbered = re.match(r"^(\d+(?:\.\d+){0,3})[.、]?\s+(.+)$", stripped)
    if numbered:
        return "heading", min(numbered.group(1).count(".") + 1, 4), stripped
    bullet = re.match(r"^[-*•]\s+(.+)$", stripped)
    if bullet:
        return "bullet", 0, bullet.group(1).strip()
    return "body", 0, stripped


def build_document_xml(text: str, title: str | None, spec: dict[str, Any]) -> str:
    parts: list[str] = []
    if title:
        parts.append(paragraph_xml(title, "DocTitle", spec["title"], spec))
    for raw_line in text.splitlines():
        if not raw_line.strip():
            parts.append(empty_paragraph_xml())
            continue
        kind, level, content = detect_line(raw_line)
        if kind == "heading":
            fmt = spec["headings"].get(str(level), spec["headings"]["4"])
            parts.append(paragraph_xml(content, f"Heading{level}", fmt, spec))
        elif kind == "bullet":
            parts.append(paragraph_xml(content, "ListParagraph", spec["body"], spec, bullet=True))
        else:
            parts.append(paragraph_xml(content, "BodyText", spec["body"], spec))

    page = spec["page"]
    if page.get("size", "A4").upper() == "LETTER":
        width, height = 12240, 15840
    else:
        width, height = 11906, 16838
    margins = {
        "top": cm_to_twips(float(page.get("margin_top_cm", 2.54))),
        "bottom": cm_to_twips(float(page.get("margin_bottom_cm", 2.54))),
        "left": cm_to_twips(float(page.get("margin_left_cm", 2.54))),
        "right": cm_to_twips(float(page.get("margin_right_cm", 2.54))),
    }
    header_ref = '<w:headerReference w:type="default" r:id="rIdHeader"/>' if spec.get("header") else ""
    footer_ref = '<w:footerReference w:type="default" r:id="rIdFooter"/>' if spec.get("footer") else ""
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="{NS['w']}" xmlns:r="{NS['r']}">
  <w:body>
    {''.join(parts)}
    <w:sectPr>
      {header_ref}
      {footer_ref}
      <w:pgSz w:w="{width}" w:h="{height}"/>
      <w:pgMar w:top="{margins['top']}" w:right="{margins['right']}" w:bottom="{margins['bottom']}" w:left="{margins['left']}" w:header="708" w:footer="708" w:gutter="0"/>
    </w:sectPr>
  </w:body>
</w:document>"""


def header_footer_xml(text: str, spec: dict[str, Any], footer: bool = False) -> str:
    tag = "ftr" if footer else "hdr"
    if footer and "PAGE" in text:
        before, after = text.split("PAGE", 1)
        runs = run_xml(before, spec["body"], spec)
        runs += '<w:r><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:instrText> PAGE </w:instrText></w:r><w:r><w:fldChar w:fldCharType="end"/></w:r>'
        runs += run_xml(after, spec["body"], spec)
    else:
        runs = run_xml(text, spec["body"], spec)
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:{tag} xmlns:w="{NS['w']}" xmlns:r="{NS['r']}">
  <w:p>
    <w:pPr><w:jc w:val="center"/></w:pPr>
    {runs}
  </w:p>
</w:{tag}>"""


def relationships_xml(spec: dict[str, Any]) -> str:
    rels = [
        '<Relationship Id="rIdStyles" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
    ]
    if spec.get("header"):
        rels.append('<Relationship Id="rIdHeader" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="header1.xml"/>')
    if spec.get("footer"):
        rels.append('<Relationship Id="rIdFooter" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>')
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  {''.join(rels)}
</Relationships>"""


def content_types_xml(spec: dict[str, Any]) -> str:
    overrides = [
        '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>',
        '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>',
        '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>',
        '<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>',
    ]
    if spec.get("header"):
        overrides.append('<Override PartName="/word/header1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>')
    if spec.get("footer"):
        overrides.append('<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>')
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  {''.join(overrides)}
</Types>"""


def root_rels_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>"""


def core_xml(title: str | None) -> str:
    safe_title = esc(title or "Document")
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>{safe_title}</dc:title>
  <dc:creator>Codex</dc:creator>
</cp:coreProperties>"""


def app_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Codex</Application>
</Properties>"""


def create_docx(input_path: Path, output_path: Path, spec: dict[str, Any], title: str | None) -> None:
    text = input_path.read_text(encoding="utf-8")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", content_types_xml(spec))
        docx.writestr("_rels/.rels", root_rels_xml())
        docx.writestr("docProps/core.xml", core_xml(title))
        docx.writestr("docProps/app.xml", app_xml())
        docx.writestr("word/document.xml", build_document_xml(text, title, spec))
        docx.writestr("word/_rels/document.xml.rels", relationships_xml(spec))
        docx.writestr("word/styles.xml", styles_xml(spec))
        if spec.get("header"):
            docx.writestr("word/header1.xml", header_footer_xml(str(spec["header"]), spec))
        if spec.get("footer"):
            docx.writestr("word/footer1.xml", header_footer_xml(str(spec["footer"]), spec, footer=True))


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a formatted .docx from plain text.")
    parser.add_argument("--input", required=True, type=Path, help="UTF-8 text input file")
    parser.add_argument("--output", required=True, type=Path, help="Output .docx path")
    parser.add_argument("--spec", type=Path, help="Optional JSON formatting spec")
    parser.add_argument("--title", help="Optional document title")
    args = parser.parse_args()

    spec = DEFAULT_SPEC
    if args.spec:
        spec = deep_merge(DEFAULT_SPEC, json.loads(args.spec.read_text(encoding="utf-8")))
    create_docx(args.input, args.output, spec, args.title)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
