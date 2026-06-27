from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTabWidget,
)

from ui.invoices.invoice_window import (
    InvoiceWindow
)

from ui.invoices.invoice_history_window import (
    InvoiceHistoryWindow
)


class InvoicesPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        tabs = QTabWidget()

        tabs.addTab(
            InvoiceWindow(),
            "Create Invoice"
        )

        tabs.addTab(
            InvoiceHistoryWindow(),
            "Invoice History"
        )

        layout.addWidget(tabs)

        self.setLayout(layout)