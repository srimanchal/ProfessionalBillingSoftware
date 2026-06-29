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

from ui.dashboard.dashboard_viewmodel import (
    DashboardViewModel
)

from ui.pages.dashboard_page import (
    DashboardPage
)

from ui.pages.products_page import (
    ProductsPage
)

from ui.pages.customers_page import (
    CustomersPage
)

from ui.pages.invoices_page import (
    InvoicesPage
)

from ui.pages.reports_page import (
    ReportsPage
)

from ui.pages.settings_page import (
    SettingsPage
)


class DashboardWindow(QMainWindow):

    def __init__(self, user):
        super().__init__()

        self.user = user
        self.viewmodel = DashboardViewModel()

        self.setup_ui()

    #################################################
    # UI
    #################################################

    def setup_ui(self):
        company = self.viewmodel.get_company()

        self.setWindowTitle(
            "Professional Billing Software"
        )

        self.resize(
            1500,
            900,
        )

        #################################################
        # Central Widget
        #################################################

        central_widget = QWidget()
        self.setCentralWidget(
            central_widget
        )

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )
        main_layout.setSpacing(0)

        central_widget.setLayout(
            main_layout
        )

        #################################################
        # Sidebar
        #################################################

        sidebar = QFrame()
        sidebar.setObjectName(
            "Sidebar"
        )

        sidebar.setFixedWidth(
            270
        )

        sidebar_layout = QVBoxLayout()
        sidebar_layout.setContentsMargins(
            25,
            25,
            25,
            25,
        )

        sidebar_layout.setSpacing(
            12
        )

        #################################################
        # Company Section
        #################################################

        company_name = QLabel(
            company.company_name
            if company
            else "Professional Billing Software"
        )

        company_name.setObjectName(
            "CompanyLabel"
        )

        company_name.setAlignment(
            Qt.AlignCenter
        )

        company_name.setWordWrap(
            True
        )

        user_label = QLabel(
            f"Logged in as\n{self.user.full_name}"
        )

        user_label.setObjectName(
            "UserLabel"
        )

        user_label.setAlignment(
            Qt.AlignCenter
        )

        sidebar_layout.addWidget(
            company_name
        )

        sidebar_layout.addWidget(
            user_label
        )

        sidebar_layout.addSpacing(
            30
        )

        #################################################
        # Navigation Buttons
        #################################################

        self.dashboard_btn = QPushButton(
            "🏠   Dashboard"
        )

        self.products_btn = QPushButton(
            "📦   Products"
        )

        self.customers_btn = QPushButton(
            "👥   Customers"
        )

        self.invoices_btn = QPushButton(
            "🧾   Invoices"
        )

        self.reports_btn = QPushButton(
            "📈   Reports"
        )

        self.settings_btn = QPushButton(
            "⚙️   Settings"
        )

        self.menu_buttons = [
            self.dashboard_btn,
            self.products_btn,
            self.customers_btn,
            self.invoices_btn,
            self.reports_btn,
            self.settings_btn,
        ]

        for button in self.menu_buttons:
            button.setMinimumHeight(
                45
            )
            button.setCursor(
                Qt.PointingHandCursor
            )
            sidebar_layout.addWidget(
                button
            )

        sidebar_layout.addStretch()

        #################################################
        # Footer
        #################################################

        version = QLabel(
            "Professional Billing Software\nVersion 1.0"
        )

        version.setAlignment(
            Qt.AlignCenter
        )

        version.setObjectName(
            "UserLabel"
        )

        sidebar_layout.addWidget(
            version
        )

        sidebar.setLayout(
            sidebar_layout
        )

        #################################################
        # Pages
        #################################################

        self.stack = QStackedWidget()

        self.dashboard_page = (
            DashboardPage()
        )

        self.products_page = (
            ProductsPage()
        )

        self.customers_page = (
            CustomersPage()
        )

        self.invoices_page = (
            InvoicesPage()
        )

        self.reports_page = (
            ReportsPage()
        )

        self.settings_page = (
            SettingsPage()
        )

        self.stack.addWidget(
            self.dashboard_page
        )

        self.stack.addWidget(
            self.products_page
        )

        self.stack.addWidget(
            self.customers_page
        )

        self.stack.addWidget(
            self.invoices_page
        )

        self.stack.addWidget(
            self.reports_page
        )

        self.stack.addWidget(
            self.settings_page
        )

        #################################################
        # Events
        #################################################

        self.dashboard_btn.clicked.connect(
            lambda: self.switch_page(
                0
            )
        )

        self.products_btn.clicked.connect(
            lambda: self.switch_page(
                1
            )
        )

        self.customers_btn.clicked.connect(
            lambda: self.switch_page(
                2
            )
        )

        self.invoices_btn.clicked.connect(
            lambda: self.switch_page(
                3
            )
        )

        self.reports_btn.clicked.connect(
            lambda: self.switch_page(
                4
            )
        )

        self.settings_btn.clicked.connect(
            lambda: self.switch_page(
                5
            )
        )

        #################################################
        # Main Layout
        #################################################

        main_layout.addWidget(
            sidebar
        )

        main_layout.addWidget(
            self.stack
        )

        self.switch_page(0)

    #################################################
    # Switch Page
    #################################################

    def switch_page(
        self,
        index,
    ):
        self.stack.setCurrentIndex(
            index
        )

        for button in self.menu_buttons:
            button.setProperty(
                "active",
                False,
            )
            button.style().unpolish(
                button
            )
            button.style().polish(
                button
            )

        active_button = (
            self.menu_buttons[index]
        )

        active_button.setProperty(
            "active",
            True,
        )

        active_button.style().unpolish(
            active_button
        )

        active_button.style().polish(
            active_button
        )