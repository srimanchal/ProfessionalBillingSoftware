from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTabWidget,
)

from ui.invoices.invoice_window import (
    InvoiceWindow,
)

from ui.invoices.invoice_history_window import (
    InvoiceHistoryWindow,
)


class InvoicesPage(QWidget):

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()

        layout.setContentsMargins(
            20,
            20,
            20,
            20,
        )

        self.tabs = QTabWidget()

        self.tabs.setDocumentMode(
            True
        )

        self.tabs.setMovable(
            False
        )

        self.tabs.addTab(
            InvoiceWindow(),
            "Create Invoice",
        )

        self.tabs.addTab(
            InvoiceHistoryWindow(),
            "Invoice History",
        )

        layout.addWidget(
            self.tabs
        )

        self.setLayout(
            layout
        )