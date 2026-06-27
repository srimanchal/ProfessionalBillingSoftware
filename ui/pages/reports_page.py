from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout
)

from ui.reports.report_window import (
    ReportWindow
)


class ReportsPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(
            ReportWindow()
        )

        self.setLayout(layout)