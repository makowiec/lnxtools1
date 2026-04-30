# -*- coding: utf-8 -*-
"""
Modul: lnxtools/core/time_manager.py

Zarzadza biezacym czasem aplikacji.
Umozliwia jego aktualizacje oraz zwracanie w formacie: RRRRMMDD_HHMMSS
"""

from datetime import datetime

class TimeManager:
    """
    Klasa odpowiedzialna za przechowywanie i aktualizacje biezacego czasu.
    """

    def __init__(self):
        # Prywatne pole przechowujace aktualny czas (obiekt datetime)
        self._current_time = None

    @property
    def current_time(self):
        """
        Zwraca aktualny czas w formacie: RRRRMMDD_HHMMSS

        :return: sformatowany czas jako string lub None jesli nie ustawiono czasu
        """

        # Jesli czas zostal wczesniej ustawiony zwroc go w odpowiednim formacie
        if self._current_time:
            return self._current_time.strftime("%Y%m%d_%H%M%S")
        return None

    def update(self):
        """
        Aktualizuje aktualny czas na biezacy czas systemowy.
        """
        self._current_time = datetime.now()

# Globalna instancja menedzera czasu
# Dzieki temu mozna korzystac z jednego wspolnego obiektu w calej aplikacji
time_manager = TimeManager()