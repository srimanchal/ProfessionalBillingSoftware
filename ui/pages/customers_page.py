from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
)

from ui.customers.customer_window import (
    CustomerWindow
)


class CustomersPage(QWidget):

    def __init__(self):
        super().__init__()

        self.customer_window = CustomerWindow()

        layout = QVBoxLayout()
        layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        layout.addWidget(
            self.customer_window
        )

        self.setLayout(layout)