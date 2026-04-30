# -*- coding: utf-8 -*-
"""
Modul: lnxtools/gui/qt_logger.py

Przekazuje dane loggera do GUI
"""

from PySide6.QtCore import QObject, Signal

class QtLogger(QObject):
    log_signal = Signal(str, str)  # message, level

qt_logger = QtLogger()