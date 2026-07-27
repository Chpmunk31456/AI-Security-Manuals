#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
created = 0

for locale_dir in sorted((ROOT / "manuals").rglob("*")):
    if not locale_dir.is_dir() or locale_dir.name not in {"en", "es-419", "pt-BR"}:
        continue
    readme = locale_dir / "README.md"
    if readme.exists():
        continue
    docx = sorted(locale_dir.glob("*.docx"))
    pdf = sorted(locale_dir.glob("*.pdf"))
    if len(docx) != 1 or len(pdf) != 1:
        continue
    labels = {
        "en": ("English edition", "Download files"),
        "es-419": ("Edición en español latinoamericano", "Descargar archivos"),
        "pt-BR": ("Edição em português do Brasil", "Baixar arquivos"),
    }
    heading, downloads = labels[locale_dir.name]
    content = f"# {heading}\n\n## {downloads}\n\n- [PDF]({pdf[0].name})\n- [DOCX]({docx[0].name})\n\n## Notice\n\nThis educational edition should be validated against current authoritative technical, legal, regulatory, standards, and product sources before operational use.\n"
    readme.write_text(content, encoding="utf-8")
    created += 1

print(f"Created {created} language README files")
