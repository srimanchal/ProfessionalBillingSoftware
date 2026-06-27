from database.repositories.base_repository import BaseRepository
from database.models.invoice import Invoice


class InvoiceRepository(BaseRepository):

    def get_by_invoice_number(self, invoice_number):
        return (
            self.session.query(Invoice)
            .filter(
                Invoice.invoice_number == invoice_number
            )
            .first()
        )