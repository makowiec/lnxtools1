# installer.py
"""
Skrypt do zarządzania katalogami config i data dla wersji portable
"""
import os
import sys
from pathlib import Path

def setup_directories():
    """Tworzy katalogi config i data obok pliku EXE"""
    # Jeśli uruchomione jako EXE, exe_dir to katalog z exe
    # Jeśli uruchomione jako skrypt, exe_dir to katalog główny
    if getattr(sys, 'frozen', False):
        # Uruchomione z PyInstallera
        exe_dir = Path(sys.executable).parent
    else:
        # Uruchomione z kodu źródłowego
        exe_dir = Path(__file__).parent

    config_dir = exe_dir / "config"
    data_dir = exe_dir / "data"

    # Tworzenie katalogów jeśli nie istnieją
    config_dir.mkdir(exist_ok=True, parents=True)
    data_dir.mkdir(exist_ok=True, parents=True)

    return exe_dir, config_dir, data_dir


if __name__ == "__main__":
    setup_directories()