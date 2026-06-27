import sys

from PySide6.QtWidgets import QApplication

from app.startup import initialize_database
from services.auth_service import AuthService
from services.company_service import CompanyService

from ui.auth.login_window import LoginWindow
from ui.company.company_window import CompanyWindow


def main():
    initialize_database()

    auth = AuthService()
    auth.create_default_admin()

    app = QApplication(sys.argv)

    company_service = CompanyService()

    if company_service.get_company() is None:
        company_window = CompanyWindow()
        company_window.show()
        app.exec()

    login = LoginWindow()
    login.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()