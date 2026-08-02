#!/usr/bin/env python3
"""Repair the single verified Kali Linux pt-BR heading-style mismatch.

The target paragraph exists in the Portuguese DOCX. This script changes it
from Normal to Heading 1 when needed, accepts an already-repaired Heading 1
state, and fails closed for any other style or duplicate/missing paragraph.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from docx import Document

TARGET_TEXT = "Fundamentos, Carreras e Habilidades Profissionais de Segurança em IA"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    document = Document(args.input)
    matches = [p for p in document.paragraphs if p.text.strip() == TARGET_TEXT]
    if len(matches) != 1:
        raise SystemExit(f"expected exactly one target paragraph, found {len(matches)}")

    paragraph = matches[0]
    current_style = paragraph.style.name if paragraph.style else ""
    if current_style == "Normal":
        paragraph.style = document.styles["Heading 1"]
    elif current_style != "Heading 1":
        raise SystemExit(f"unexpected current style: {current_style!r}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    document.save(args.output)


if __name__ == "__main__":
    main()
