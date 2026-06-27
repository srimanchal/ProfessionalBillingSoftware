import sys

from PySide6.QtWidgets import QApplication

from app.startup import initialize_database

from services.settings_service import (
    SettingsService,
)

from services.first_run_service import (
    FirstRunService,
)

from ui.settings.theme_manager import (
    LIGHT_THEME,
    DARK_THEME,
)

from ui.auth.login_window import (
    LoginWindow,
)

from ui.onboarding.first_run_window import (
    FirstRunWindow,
)


def main():
    app = QApplication(sys.argv)

    initialize_database()

    settings = SettingsService()

    theme = settings.get(
        "theme",
        "dark",
    )

    if theme.lower() == "dark":
        app.setStyleSheet(
            DARK_THEME
        )
    else:
        app.setStyleSheet(
            LIGHT_THEME
        )

    first_run_service = (
        FirstRunService()
    )

    if first_run_service.is_first_run():
        window = (
            FirstRunWindow()
        )
    else:
        window = (
            LoginWindow()
        )

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()