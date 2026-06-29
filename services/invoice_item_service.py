from database.session import SessionLocal
from database.models.invoice_item import (
    InvoiceItem
)


class InvoiceItemService:

    def create_item(
        self,
        data,
    ):
        db = SessionLocal()

        try:
            item = InvoiceItem(
                **data
            )

            db.add(item)
            db.commit()
            db.refresh(item)

            return item

        finally:
            db.close()