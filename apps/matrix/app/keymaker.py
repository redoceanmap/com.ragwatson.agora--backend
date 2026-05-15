from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv(Path(__file__).resolve().parents[3] / ".env")

GEMINI_MODEL = "gemini-2.5-flash"


class Keymaker:
    def __init__(self):
        api_key = (os.getenv("GEMINI_API_KEY") or "").strip()
        if api_key:
            genai.configure(api_key=api_key)
            self.gemini: genai.GenerativeModel | None = genai.GenerativeModel(GEMINI_MODEL)
        else:
            self.gemini = None


_keymaker: Keymaker | None = None


def get_keymaker() -> Keymaker:
    global _keymaker
    if _keymaker is None:
        _keymaker = Keymaker()
    return _keymaker
