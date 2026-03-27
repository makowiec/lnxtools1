# -*- coding: utf-8 -*-
"""
Modul: lnxtools/utils/theme.py

Tryby graficzne pracy programu.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Theme:
    name: str

    # Podstawowe
    bg: str
    fg: str
    border: str

    # Przyciski
    button_bg: str
    button_fg: str
    button_hover: str
    button_pressed: str

    # Pola tekstowe / input
    input_bg: str
    input_border: str
    input_focus_border: str

    # Scrollbar
    scrollbar_bg: str
    scrollbar_handle: str
    scrollbar_hover: str

    # Tabela
    table_alternate: str
    table_grid: str
    table_header_bg: str
    table_selection: str
    table_selection_inactive: str

    # Checkbox / indicator
    indicator_border: str
    indicator_checked: str

    accent: str = "#FFA500"


# Style

DARK_STYLESHEET = """
QWidget {{
    background-color: {bg};
    color: {fg};
    font-size: 11pt;
}}

QTextEdit, QPlainTextEdit, LineNumberedPlainTextEdit {{
    background-color: {input_bg};
    color: {fg};
    border: 1px solid {border};
}}

QGroupBox {{
    border: 1px solid {border};
    margin-top: 10px;
}}

QGroupBox::title {{
    subcontrol-origin: margin;
    left: 8px;
    padding: 0 4px;
    color: {fg};
}}

/* Przyciski */
QPushButton {{
    background-color: {button_bg};
    color: {button_fg};
    border: 1px solid #555555;
    padding: 6px;
    border-radius: 4px;
}}

QPushButton:hover {{
    background-color: {button_hover};
}}

QPushButton:pressed {{
    background-color: {button_pressed};
}}

QPushButton:focus {{
    border: 1px solid #589df6;
}}

QPushButton:disabled {{
    background-color: {bg};
    color: #777777;
    border: 1px solid {border};
}}

/* Pola jednolinijkowe */
QLineEdit {{
    background-color: {input_bg};
    color: {fg};
    border: 1px solid {input_border};
    padding: 2px;
}}

QLineEdit:focus {{
    border: 1px solid {input_focus_border};
}}

/* Scrollbar */
QScrollBar:vertical {{
    background: {scrollbar_bg};
    width: 10px;
}}

QScrollBar::handle:vertical {{
    background: {scrollbar_handle};
    border-radius: 5px;
}}

QScrollBar::handle:vertical:hover {{
    background: {scrollbar_hover};
}}

/* Tabela */
QTableWidget {{
    background-color: {input_bg};
    alternate-background-color: {table_alternate};
    gridline-color: {table_grid};
    border: 1px solid {border};
}}

QTableWidget::item {{
    padding: 4px;
}}

QTableWidget::item:selected {{
    background-color: {table_selection};
    color: #000000;
}}

QTableWidget::item:selected:!active {{
    background-color: {table_selection_inactive};
    color: #000000;
}}

QHeaderView::section {{
    background-color: {table_header_bg};
    color: {fg};
    border: 1px solid {border};
    padding: 4px;
}}

/* Checkbox i indicator */
QCheckBox::indicator, QListWidget::indicator {{
    width: 14px;
    height: 14px;
    border: 1px solid {indicator_border};
    background-color: {input_bg};
}}

QCheckBox::indicator:checked, QListWidget::indicator:checked {{
    background-color: {indicator_checked};
    border: 1px solid #6a6d70;
}}

QCheckBox::indicator:hover, QListWidget::indicator:hover {{
    border: 1px solid {fg};
}}

/* Globalna selekcja */
QWidget {{
    selection-background-color: {accent};
    selection-color: #000000;
}}
QMenuBar {{
    font-size: 12pt;
    font-weight: normal;
}}

QMenuBar::item {{
    font-size: 12pt;
    #padding: 6px 10px;
}}

QMenu {{
    font-size: 12pt;
}}

QMenu::item {{
    font-size: 12pt;
    #padding: 8px 12px 8px 8px;
    min-height: 24px;     /* pomaga przy większej czcionce */
}}

QMenu::item:selected {{
    /* styl przy zaznaczeniu */
}}
"""

LIGHT_STYLESHEET = """
QWidget {{
    background-color: {bg};
    color: {fg};
    font-size: 11pt;
}}

