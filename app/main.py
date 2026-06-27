import sys

from PySide6.QtWidgets import QApplication

from app.startup import initialize_database
from services.auth_service import AuthService
from ui.auth.login_window import LoginWindow


def main():
    initialize_database()

    auth = AuthService()
    auth.create_default_admin()

    app = QApplication(sys.argv)

    window = LoginWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()