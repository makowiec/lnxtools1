# -*- coding: utf-8 -*-
"""
lnxtools - zbior narzedzi wspomagajacych administrowanie serwerami linux

Glowny punkt wejscia aplikacji.
Uruchamia interfejs graficzny (GUI).

Ten plik jest odpowiedzialny wylacznie za start aplikacji.
Cala logika GUI znajduje sie w gui/, a logika biznesowa w core/.

Wersja: 0.1.0
Autor: Lukasz M
Data utworzenia: 24-03-2026
"""

__version__ = "0.1.0"
__author__ = "Lukasz M"

import sys
from pathlib import Path

# Dodanie sciezki do src na potrzeby pyCharm i Python by byl widzialy katalog lnxtools
root = Path(__file__).resolve().parents[2]  # przejscie dwa pozimy w gore
if str(root) not in sys.path:
    sys.path.insert(0, str(root))


def main() -> None:
    """Glowna funkcja uruchamiajaca aplikację GUI"""
    # Import GUI
    from src.lnxtools.gui.main_window import launch_application

    launch_application()


if __name__ == "__main__":
    main()