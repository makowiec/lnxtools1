# -*- coding: utf-8 -*-
"""
Modul: lnxtools/core/time_manager.py

Zwraca aktualny czas w formacie RRRRMMDD_HHMMSS
"""

from datetime import datetime

class TimeManager:

    # Zwraca aktualny czas
    def __init__(self):
        self._current_time = None

    @property
    def current_time(self):

        # Zwraca aktualny czas w formacie RRRRMMDD_HHMMSS
        if self._current_time:
            return self._current_time.strftime("%Y%m%d_%H%M%S")
        return None

    def update(self):
        self._current_time = datetime.now()

# Globalna instancja
time_manager = TimeManager()