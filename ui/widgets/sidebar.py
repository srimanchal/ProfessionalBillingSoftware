from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
)

from PySide6.QtGui import (
    QPixmap,
)

from PySide6.QtCore import (
    Qt,
)

from services.company_service import (
    CompanyService,
)


class Sidebar(QWidget):

    def __init__(self):
        super().__init__()

        self.company_service = (
            CompanyService()
        )

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()

        # =====================
        # Company Logo
        # =====================

        self.logo_label = QLabel()
        self.logo_label.setFixedSize(
            120,
            120,
        )

        self.logo_label.setAlignment(
            Qt.AlignCenter
        )

        # =====================
        # Company Name
        # =====================

        self.company_name_label = QLabel(
            "Professional Billing Software"
        )

        self.company_name_label.setAlignment(
            Qt.AlignCenter
        )

        self.company_name_label.setWordWrap(
            True
        )

        self.company_name_label.setStyleSheet(
            """
            font-size:16px;
            font-weight:bold;
            padding:10px;
            """
        )

        self.load_company()

        # =====================
        # Navigation Buttons
        # =====================

        self.dashboard_btn = QPushButton(
            "Dashboard"
        )

        self.products_btn = QPushButton(
            "Products"
        )

        self.customers_btn = QPushButton(
            "Customers"
        )

        self.invoices_btn = QPushButton(
            "Invoices"
        )

        self.reports_btn = QPushButton(
            "Reports"
        )

        self.settings_btn = QPushButton(
            "Settings"
        )

        # =====================
        # Layout
        # =====================

        layout.addWidget(
            self.logo_label
        )

        layout.addWidget(
            self.company_name_label
        )

        layout.addSpacing(
            20
        )

        layout.addWidget(
            self.dashboard_btn
        )

        layout.addWidget(
            self.products_btn
        )

        layout.addWidget(
            self.customers_btn
        )

        layout.addWidget(
            self.invoices_btn
        )

        layout.addWidget(
            self.reports_btn
        )

        layout.addWidget(
            self.settings_btn
        )

        layout.addStretch()

        self.setLayout(layout)

    def load_company(self):

        company = (
            self.company_service.get_company()
        )

        if not company:
            return

        self.company_name_label.setText(
            company.company_name
        )

        if (
            company.logo_path
            and
            company.logo_path.strip()
        ):
            pixmap = QPixmap(
                company.logo_path
            )

            if not pixmap.isNull():

                pixmap = pixmap.scaled(
                    100,
                    100,
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation,
                )

                self.logo_label.setPixmap(
                    pixmap
                )