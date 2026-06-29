import json
from datetime import datetime

from app.constants import DOCUMENTS_DIR


class SettingsService:

    def __init__(self):
        self.settings_file = (
            DOCUMENTS_DIR
            / "settings.json"
        )

        self.load()

    def get_financial_year(self):
        today = datetime.now()

        year = today.year

        if today.month < 4:
            start_year = year - 1
            end_year = year
        else:
            start_year = year
            end_year = year + 1

        return (
            f"{start_year}-{str(end_year)[-2:]}"
        )

    def load(self):

        if not self.settings_file.exists():

            self.settings = {
                "theme": "dark",
                "auto_backup": True,
                "backup_days": 7,
                "company_logo": "",
                "invoice_prefix": "INV",
                "invoice_counter": 1,
                "financial_year":
                    self.get_financial_year(),
                "currency": "INR",
                "decimal_places": 2,
            }

            self.save()

        else:
            with open(
                self.settings_file,
                "r",
                encoding="utf-8",
            ) as f:
                self.settings = json.load(f)

            defaults = {
                "theme": "dark",
                "auto_backup": True,
                "backup_days": 7,
                "company_logo": "",
                "invoice_prefix": "INV",
                "invoice_counter": 1,
                "financial_year":
                    self.get_financial_year(),
                "currency": "INR",
                "decimal_places": 2,
            }

            changed = False

            for key, value in defaults.items():
                if key not in self.settings:
                    self.settings[key] = value
                    changed = True

            if changed:
                self.save()

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

    def get_next_invoice_number(self):

        prefix = self.get(
            "invoice_prefix",
            "INV",
        )

        financial_year = self.get(
            "financial_year",
            self.get_financial_year(),
        )

        counter = self.get(
            "invoice_counter",
            1,
        )

        invoice_number = (
            f"{prefix}/"
            f"{financial_year}/"
            f"{counter:06d}"
        )

        return invoice_number

    def increment_invoice_counter(self):

        counter = self.get(
            "invoice_counter",
            1,
        )

        counter += 1

        self.set(
            "invoice_counter",
            counter,
        )