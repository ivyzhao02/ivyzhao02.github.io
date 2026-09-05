#!/usr/bin/env python3
"""Validate the dependency-free ivyzhao.ca source before publishing."""

from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = sorted(ROOT.glob("*.html"))
SITE_URL = "https://ivyzhao.ca"
GOOGLE_TAG_ID = "G-XYHKNGK1D8"
GOOGLE_TAG_SRC = f"https://www.googletagmanager.com/gtag/js?id={GOOGLE_TAG_ID}"
REQUIRED_META_NAMES = {
    "description",
    "theme-color",
    "twitter:card",
    "twitter:title",
    "twitter:description",
    "twitter:image",
    "twitter:image:alt",
}
REQUIRED_META_PROPERTIES = {
    "og:title",
    "og:description",
    "og:type",
    "og:site_name",
    "og:locale",
    "og:url",
    "og:image",
    "og:image:width",
    "og:image:height",
    "og:image:alt",
}
MOJIBAKE_MARKERS = ("\ufffd", "\u00c3\u00a2", "\u00e2\u20ac", "\u00c2\u00a0")


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.references: list[tuple[str, str]] = []
        self.h1_count = 0
        self.images_without_alt = 0
        self.meta_names: set[str] = set()
        self.meta_properties: set[str] = set()
        self.canonicals: list[str] = []
        self.json_ld_blocks: list[str] = []
        self.target_blank_without_rel: list[str] = []
        self._json_ld_depth = 0
        self._json_ld_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if element_id := attributes.get("id"):
            self.ids.add(element_id)
        if tag == "h1":
            self.h1_count += 1
        if tag == "meta":
            if name := attributes.get("name"):
                self.meta_names.add(name)
            if prop := attributes.get("property"):
                self.meta_properties.add(prop)
        if tag == "link" and "canonical" in (attributes.get("rel") or "").split():
            if href := attributes.get("href"):
                self.canonicals.append(href)
        if tag == "img" and "alt" not in attributes:
            self.images_without_alt += 1
        for attribute in ("href", "src", "poster"):
            if value := attributes.get(attribute):
                self.references.append((attribute, value))
        if attributes.get("target") == "_blank":
            rel = set((attributes.get("rel") or "").split())
            if "noopener" not in rel:
                self.target_blank_without_rel.append(attributes.get("href", "unknown link"))
        if tag == "script" and attributes.get("type") == "application/ld+json":
            self._json_ld_depth = 1
            self._json_ld_parts = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._json_ld_depth:
            self.json_ld_blocks.append("".join(self._json_ld_parts))
            self._json_ld_depth = 0

    def handle_data(self, data: str) -> None:
        if self._json_ld_depth:
            self._json_ld_parts.append(data)


def expected_url(path: Path) -> str:
    return f"{SITE_URL}/" if path.name == "index.html" else f"{SITE_URL}/{path.name}"


def local_target(page: Path, reference: str) -> tuple[Path, str]:
    parsed = urlsplit(reference)
    target_path = unquote(parsed.path)
    if not target_path:
        target = page
    elif target_path.startswith("/"):
        target = ROOT / target_path.lstrip("/")
    else:
        target = page.parent / target_path
    if target.is_dir():
        target /= "index.html"
    return target.resolve(), unquote(parsed.fragment)


