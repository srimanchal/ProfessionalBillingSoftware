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

        layout = QVBoxLayout()

        layout.addWidget(
            CustomerWindow()
        )

        self.setLayout(layout)