# build.py
"""
Skrypt do budowania przenośnego pliku EXE
"""
import PyInstaller.__main__
import os
import sys


def build_executable():
    """Buduje przenośny plik EXE"""

    # Parametry PyInstallera
    params = [
        'main.py',  # Główny plik wejścia
        '--name=lnxtools',  # Nazwa aplikacji
        '--windowed',  # Bez konsoli (dla GUI)
        '--onefile',  # Jeden plik EXE
        '--add-data=src:src',  # Dodaj katalog src
        '--add-data=config:config',  # Dodaj katalog config
        '--add-data=data:data',  # Dodaj katalog data
        '--add-data=src/lnxtools/resources/icons/lnxtools.ico:src/lnxtools/resources/icons',  # Dodaj resources z ikoną
        '--hidden-import=PySide6',  # Ukryte importy
        '--icon=src/lnxtools/resources/icons/lnxtools.ico',  # Ikona (dla EXE)
        '--distpath=dist',  # Katalog wyjściowy
        '--workpath=build',  # Katalog budowania
        '--specpath=.',  # Katalog spec
    ]

    PyInstaller.__main__.run(params)

    print("\n" + "=" * 50)
    print("Budowanie zakończone!")
    print("=" * 50)
    print("Plik EXE znajduje się w: dist/lnxtools.exe")
    print("\nAby rozprowadzać aplikację:")
    print("1. Skopiuj plik dist/lnxtools.exe do wyznaczonego katalogu")
    print("2. Katalogi 'config' i 'data' zostaną utworzone automatycznie")
    print("=" * 50)


if __name__ == "__main__":
    build_executable()