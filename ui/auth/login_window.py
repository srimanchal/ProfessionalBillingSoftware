from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QMessageBox,
    QSizePolicy,
)

from PySide6.QtCore import Qt

from ui.auth.login_viewmodel import (
    LoginViewModel
)

from ui.dashboard.dashboard_window import (
    DashboardWindow
)


class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.viewmodel = LoginViewModel()

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(
            "Professional Billing Software"
        )

        self.resize(
            1200,
            700,
        )

        self.setMinimumSize(
            1100,
            650,
        )

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )
        main_layout.setSpacing(0)

        #################################################
        # Left Hero Section
        #################################################

        hero = QFrame()
        hero.setObjectName(
            "LoginHero"
        )

        hero_layout = QVBoxLayout()
        hero_layout.setContentsMargins(
            70,
            70,
            70,
            70,
        )

        hero_layout.addStretch()

        app_name = QLabel(
            "Professional Billing Software"
        )
        app_name.setObjectName(
            "LoginTitle"
        )
        app_name.setWordWrap(True)
        app_name.setAlignment(
            Qt.AlignLeft
        )

        tagline = QLabel(
            "Smart Invoicing for Modern Businesses"
        )
        tagline.setObjectName(
            "LoginTagline"
        )
        tagline.setAlignment(
            Qt.AlignLeft
        )

        features = QLabel(
            "✔ GST Billing\n"
            "✔ Inventory Management\n"
            "✔ Customer Management\n"
            "✔ Reports & Analytics\n"
            "✔ Professional PDF Invoices\n"
            "✔ Real-Time Dashboard"
        )

        features.setObjectName(
            "LoginFeatures"
        )
        features.setAlignment(
            Qt.AlignLeft
        )

        hero_layout.addWidget(
            app_name,
            alignment=Qt.AlignLeft
        )

        hero_layout.addSpacing(
            20
        )

        hero_layout.addWidget(
            tagline,
            alignment=Qt.AlignLeft
        )

        hero_layout.addSpacing(
            60
        )

        hero_layout.addWidget(
            features,
            alignment=Qt.AlignLeft
        )

        hero_layout.addStretch()

        hero.setLayout(
            hero_layout
        )

        #################################################
        # Right Side
        #################################################

        right = QFrame()
        right.setObjectName(
            "LoginBackground"
        )

        right_layout = QVBoxLayout()
        right_layout.setAlignment(
            Qt.AlignCenter
        )

        card = QFrame()
        card.setObjectName(
            "LoginCard"
        )
        card.setFixedWidth(
            430
        )

        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(
            45,
            45,
            45,
            45,
        )
        card_layout.setSpacing(
            18
        )

        title = QLabel(
            "Welcome Back"
        )
        title.setObjectName(
            "LoginCardTitle"
        )
        title.setAlignment(
            Qt.AlignCenter
        )

        subtitle = QLabel(
            "Sign in to continue"
        )
        subtitle.setObjectName(
            "LoginSubtitle"
        )
        subtitle.setAlignment(
            Qt.AlignCenter
        )

        self.username = QLineEdit()
        self.username.setPlaceholderText(
            "Username"
        )
        self.username.setMinimumHeight(
            45
        )

        self.password = QLineEdit()
        self.password.setPlaceholderText(
            "Password"
        )
        self.password.setEchoMode(
            QLineEdit.Password
        )
        self.password.setMinimumHeight(
            45
        )

        self.login_button = QPushButton(
            "Login"
        )
        self.login_button.setMinimumHeight(
            48
        )

        version = QLabel(
            "Version 1.0"
        )
        version.setObjectName(
            "LoginVersion"
        )
        version.setAlignment(
            Qt.AlignCenter
        )

        card_layout.addWidget(
            title
        )

        card_layout.addWidget(
            subtitle
        )

        card_layout.addSpacing(
            15
        )

        card_layout.addWidget(
            self.username
        )

        card_layout.addWidget(
            self.password
        )

        card_layout.addSpacing(
            10
        )

        card_layout.addWidget(
            self.login_button
        )

        card_layout.addSpacing(
            15
        )

        card_layout.addWidget(
            version
        )

        card.setLayout(
            card_layout
        )

        right_layout.addWidget(
            card
        )

        right.setLayout(
            right_layout
        )

        #################################################
        # Main Layout
        #################################################

        main_layout.addWidget(
            hero,
            3
        )

        main_layout.addWidget(
            right,
            2
        )

        self.setLayout(
            main_layout
        )

        #################################################
        # Events
        #################################################

        self.login_button.clicked.connect(
            self.login
        )

        self.password.returnPressed.connect(
            self.login
        )

    #################################################
    # Login
    #################################################

    def login(self):
        username = (
            self.username.text()
            .strip()
        )

        password = (
            self.password.text()
        )

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

        self.dashboard = (
            DashboardWindow(
                user
            )
        )

        self.dashboard.show()

        self.close()