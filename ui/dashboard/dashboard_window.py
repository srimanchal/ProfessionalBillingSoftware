from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QFrame,
    QStackedWidget,
)
from PySide6.QtCore import Qt

from ui.dashboard.dashboard_viewmodel import DashboardViewModel

from ui.pages.dashboard_page import DashboardPage
from ui.pages.products_page import ProductsPage
from ui.pages.customers_page import CustomersPage
from ui.pages.invoices_page import InvoicesPage
from ui.pages.reports_page import ReportsPage
from ui.pages.settings_page import SettingsPage


class DashboardWindow(QMainWindow):

    def __init__(self, user):
        super().__init__()

        self.user = user
        self.viewmodel = DashboardViewModel()

        self.setup_ui()

    def setup_ui(self):
        company = self.viewmodel.get_company()

        self.setWindowTitle("Professional Billing Software")
        self.resize(1400, 800)

        # Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        #################################################
        # Sidebar
        #################################################

        sidebar = QFrame()
        sidebar.setFixedWidth(250)

        sidebar_layout = QVBoxLayout()

        company_name = QLabel(
            company.company_name
            if company
            else "Professional Billing Software"
        )

        company_name.setAlignment(Qt.AlignCenter)
        company_name.setWordWrap(True)

        user_label = QLabel(
            f"Logged in as\n{self.user.full_name}"
        )

        user_label.setAlignment(Qt.AlignCenter)

        dashboard_btn = QPushButton("Dashboard")
        products_btn = QPushButton("Products")
        customers_btn = QPushButton("Customers")
        invoices_btn = QPushButton("Invoices")
        reports_btn = QPushButton("Reports")
        settings_btn = QPushButton("Settings")

        sidebar_layout.addWidget(company_name)
        sidebar_layout.addWidget(user_label)
        sidebar_layout.addSpacing(30)

        sidebar_layout.addWidget(dashboard_btn)
        sidebar_layout.addWidget(products_btn)
        sidebar_layout.addWidget(customers_btn)
        sidebar_layout.addWidget(invoices_btn)
        sidebar_layout.addWidget(reports_btn)
        sidebar_layout.addWidget(settings_btn)

        sidebar_layout.addStretch()

        sidebar.setLayout(sidebar_layout)

        #################################################
        # Pages
        #################################################

        self.stack = QStackedWidget()

        self.dashboard_page = DashboardPage()
        self.products_page = ProductsPage()
        self.customers_page = CustomersPage()
        self.invoices_page = InvoicesPage()
        self.reports_page = ReportsPage()
        self.settings_page = SettingsPage()

        self.stack.addWidget(self.dashboard_page)
        self.stack.addWidget(self.products_page)
        self.stack.addWidget(self.customers_page)
        self.stack.addWidget(self.invoices_page)
        self.stack.addWidget(self.reports_page)
        self.stack.addWidget(self.settings_page)

        #################################################
        # Button Events
        #################################################

        dashboard_btn.clicked.connect(
            lambda: self.stack.setCurrentIndex(0)
        )

        products_btn.clicked.connect(
            lambda: self.stack.setCurrentIndex(1)
        )

        customers_btn.clicked.connect(
            lambda: self.stack.setCurrentIndex(2)
        )

        invoices_btn.clicked.connect(
            lambda: self.stack.setCurrentIndex(3)
        )

        reports_btn.clicked.connect(
            lambda: self.stack.setCurrentIndex(4)
        )

        settings_btn.clicked.connect(
            lambda: self.stack.setCurrentIndex(5)
        )

        #################################################
        # Add Widgets To Main Layout
        #################################################

        main_layout.addWidget(sidebar)
        main_layout.addWidget(self.stack)

        # Default Page
        self.stack.setCurrentIndex(0)