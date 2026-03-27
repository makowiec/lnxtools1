# -*- coding: utf-8 -*-
"""
Modul: lnxtools/gui/main_window.py

Glowne okno programu.
Zawiera menu glowne z mozliwoscia wyboru modulu.
W oknie prezentowane sa logowania systemu z podzialem na kategorie:
INFO, OK, WARNING i ERROR
"""

import sys

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QMessageBox,
)
from PySide6.QtGui import QAction

from src.lnxtools.core.theme_manager import ThemeManager


class MainWindow(QMainWindow):
    """Glowne okno aplikacji lnxtools."""

    def __init__(self):
        super().__init__()

        # Inicjalizacja ThemeManagera
        self.theme_manager = ThemeManager()

        # Nazwa i rozmiary okna
        self.setWindowTitle("Lnxtools")
        self.resize(1100, 700)

        # Tworzenie menu gornego
        self.create_menu_bar()

        # Dodatkowe zabezpieczenie
        self.apply_initial_theme()

        # Centralny widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)

        self.statusBar().showMessage("Gotowy do pracy")

    def create_menu_bar(self):
        """Tworzy pasek menu z pozycjami."""
        menubar = self.menuBar()

        # Menu Bash
        bash_menu = menubar.addMenu("Bash")

        bashsync_action = QAction("BashSync", self)
        bashsync_action.triggered.connect(lambda: self.on_bash_selected("BashSync"))

        bashasync_action = QAction("BashAsync", self)
        bashasync_action.triggered.connect(lambda: self.on_bash_selected("BashAsync"))

        bash_menu.addAction(bashsync_action)
        bash_menu.addAction(bashasync_action)

        # Menu Send
        send_menu = menubar.addMenu("Send")

        send_action = QAction("Send", self)
        send_action.triggered.connect(lambda: self.on_send_selected("Send"))

        send_menu.addAction(send_action)

        # Menu Infra
        infra_menu = menubar.addMenu("Infra")

        infralnximp_action = QAction("LnxImp", self)
        infralnximp_action.triggered.connect(lambda: self.on_infra_selected("LnxImp"))

        infradataimp_action = QAction("DataImp", self)
        infradataimp_action.triggered.connect(lambda: self.on_infra_selected("DataImp"))

        infraraport_action = QAction("Raport", self)
        infraraport_action.triggered.connect(lambda: self.on_infra_selected("Raport"))

        infra_menu.addAction(infralnximp_action)
        infra_menu.addAction(infradataimp_action)
        infra_menu.addAction(infraraport_action)

        # Menu Tools
        tools_menu = menubar.addMenu("Tools")

        toolsarch_action = QAction("Arch", self)
        toolsarch_action.triggered.connect(lambda: self.on_tools_selected("Arch"))

        toolsexport_action = QAction("Export", self)
        toolsexport_action.triggered.connect(lambda: self.on_tools_selected("Export"))

        tools_menu.addAction(toolsarch_action)
        tools_menu.addAction(toolsexport_action)

        # Menu Theme
        theme_menu = menubar.addMenu("Theme")

        # Tryb jasny
        light_action = QAction("Light", self)
        light_action.triggered.connect(lambda: self.change_theme("light"))
        theme_menu.addAction(light_action)

        # Tryb ciemny
        dark_action = QAction("Dark", self)
        dark_action.triggered.connect(lambda: self.change_theme("dark"))
        theme_menu.addAction(dark_action)

        # Menu About
        about_menu = menubar.addMenu("About")

        about_action = QAction("About", self)
        about_action.triggered.connect(lambda: self.on_about_selected("About"))

        about_menu.addAction(about_action)

    # ====================== AKCJE MENU ======================
    def on_bash_selected(self, bash_type: str):
        """Wywolywane po wybraniu Bash1 lub Bash2."""
        QMessageBox.information(self, "Bash", f"Wybrano: {bash_type}\nTutaj w przyszlosci uruchomisz skrypt Bash.")
        self.statusBar().showMessage(f"Wybrano {bash_type}")

    def on_send_selected(self, send_type: str):
        """Wywolywane po wybraniu Send."""
        QMessageBox.information(self, "Send", f"Wybrano: {send_type}\nTutaj w przyszlosci uruchomisz skrypt Send.")
        self.statusBar().showMessage(f"Wybrano {send_type}")

    def on_infra_selected(self, infra_type: str):
        """Wywolywane po wybraniu LnxImp lub DataImp lub Raport."""
        QMessageBox.information(self, "Infra", f"Wybrano: {infra_type}\nTutaj w przyszlosci uruchomisz skrypt Infra.")
        self.statusBar().showMessage(f"Wybrano {infra_type}")

    def on_tools_selected(self, tools_type: str):
        """Wywolywane po wybraniu Arch lub Export."""
        QMessageBox.information(self, "Tools", f"Wybrano: {tools_type}\nTutaj w przyszlosci uruchomisz skrypt Tools.")
        self.statusBar().showMessage(f"Wybrano {tools_type}")

    def change_theme(self, theme_name: str):
        """Zmiana motywu z menu"""
        self.theme_manager.set_theme(theme_name)

    def apply_initial_theme(self):
        """Zapewnia, ze motyw zostanie zastosowany od razu po uruchomieniu"""
        self.theme_manager.apply_global_stylesheet()

    def on_about_selected(self, about_type: str):
        """Wywolywane po wybraniu About."""
        QMessageBox.information(self, "About", f"Wybrano: {about_type}\nTutaj w przyszlosci uruchomisz skrypt About.")
        self.statusBar().showMessage(f"Wybrano {about_type}")


def launch_application() -> None:
    """Funkcja startowa."""
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())