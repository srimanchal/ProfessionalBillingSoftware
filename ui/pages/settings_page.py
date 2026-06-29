from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTabWidget,
)

from ui.settings.settings_window import (
    SettingsWindow,
)

from ui.settings.backup_window import (
    BackupWindow,
)


class SettingsPage(QWidget):

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

        self.tabs.addTab(
            SettingsWindow(),
            "General",
        )

        self.tabs.addTab(
            BackupWindow(),
            "Backup",
        )

        layout.addWidget(
            self.tabs
        )

        self.setLayout(
            layout
        )