# -*- coding: utf-8 -*-
"""
Modul: lnxtools/utils/paths.py

Zawiera globalne sciezki dla programu.
"""

from pathlib import Path

# Glowny katalog aplikacji (portable)
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Katalogi poza src/
DATA_DIR = BASE_DIR / "data"
CONFIG_DIR = BASE_DIR / "config"
LOGS_DIR = DATA_DIR / "logs"

# Tworzenie katalogow (bezpieczne przy kazdym imporcie)
for directory in (DATA_DIR, CONFIG_DIR, LOGS_DIR):
    directory.mkdir(parents=True, exist_ok=True)

# Plik ustawien uzytkownika
SETTINGS_FILE = CONFIG_DIR / "settings.json"

# Katalog na szablony / dane aplikacji (opcjonalnie)
TEMPLATES_DIR = DATA_DIR / "templates"
TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)


# Pomocnicze funkcje (jesli beda potrzebne)
def get_base_dir() -> Path:
    return BASE_DIR

def get_data_dir() -> Path:
    return DATA_DIR

def get_config_dir() -> Path:
    return CONFIG_DIR