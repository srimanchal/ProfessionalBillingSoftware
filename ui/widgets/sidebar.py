from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout
)


class Sidebar(QWidget):

    def __init__(self):
        super().__init__()

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

        layout = QVBoxLayout()

        layout.addWidget(self.dashboard_btn)
        layout.addWidget(self.products_btn)
        layout.addWidget(self.customers_btn)
        layout.addWidget(self.invoices_btn)
        layout.addWidget(self.reports_btn)
        layout.addWidget(self.settings_btn)

        layout.addStretch()

        self.setLayout(layout)