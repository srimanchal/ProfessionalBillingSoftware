from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QComboBox,
    QPushButton,
    QMessageBox,
)

from services.settings_service import (
    SettingsService
)


class SettingsWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.service = (
            SettingsService()
        )

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(
            QLabel(
                "Application Theme"
            )
        )

        self.theme = QComboBox()

        self.theme.addItems(
            [
                "light",
                "dark",
            ]
        )

        self.theme.setCurrentText(
            self.service.get(
                "theme",
                "light",
            )
        )

        layout.addWidget(
            self.theme
        )

        self.save_btn = QPushButton(
            "Save"
        )

        layout.addWidget(
            self.save_btn
        )

        self.setLayout(layout)

        self.save_btn.clicked.connect(
            self.save_settings
        )

    def save_settings(self):
        self.service.set(
            "theme",
            self.theme.currentText(),
        )

        QMessageBox.information(
            self,
            "Success",
            "Restart application to apply theme."
        )