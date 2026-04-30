# -*- coding: utf-8 -*-
"""
Modul: lnxtools/core/logger.py

Loguje zadania z podzialem na kategorie INFO, OK, WARNING i ERROR
"""

from src.lnxtools.core.time_manager import time_manager
from src.lnxtools.utils.paths import LOG_FILE
from src.lnxtools.gui.qt_logger import qt_logger


def log(message: str, level: str = "INFO"):
    time_manager.update()
    entry = f"[{time_manager.current_time}] [{level}] {message}\n"

    # zapis do pliku
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)

    # wysylanie do GUI
    qt_logger.log_signal.emit(message, level)

# Funkcje pomocnicze
def info(message: str):
    log(message, level="INFO")

def error(message: str):
    log(message, level="ERROR")

def warning(message: str):
    log(message, level="WARNING")

def ok(message: str):
    log(message, level="OK")