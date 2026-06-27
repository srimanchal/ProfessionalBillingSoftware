from pathlib import Path
from datetime import datetime
import shutil
import zipfile

from app.constants import (
    DOCUMENTS_DIR,
    DATABASE_FILE,
)


class BackupService:

    def __init__(self):
        self.backup_dir = (
            DOCUMENTS_DIR
            / "backups"
        )

        self.backup_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    # ==========================
    # Database Backup
    # ==========================
    def create_database_backup(
        self,
    ):
        timestamp = (
            datetime.now()
            .strftime(
                "%Y%m%d_%H%M%S"
            )
        )

        backup_file = (
            self.backup_dir
            / f"billing_{timestamp}.db"
        )

        shutil.copy2(
            DATABASE_FILE,
            backup_file,
        )

        return backup_file

    # ==========================
    # ZIP Backup
    # ==========================
    def create_zip_backup(
        self,
    ):
        timestamp = (
            datetime.now()
            .strftime(
                "%Y%m%d_%H%M%S"
            )
        )

        zip_path = (
            self.backup_dir
            / f"backup_{timestamp}.zip"
        )

        with zipfile.ZipFile(
            zip_path,
            "w",
            zipfile.ZIP_DEFLATED,
        ) as zipf:

            zipf.write(
                DATABASE_FILE,
                DATABASE_FILE.name,
            )

        return zip_path

    # ==========================
    # Restore Database
    # ==========================
    def restore_database(
        self,
        backup_file,
    ):
        shutil.copy2(
            backup_file,
            DATABASE_FILE,
        )

        return True

    # ==========================
    # List Backups
    # ==========================
    def get_backups(
        self,
    ):
        return sorted(
            self.backup_dir.glob("*"),
            reverse=True,
        )