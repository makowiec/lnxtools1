# -*- coding: utf-8 -*-
"""
Modul: lnxtools/core/theme_manager.py

Zarzadzanie motywami.
"""

import json
from src.lnxtools.utils.themes import THEMES
from src.lnxtools.utils.config import SETTINGS_FILE, CONFIG


class ThemeManager:
    def __init__(self, app):
        self.app = app
        self.theme = CONFIG.get("theme", "dark")
        self.apply(self.theme)

    def toggle(self):
        self.theme = "light" if self.theme == "dark" else "dark"
        self.apply(self.theme)
        self.save()

    def apply(self, name):
        self.app.setStyleSheet(THEMES[name])

    def save(self):
        # aktualizacja całego config.json, nie tylko theme
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        data["theme"] = self.theme

        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)