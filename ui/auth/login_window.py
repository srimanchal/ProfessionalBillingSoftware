from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
    QApplication
)
from PySide6.QtCore import Qt

from ui.auth.login_viewmodel import LoginViewModel

from ui.dashboard.dashboard_window import DashboardWindow


class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.viewmodel = LoginViewModel()

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(
            "Professional Billing Software - Login"
        )

        self.resize(450, 300)

        layout = QVBoxLayout()

        title = QLabel(
            "Professional Billing Software"
        )
        title.setAlignment(Qt.AlignCenter)

        self.username = QLineEdit()
        self.username.setPlaceholderText(
            "Username"
        )

        self.password = QLineEdit()
        self.password.setPlaceholderText(
            "Password"
        )
        self.password.setEchoMode(
            QLineEdit.Password
        )

        login_button = QPushButton("Login")
        login_button.clicked.connect(
            self.login
        )

        layout.addStretch()
        layout.addWidget(title)
        layout.addSpacing(20)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addSpacing(10)
        layout.addWidget(login_button)
        layout.addStretch()

        self.setLayout(layout)

    def login(self):
        username = self.username.text().strip()
        password = self.password.text()

        user = self.viewmodel.login(
            username,
            password
        )

        if not user:
            QMessageBox.warning(
                self,
                "Login Failed",
                "Invalid username or password."
            )
            return

        self.dashboard = DashboardWindow(user)
        self.dashboard.show()

        self.close()

        self.close()