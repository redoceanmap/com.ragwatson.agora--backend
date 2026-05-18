from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

load_dotenv(Path(__file__).resolve().parents[3] / ".env")

GEMINI_MODEL = "gemini-2.5-flash"


class Keymaker:
    def __init__(self):
        api_key = (os.getenv("GEMINI_API_KEY") or "").strip()
        if api_key:
            self.client: genai.Client | None = genai.Client(api_key=api_key)
        else:
            self.client = None


_keymaker: Keymaker | None = None


def get_keymaker() -> Keymaker:
    global _keymaker
    if _keymaker is None:
        _keymaker = Keymaker()
    return _keymaker