def validate_page(page: Path, errors: list[str], parsed_pages: dict[Path, PageParser]) -> None:
    try:
        raw = page.read_bytes()
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        errors.append(f"{page.name}: not valid UTF-8 ({exc})")
        return

    for marker in MOJIBAKE_MARKERS:
        if marker in text:
            errors.append(f"{page.name}: possible mojibake marker {marker!r}")

    parser = PageParser()
    parser.feed(text)
    parsed_pages[page.resolve()] = parser

    if parser.h1_count != 1:
        errors.append(f"{page.name}: expected one h1, found {parser.h1_count}")
    if parser.images_without_alt:
        errors.append(f"{page.name}: {parser.images_without_alt} image(s) lack alt text")

    missing_names = REQUIRED_META_NAMES - parser.meta_names
    missing_properties = REQUIRED_META_PROPERTIES - parser.meta_properties
    if missing_names:
        errors.append(f"{page.name}: missing meta names {sorted(missing_names)}")
    if missing_properties:
        errors.append(f"{page.name}: missing Open Graph properties {sorted(missing_properties)}")
    if parser.canonicals != [expected_url(page)]:
        errors.append(f"{page.name}: canonical should be {expected_url(page)!r}")
    if parser.target_blank_without_rel:
        errors.append(
            f"{page.name}: target=_blank link(s) lack rel=noopener: "
            + ", ".join(parser.target_blank_without_rel)
        )

    if text.count(GOOGLE_TAG_SRC) != 1:
        errors.append(f"{page.name}: expected one Google tag loader for {GOOGLE_TAG_ID}")
    config_pattern = rf"gtag\(\s*['\"]config['\"]\s*,\s*['\"]{re.escape(GOOGLE_TAG_ID)}['\"]\s*\)"
    if len(re.findall(config_pattern, text)) != 1:
        errors.append(f"{page.name}: expected one Google tag config for {GOOGLE_TAG_ID}")

    for block in parser.json_ld_blocks:
        try:
            json.loads(block)
        except json.JSONDecodeError as exc:
            errors.append(f"{page.name}: invalid JSON-LD ({exc})")

    for attribute, reference in parser.references:
        parsed = urlsplit(reference)
        if parsed.scheme in {"http", "https", "mailto", "tel", "data"} or reference.startswith("//"):
            continue
        target, fragment = local_target(page, reference)
        if not target.exists():
            errors.append(f"{page.name}: missing {attribute} target {reference!r}")
            continue
        if fragment and target.suffix.lower() == ".html":
            target_parser = parsed_pages.get(target)
            if target_parser is None:
                target_parser = PageParser()
                target_parser.feed(target.read_text(encoding="utf-8"))
                parsed_pages[target] = target_parser
            if fragment not in target_parser.ids:
                errors.append(f"{page.name}: missing fragment #{fragment} in {target.name}")


def validate_sitemap(errors: list[str]) -> None:
    sitemap = ROOT / "sitemap.xml"
    try:
        tree = ET.parse(sitemap)
    except (ET.ParseError, OSError) as exc:
        errors.append(f"sitemap.xml: could not parse ({exc})")
        return
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    actual = {element.text for element in tree.findall("sm:url/sm:loc", namespace)}
    expected = {expected_url(path) for path in HTML_FILES}
    if actual != expected:
        errors.append(
            "sitemap.xml: URL mismatch; "
            f"missing={sorted(expected - actual)}, extra={sorted(actual - expected)}"
        )


def validate_shared_content(errors: list[str]) -> None:
    combined = "\n".join(path.read_text(encoding="utf-8") for path in HTML_FILES)
    stale_claims = (
        "1,450",
        "Community Management Lead &middot; Operations",
        "ChatGPT",
        "Codex",
    )
    for claim in stale_claims:
        if claim in combined:
            errors.append(f"site: stale public claim remains: {claim!r}")

    home = (ROOT / "index.html").read_text(encoding="utf-8")
    if '"@type": "Person"' not in home:
        errors.append("index.html: Person JSON-LD is missing")

    stylesheet = (ROOT / "style.css").read_text(encoding="utf-8")
    if "fonts.googleapis.com" in stylesheet or "fonts.gstatic.com" in stylesheet:
        errors.append("style.css: fonts should load from the local assets/fonts directory")

    for asset in (
        "assets/ivy-zhao-resume.pdf",
        "assets/ivy-zhao-resume-page-1.png",
        "assets/ivy-zhao-resume-page-1.webp",
        "assets/ivyzhao-social-preview.png",
        "assets/favicon.svg",
        "assets/apple-touch-icon.png",
        "assets/fonts/dm-sans-latin.woff2",
        "assets/fonts/newsreader-latin.woff2",
    ):
        path = ROOT / asset
        if not path.exists() or path.stat().st_size < 100:
            errors.append(f"site: required asset is missing or empty: {asset}")


def main() -> int:
    errors: list[str] = []
    parsed_pages: dict[Path, PageParser] = {}
    for page in HTML_FILES:
        validate_page(page, errors, parsed_pages)
    validate_sitemap(errors)
    validate_shared_content(errors)

    if errors:
        print("Site validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Validated {len(HTML_FILES)} HTML pages, Google tag coverage, local references, "
        "metadata, UTF-8, and sitemap coverage."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
