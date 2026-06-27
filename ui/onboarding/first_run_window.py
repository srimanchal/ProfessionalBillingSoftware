from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
)

from services.first_run_service import (
    FirstRunService,
)


class FirstRunWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.service = (
            FirstRunService()
        )

        self.setWindowTitle(
            "Create Administrator Account"
        )

        self.resize(
            500,
            350,
        )

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()

        layout.addWidget(
            QLabel(
                "Username"
            )
        )

        self.username = QLineEdit()

        layout.addWidget(
            self.username
        )

        layout.addWidget(
            QLabel(
                "Password"
            )
        )

        self.password = QLineEdit()
        self.password.setEchoMode(
            QLineEdit.Password
        )

        layout.addWidget(
            self.password
        )

        layout.addWidget(
            QLabel(
                "Confirm Password"
            )
        )

        self.confirm_password = (
            QLineEdit()
        )

        self.confirm_password.setEchoMode(
            QLineEdit.Password
        )

        layout.addWidget(
            self.confirm_password
        )

        self.create_button = (
            QPushButton(
                "Create Administrator"
            )
        )

        layout.addWidget(
            self.create_button
        )

        self.setLayout(layout)

        self.create_button.clicked.connect(
            self.create_admin
        )

    def create_admin(self):

        username = (
            self.username.text().strip()
        )

        password = (
            self.password.text()
        )

        confirm = (
            self.confirm_password.text()
        )

        if not username:
            QMessageBox.warning(
                self,
                "Validation",
                "Username is required.",
            )
            return

        if not password:
            QMessageBox.warning(
                self,
                "Validation",
                "Password is required.",
            )
            return

        if password != confirm:
            QMessageBox.warning(
                self,
                "Validation",
                "Passwords do not match.",
            )
            return

        self.service.create_admin(
            username,
            password,
        )

        QMessageBox.information(
            self,
            "Success",
            "Administrator account created successfully.",
        )

        from ui.company.company_window import (
            CompanyWindow,
        )

        self.company_window = (
            CompanyWindow()
        )

        self.company_window.show()

        self.close()