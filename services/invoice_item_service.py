from database.session import SessionLocal
from database.models.invoice_item import InvoiceItem


class InvoiceItemService:

    def __init__(self):
        self.db = SessionLocal()

    def create_item(self, data):
        item = InvoiceItem(**data)

        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)

        return item