QTextEdit, QPlainTextEdit, LineNumberedPlainTextEdit {{
    background-color: {input_bg};
    color: {fg};
    border: 1px solid {border};
}}

QGroupBox {{
    border: 1px solid {border};
    margin-top: 10px;
}}

QGroupBox::title {{
    subcontrol-origin: margin;
    left: 8px;
    padding: 0 6px;
    color: {fg};
    background-color: {bg};
}}

/* Przyciski */
QPushButton {{
    background-color: {button_bg};
    color: {button_fg};
    border: 1px solid #a0a0a0;
    padding: 6px;
    border-radius: 4px;
}}

QPushButton:hover {{
    background-color: #d0d0d0;
}}

QPushButton:pressed {{
    background-color: #c0c0c0;
}}

QPushButton:focus {{
    border: 1px solid #589df6;
}}

QPushButton:disabled {{
    background-color: {bg};
    color: #888888;
    border: 1px solid {border};
}}

/* Pola jednolinijkowe */
QLineEdit {{
    background-color: {input_bg};
    color: {fg};
    border: 1px solid {input_border};
    padding: 2px;
}}

QLineEdit:focus {{
    border: 1px solid {input_focus_border};
}}

/* Tabela */
QTableWidget {{
    background-color: {input_bg};
    alternate-background-color: #f0f0f0;
    gridline-color: {border};
    border: 1px solid {border};
}}

QTableWidget::item:selected {{
    background-color: {table_selection};
    color: #000000;
}}

QTableWidget::item:selected:!active {{
    background-color: {table_selection_inactive};
    color: #000000;
}}

QHeaderView::section {{
    background-color: #e0e0e0;
    color: {fg};
    border: 1px solid {border};
}}

/* Checkbox */
QCheckBox::indicator {{
    width: 14px;
    height: 14px;
    border: 1px solid {indicator_border};
    background-color: {input_bg};
}}

QCheckBox::indicator:checked {{
    background-color: {indicator_checked};
    border: 1px solid #a0a0a0;
}}

/* Globalna selekcja */
QWidget {{
    selection-background-color: {accent};
    selection-color: #000000;
}}
QMenuBar {{
    font-size: 12pt;
    font-weight: normal;
}}

QMenuBar::item {{
    font-size: 12pt;
    #padding: 6px 10px;
}}

QMenu {{
    font-size: 12pt;
}}

QMenu::item {{
    font-size: 12pt;
    #padding: 8px 12px 8px 8px;
    #min-height: 24px;     /* pomaga przy większej czcionce */
}}

QMenu::item:selected {{
    /* styl przy zaznaczeniu */
}}
"""

THEMES = {
    "dark": Theme(
        name="dark",
        bg="#2b2b2b", fg="#dcdcdc", border="#3c3f41",
        button_bg="#3c3f41", button_fg="#ffffff",
        button_hover="#4e5254", button_pressed="#2d2f31",
        input_bg="#1e1e1e", input_border="#3c3f41", input_focus_border="#589df6",
        scrollbar_bg="#2b2b2b", scrollbar_handle="#3c3f41", scrollbar_hover="#4e5254",
        table_alternate="#252526", table_grid="#3c3f41", table_header_bg="#3c3f41",
        table_selection="#FFA500", table_selection_inactive="#ffb84d",
        indicator_border="#5a5d60", indicator_checked="#FFA500",
    ),
    "light": Theme(
        name="light",
        bg="#f5f5f5", fg="#000000", border="#c0c0c0",
        button_bg="#e0e0e0", button_fg="#000000",
        button_hover="#d0d0d0", button_pressed="#c0c0c0",
        input_bg="#ffffff", input_border="#c0c0c0", input_focus_border="#589df6",
        scrollbar_bg="#f0f0f0", scrollbar_handle="#c0c0c0", scrollbar_hover="#a0a0a0",
        table_alternate="#f0f0f0", table_grid="#c0c0c0", table_header_bg="#e0e0e0",
        table_selection="#FFA500", table_selection_inactive="#ffb84d",
        indicator_border="#a0a0a0", indicator_checked="#FFA500",
    ),
}


def get_stylesheet(theme_name: str = "dark") -> str:
    """Zwraca gotowy stylesheet z wstawionymi kolorami"""
    theme = THEMES.get(theme_name, THEMES["dark"])
    template = DARK_STYLESHEET if theme_name == "dark" else LIGHT_STYLESHEET
    return template.format(**theme.__dict__).strip()