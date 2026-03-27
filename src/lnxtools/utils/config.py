# -*- coding: utf-8 -*-
"""
Modul: lnxtools/utils/config.py

Zawiera zmienne i ustawienia globalne dla programu.
"""

import json
from src.lnxtools.utils.paths import SETTINGS_FILE

# Domyslne ustawienia aplikacji – wszystkie nowe ustawienia dodajemy tutaj
DEFAULT_SETTINGS = {
    "theme": "dark",
    "language": "pl",
    "window_geometry": None,      # [x, y, width, height]
    "maximized": False,
    "last_used_tool": None,
    "show_tooltips": True,
}


def load_settings() -> dict:
    """
    Wczytuje ustawienia uzytkownika.
    Przy pierwszym uruchomieniu tworzy plik settings.json z wartosciami domyslnymi.
    """
    if not SETTINGS_FILE.exists():
        print("→ Tworze nowy plik settings.json z ustawieniami domyslnymi.")
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS.copy()

    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            user_settings = json.load(f)

        # Bezpieczny merge: DEFAULT_SETTINGS + ustawienia uzytkownika (uzytkownik nadpisuje)
        merged = DEFAULT_SETTINGS.copy()
        merged.update(user_settings)
        return merged

    except Exception as e:
        print(f"Uwaga: Blad odczytu settings.json ({e}). Tworze nowy plik z domyslnymi ustawieniami.")
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS.copy()


def save_settings(settings: dict) -> None:
    """
    Zapisuje ustawienia do pliku config/settings.json
    """
    try:
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(settings, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Blad zapisu settings.json: {e}")