from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QFrame
)
from PySide6.QtCore import Qt

from ui.dashboard.dashboard_viewmodel import (
    DashboardViewModel
)


class DashboardWindow(QMainWindow):

    def __init__(self, user):
        super().__init__()

        self.user = user
        self.viewmodel = DashboardViewModel()

        self.setup_ui()

    def setup_ui(self):
        company = self.viewmodel.get_company()

        self.setWindowTitle(
            "Professional Billing Software"
        )

        self.resize(1400, 800)

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout()
        central.setLayout(main_layout)

        # Sidebar
        sidebar = QFrame()
        sidebar.setFixedWidth(250)

        sidebar_layout = QVBoxLayout()

        title = QLabel(
            company.company_name
            if company
            else "Professional Billing Software"
        )

        title.setWordWrap(True)

        dashboard_btn = QPushButton("Dashboard")
        products_btn = QPushButton("Products")
        customers_btn = QPushButton("Customers")
        invoices_btn = QPushButton("Invoices")
        reports_btn = QPushButton("Reports")
        settings_btn = QPushButton("Settings")

        sidebar_layout.addWidget(title)
        sidebar_layout.addSpacing(30)

        sidebar_layout.addWidget(dashboard_btn)
        sidebar_layout.addWidget(products_btn)
        sidebar_layout.addWidget(customers_btn)
        sidebar_layout.addWidget(invoices_btn)
        sidebar_layout.addWidget(reports_btn)
        sidebar_layout.addWidget(settings_btn)

        sidebar_layout.addStretch()

        sidebar.setLayout(sidebar_layout)

        # Content
        content = QWidget()
        content_layout = QVBoxLayout()
        content.setLayout(content_layout)

        welcome = QLabel(
            f"Welcome {self.user.full_name}"
        )

        welcome.setAlignment(
            Qt.AlignCenter
        )

        content_layout.addStretch()
        content_layout.addWidget(welcome)
        content_layout.addStretch()

        main_layout.addWidget(sidebar)
        main_layout.addWidget(content)