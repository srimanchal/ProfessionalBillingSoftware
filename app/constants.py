from pathlib import Path
import os

APP_NAME = "Professional Billing Software"

DOCUMENTS_DIR = Path.home() / "Documents" / APP_NAME
DATA_DIR = DOCUMENTS_DIR / "data"
INVOICES_DIR = DOCUMENTS_DIR / "invoices"
REPORTS_DIR = DOCUMENTS_DIR / "reports"
BACKUPS_DIR = DOCUMENTS_DIR / "backups"
LOGS_DIR = DOCUMENTS_DIR / "logs"
EXPORTS_DIR = DOCUMENTS_DIR / "exports"

DATABASE_FILE = DATA_DIR / "billing.db"

for folder in [
    DOCUMENTS_DIR,
    DATA_DIR,
    INVOICES_DIR,
    REPORTS_DIR,
    BACKUPS_DIR,
    LOGS_DIR,
    EXPORTS_DIR,
]:
    folder.mkdir(parents=True, exist_ok=True)