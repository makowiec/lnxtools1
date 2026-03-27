"""
ThemeManager - centralna klasa odpowiedzialna za zarzadzanie motywami (Light/Dark)
w aplikacji lnxtools.

Uzywa wzorca Singleton, dzieki czemu motyw jest spojny w calej aplikacji.
"""

from PySide6.QtWidgets import QWidget, QApplication

from src.lnxtools.utils.theme import get_stylesheet
from src.lnxtools.utils.config import load_settings, save_settings


class ThemeManager:
    """
    Singleton zarzadzajacy motywem aplikacji.

    Zapewnia:
    - Wczytanie zapisanego motywu z settings.json
    - Zmiane motywu (Light / Dark)
    - Automatyczne zastosowanie stylesheetu na cale okno aplikacji
    - Mozliwosc przelaczania motywu bez restartu programu
    """

    _instance = None

    def __new__(cls):
        """Implementacja wzorca Singleton."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """
        Inicjalizacja ThemeManagera (wykonuje sie tylko raz).
        Wczytuje zapisany motyw z pliku konfiguracyjnego i aplikuje go.
        """
        if self._initialized:
            return

        self._initialized = True

        # Wczytujemy ustawienia uzytkownika i ustawiamy aktualny motyw
        settings = load_settings()
        self.current_theme_name = settings.get("theme", "dark")

        # Natychmiast stosujemy motyw do calej aplikacji
        self.apply_global_stylesheet()

    def get_current_theme_name(self) -> str:
        """Zwraca nazwe aktualnie aktywnego motywu ('light' lub 'dark')."""
        return self.current_theme_name

    def set_theme(self, theme_name: str) -> None:
        """
        Zmienia motyw aplikacji na podany.

        Args:
            theme_name (str): 'light' lub 'dark'
        """
        if theme_name not in ("light", "dark"):
            return

        self.current_theme_name = theme_name

        # Zapisujemy wybor uzytkownika do pliku konfiguracyjnego
        settings = load_settings()
        settings["theme"] = theme_name
        save_settings(settings)

        # Natychmiast odswiezamy wyglad calej aplikacji
        self.apply_global_stylesheet()

    def toggle_theme(self) -> None:
        """Przelacza motyw na przeciwny (Dark ↔ Light)."""
        new_theme = "light" if self.current_theme_name == "dark" else "dark"
        self.set_theme(new_theme)

    def apply_global_stylesheet(self) -> None:
        """
        Naklada stylesheet na cale QApplication.
        Jest to najwygodniejszy sposob na spojny wyglad calej aplikacji.
        """
        stylesheet = get_stylesheet(self.current_theme_name)

        app = QApplication.instance()
        if isinstance(app, QApplication):  # <- bezpieczne sprawdzenie typu
            app.setStyleSheet(stylesheet)

    def apply_to_widget(self, widget: QWidget) -> None:
        """
        Opcjonalna metoda - pozwala nalozyc stylesheet tylko na konkretny widget.
        Przydatna, gdy nie chcesz uzywac globalnego stylesheetu lub masz okna dialogowe.

        Args:
            widget (QWidget): Widget, ktory ma zostac wystylizowany
        """
        stylesheet = get_stylesheet(self.current_theme_name)
        widget.setStyleSheet(stylesheet)