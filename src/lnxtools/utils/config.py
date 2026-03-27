# -*- coding: utf-8 -*-
"""
Modul: lnxtools/utils/config.py

Zawiera zmienne i ustawienia globalne dla programu.
"""

import json
import shutil
from pathlib import Path

# Glowny katalog aplikacji
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Katalogi poza src
DATA_DIR = BASE_DIR / "data"
CONFIG_DIR = BASE_DIR / "config"
LOGS_DIR = DATA_DIR / "logs"

for directory in (DATA_DIR, CONFIG_DIR, LOGS_DIR):
    directory.mkdir(parents=True, exist_ok=True)

# Katalogi src
SRC_DIR = BASE_DIR / "src"
LNXTOOLS_DIR = SRC_DIR / "lnxtools"
CORE_DIR = LNXTOOLS_DIR / "core"
GUI_DIR = LNXTOOLS_DIR / "gui"
TEMPLATES_DIR = LNXTOOLS_DIR / "templates"

# Ustawienia uzytkownika lub domyslne
SETTINGS_FILE = CONFIG_DIR / "settings.json"
DEFAULT_SETTINGS_FILE = TEMPLATES_DIR / "settings.default.json"

# Pierwsze uruchomienie – kopiowanie settings.default.json
if not SETTINGS_FILE.exists():
    shutil.copy(DEFAULT_SETTINGS_FILE, SETTINGS_FILE)

# Wczytanie konfiguracji
with open(DEFAULT_SETTINGS_FILE, "r", encoding="utf-8") as f:
    _defaults = json.load(f)

with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
    _user = json.load(f)

# Merge: user > defaults
CONFIG = {**_defaults, **_user}