import sys
import traceback

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer

from app.startup import (
    initialize_database,
)

from app.logger import logger

from services.first_run_service import (
    FirstRunService,
)

from services.company_service import (
    CompanyService,
)

from services.settings_service import (
    SettingsService,
)

from ui.settings.theme_manager import (
    ThemeManager,
)

from ui.onboarding.first_run_window import (
    FirstRunWindow,
)

from ui.company.company_window import (
    CompanyWindow,
)

from ui.auth.login_window import (
    LoginWindow,
)

from ui.splash_screen import (
    SplashScreen,
)


def start_application():
    logger.info(
        "Starting Professional Billing Software..."
    )

    splash = SplashScreen()
    splash.start()
    QApplication.processEvents()

    splash.set_progress(
        20,
        "Initializing database..."
    )
    QApplication.processEvents()

    initialize_database()

    splash.set_progress(
        40,
        "Loading settings..."
    )
    QApplication.processEvents()

    SettingsService()

    splash.set_progress(
        60,
        "Checking application setup..."
    )
    QApplication.processEvents()

    first_run_service = (
        FirstRunService()
    )

    if first_run_service.is_first_run():
        splash.finish()

        window = FirstRunWindow()
        window.show()
        return

    splash.set_progress(
        80,
        "Loading company information..."
    )
    QApplication.processEvents()

    company_service = (
        CompanyService()
    )

    if (
        company_service.get_company()
        is None
    ):
        splash.finish()

        window = CompanyWindow()
        window.show()
        return

    splash.set_progress(
        100,
        "Starting application..."
    )
    QApplication.processEvents()

    splash.finish()

    login = LoginWindow()
    login.show()

    app = QApplication.instance()
    app.login_window = login


def main():
    try:
        app = QApplication(sys.argv)

        app.setApplicationName(
            "Professional Billing Software"
        )

        app.setOrganizationName(
            "Professional Billing Software"
        )

        ThemeManager.apply(app)

        QTimer.singleShot(
            100,
            start_application
        )

        sys.exit(
            app.exec()
        )

    except Exception:
        print(
            "\n========== ERROR ==========\n"
        )

        traceback.print_exc()

        print(
            "\n===========================\n"
        )

        input(
            "Press Enter to exit..."
        )

        raise


if __name__ == "__main__":
    main()