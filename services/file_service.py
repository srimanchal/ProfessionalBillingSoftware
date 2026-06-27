import shutil
from pathlib import Path

from app.constants import (
    LOGOS_DIR,
    SIGNATURES_DIR,
)


class FileService:

    @staticmethod
    def save_logo(
        source_file
    ):
        if not source_file:
            return None

        source = Path(
            source_file
        )

        destination = (
            LOGOS_DIR /
            source.name
        )

        shutil.copy2(
            source,
            destination,
        )

        return str(
            destination
        )

    @staticmethod
    def save_signature(
        source_file
    ):
        if not source_file:
            return None

        source = Path(
            source_file
        )

        destination = (
            SIGNATURES_DIR /
            source.name
        )

        shutil.copy2(
            source,
            destination,
        )

        return str(
            destination
        )