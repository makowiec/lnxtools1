# -*- coding: utf-8 -*-
"""
Modul: lnxtools/build.py

Skrypt do budowania pliku EXE w wersji portable
"""
import PyInstaller.__main__


def build_executable():
    """Buduje plik EXE w wersji portable"""

    # Parametry PyInstallera
    params = [
        'main.py',  # Glowny plik wejscia
        '--name=lnxtools',  # Nazwa aplikacji
        '--windowed',  # Bez konsoli (dla GUI)
        '--onefile',  # Jeden plik EXE
        '--add-data=config:config',  # Dodanie katalogu config
        '--add-data=data:data',  # Dodanie katalogu data
        '--add-data=src/lnxtools/resources/icons/lnxtools.ico:resources/icons',  # Dodanie resources z ikona
        '--hidden-import=PySide6',  # Ukryte importy
        '--icon=src/lnxtools/resources/icons/lnxtools.ico',  # Ikona dla pliku EXE
        '--distpath=dist',  # Katalog wyjsciowy
        '--workpath=build',  # Katalog budowania
        '--specpath=.',  # Katalog spec
    ]

    PyInstaller.__main__.run(params)

    print("\n" + "=" * 50)
    print("Budowanie zakobczone!")
    print("=" * 50)
    print("Plik EXE znajduje się w: dist/lnxtools.exe")
    print("\nAby rozprowadzac aplikację:")
    print("1. Skopiuj plik dist/lnxtools.exe do wyznaczonego katalogu")
    print("2. Katalogi 'config' i 'data' zostana utworzone automatycznie")
    print("=" * 50)


if __name__ == "__main__":
    build_executable()