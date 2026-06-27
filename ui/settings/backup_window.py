from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QListWidget,
    QFileDialog,
    QMessageBox,
)

from services.backup_service import (
    BackupService
)


class BackupWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.service = (
            BackupService()
        )

        self.setup_ui()

        self.load_backups()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.backup_btn = QPushButton(
            "Create Database Backup"
        )

        self.zip_btn = QPushButton(
            "Create ZIP Backup"
        )

        self.restore_btn = QPushButton(
            "Restore Backup"
        )

        self.list_widget = (
            QListWidget()
        )

        layout.addWidget(
            self.backup_btn
        )

        layout.addWidget(
            self.zip_btn
        )

        layout.addWidget(
            self.restore_btn
        )

        layout.addWidget(
            self.list_widget
        )

        self.setLayout(layout)

        self.backup_btn.clicked.connect(
            self.create_backup
        )

        self.zip_btn.clicked.connect(
            self.create_zip
        )

        self.restore_btn.clicked.connect(
            self.restore_backup
        )

    def load_backups(self):
        self.list_widget.clear()

        backups = (
            self.service.get_backups()
        )

        for backup in backups:
            self.list_widget.addItem(
                str(backup.name)
            )

    def create_backup(self):
        file = (
            self.service
            .create_database_backup()
        )

        QMessageBox.information(
            self,
            "Backup",
            f"Backup created:\n{file}"
        )

        self.load_backups()

    def create_zip(self):
        file = (
            self.service
            .create_zip_backup()
        )

        QMessageBox.information(
            self,
            "Backup",
            f"ZIP created:\n{file}"
        )

        self.load_backups()

    def restore_backup(self):
        file_name, _ = (
            QFileDialog.getOpenFileName(
                self,
                "Select Backup",
                "",
                "Database (*.db)"
            )
        )

        if not file_name:
            return

        self.service.restore_database(
            file_name
        )

        QMessageBox.information(
            self,
            "Restore",
            "Database restored.\nRestart application."
        )