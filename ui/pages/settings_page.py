from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTabWidget,
)

from ui.settings.settings_window import (
    SettingsWindow
)

from ui.settings.backup_window import (
    BackupWindow
)


class SettingsPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        tabs = QTabWidget()

        tabs.addTab(
            SettingsWindow(),
            "General"
        )

        tabs.addTab(
            BackupWindow(),
            "Backup"
        )

        layout.addWidget(
            tabs
        )

        self.setLayout(layout)