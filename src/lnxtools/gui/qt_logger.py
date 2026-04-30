# -*- coding: utf-8 -*-
"""
Modul: lnxtools/gui/qt_logger.py


Odpowiada za przekazywanie komunikatow logowania do interfejsu graficznego (Qt).
Wykorzystuje mechanizm sygnalow Qt (Signal), aby komunikowac sie z GUI.
"""

from PySide6.QtCore import QObject, Signal

class QtLogger(QObject):
    """
    Klasa loggera dla GUI.

    Dziedziczy po QObject, aby moc korzystac z systemu sygnalow Qt.
    """

    # Definicja sygnalu logowania
    # Przekazuje:
    # - message (str): tresc loga
    # - level (str): poziom logowania (np. INFO, ERROR)
    log_signal = Signal(str, str)  # message, level

# Globalna instancja loggera GUI
# Umozliwia latwy dostep i wysylanie logow z roznych czesci aplikacji
qt_logger = QtLogger()