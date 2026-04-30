# -*- coding: utf-8 -*-
"""
Modul: lnxtools/installer.py

Skrypt do zarzadzania katalogami config i data dla wersji portable
"""
import sys
from pathlib import Path


def setup_directories():
    """Tworzy katalogi config i data obok pliku EXE"""
    # Jesli uruchomione jako EXE, exe_dir to katalog z exe
    # Jesli uruchomione jako skrypt, exe_dir to katalog glowny
    if getattr(sys, 'frozen', False):
        # Uruchomione z PyInstallera
        exe_dir = Path(sys.executable).parent
    else:
        # Uruchomione z kodu xrodlowego
        exe_dir = Path(__file__).parent

    config_dir = exe_dir / "config"
    data_dir = exe_dir / "data"

    # Tworzenie katalogow jesli nie istnieja
    config_dir.mkdir(exist_ok=True, parents=True)
    data_dir.mkdir(exist_ok=True, parents=True)

    return exe_dir, config_dir, data_dir


if __name__ == "__main__":
    setup_directories()