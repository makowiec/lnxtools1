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
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QMessageBox,
)
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    """Główne okno aplikacji lnxtools."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lnxtools")
        self.resize(1100, 700)

        # Tworzenie menu gornego
        self._create_menu_bar()

        # Centralny widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)

        self.statusBar().showMessage("Gotowy do pracy")

    def _create_menu_bar(self):
        """Tworzy pasek menu z pozycjami Bash i Send."""
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

        themelight_action = QAction("Light", self)
        themelight_action.triggered.connect(lambda: self.on_theme_selected("Light"))

        themedark_action = QAction("Dark", self)
        themedark_action.triggered.connect(lambda: self.on_theme_selected("Dark"))

        theme_menu.addAction(themelight_action)
        theme_menu.addAction(themedark_action)

        # Menu About
        about_menu = menubar.addMenu("About")

        about_action = QAction("About", self)
        about_action.triggered.connect(lambda: self.on_about_selected("About"))

        about_menu.addAction(about_action)

    # ====================== AKCJE MENU ======================
    def on_bash_selected(self, bash_type: str):
        """Wywoływane po wybraniu Bash1 lub Bash2."""
        QMessageBox.information(self, "Bash", f"Wybrano: {bash_type}\nTutaj w przyszłości uruchomisz skrypt Bash.")
        self.statusBar().showMessage(f"Wybrano {bash_type}")

    def on_send_selected(self, send_type: str):
        """Wywoływane po wybraniu Send."""
        QMessageBox.information(self, "Send", f"Wybrano: {send_type}\nTutaj w przyszłości uruchomisz skrypt Send.")
        self.statusBar().showMessage(f"Wybrano {send_type}")

    def on_infra_selected(self, infra_type: str):
        """Wywoływane po wybraniu LnxImp lub DataImp lub Raport."""
        QMessageBox.information(self, "Infra", f"Wybrano: {infra_type}\nTutaj w przyszłości uruchomisz skrypt Infra.")
        self.statusBar().showMessage(f"Wybrano {infra_type}")

    def on_tools_selected(self, tools_type: str):
        """Wywoływane po wybraniu Arch lub Export."""
        QMessageBox.information(self, "Tools", f"Wybrano: {tools_type}\nTutaj w przyszłości uruchomisz skrypt Tools.")
        self.statusBar().showMessage(f"Wybrano {tools_type}")

    def on_theme_selected(self, theme_type: str):
        """Wywoływane po wybraniu Light lub Dark."""
        QMessageBox.information(self, "Theme", f"Wybrano: {theme_type}\nTutaj w przyszłości uruchomisz skrypt Theme.")
        self.statusBar().showMessage(f"Wybrano {theme_type}")

    def on_about_selected(self, about_type: str):
        """Wywoływane po wybraniu About."""
        QMessageBox.information(self, "About", f"Wybrano: {about_type}\nTutaj w przyszłości uruchomisz skrypt About.")
        self.statusBar().showMessage(f"Wybrano {about_type}")


def launch_application() -> None:
    """Funkcja startowa."""
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())