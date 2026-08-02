#!/usr/bin/env python3
from __future__ import annotations

import sys
import audit_full_multilingual_parity as audit

_base = audit.token_set


def normalized_tokens(text: str) -> set[str]:
    result = _base(text)
    lowered = text.casefold()
    if "ocde" in lowered:
        result.add("oecd")
    privacy_phrases = (
        "informações de identificação pessoal",
        "informacion de identificacion personal",
        "información de identificación personal",
        "datos de identificación personal",
    )
    if any(phrase in lowered for phrase in privacy_phrases):
        result.add("pii")
    return result


audit.token_set = normalized_tokens

if __name__ == "__main__":
    sys.exit(audit.main())
