import json

from app.constants import DOCUMENTS_DIR


class SettingsService:

    def __init__(self):
        self.settings_file = (
            DOCUMENTS_DIR
            / "settings.json"
        )

        self.load()

    def load(self):

        if not self.settings_file.exists():

            self.settings = {
                "theme": "light",
                "auto_backup": True,
                "backup_days": 7,
                "company_logo": "",
            }

            self.save()

        else:
            with open(
                self.settings_file,
                "r",
                encoding="utf-8",
            ) as f:
                self.settings = json.load(f)

    def save(self):
        with open(
            self.settings_file,
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(
                self.settings,
                f,
                indent=4,
            )

    def get(
        self,
        key,
        default=None,
    ):
        return self.settings.get(
            key,
            default,
        )

    def set(
        self,
        key,
        value,
    ):
        self.settings[key] = value
        self.save()