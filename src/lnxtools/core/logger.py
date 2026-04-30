# -*- coding: utf-8 -*-
"""
Modul: lnxtools/core/logger.py

Loguje zadania z podzialem na kategorie INFO, OK, WARNING i ERROR
"""

from src.lnxtools.core.time_manager import time_manager
from src.lnxtools.utils.paths import LOG_FILE
from src.lnxtools.gui.qt_logger import qt_logger


def log(message: str, level: str = "INFO"):
    """
    Glowna funkcja logująca.

    :param message: Tresc wiadomości do zapisania
    :param level: Poziom logowania (np. INFO, ERROR, WARNING)
    """

    # Aktualizuj czas przed utworzeniem wpisu
    time_manager.update()

    # Tworzenie wpisu loga z timestampem i poziomem
    entry = f"[{time_manager.current_time}] [{level}] {message}\n"

    # Zapis do pliku
    # Otwieranie plik loga w trybie dopisywania (append)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)

    # Wysylanie do GUI
    # Emituje sygnal do loggera GUI
    qt_logger.log_signal.emit(message, level)

# Funkcje pomocnicze
def info(message: str):
    """Logowanie wiadomosci informacyjnej"""
    log(message, level="INFO")

def error(message: str):
    """Logowanie bledu"""
    log(message, level="ERROR")

def warning(message: str):
    """Logowanie ostrzezenia"""
    log(message, level="WARNING")

def ok(message: str):
    """Logowanie poprawnego dzialania"""
    log(message, level="OK")