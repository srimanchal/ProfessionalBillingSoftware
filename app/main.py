import sys

from PySide6.QtWidgets import QApplication

from app.startup import initialize_database

from services.settings_service import (
    SettingsService,
)

from ui.settings.theme_manager import (
    LIGHT_THEME,
    DARK_THEME,
)

from ui.auth.login_window import (
    LoginWindow,
)


def main():
    app = QApplication(sys.argv)

    # Initialize database
    initialize_database()

    # Load application settings
    settings = SettingsService()

    theme = settings.get(
        "theme",
        "light",
    )

    if theme == "dark":
        app.setStyleSheet(
            DARK_THEME
        )
    else:
        app.setStyleSheet(
            LIGHT_THEME
        )

    # Start application
    window = LoginWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()