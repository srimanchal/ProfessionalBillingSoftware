from database.repositories.base_repository import (
    BaseRepository
)

from database.models.invoice import (
    Invoice
)


class InvoiceRepository(
    BaseRepository
):

    def get_all_invoices(
        self,
    ):
        return (
            self.session.query(
                Invoice
            )
            .order_by(
                Invoice.id.desc()
            )
            .all()
        )

    def get_by_invoice_number(
        self,
        invoice_number,
    ):
        return (
            self.session.query(
                Invoice
            )
            .filter(
                Invoice.invoice_number
                == invoice_number
            )
            .first()
        )

    def get_invoice(
        self,
        invoice_id,
    ):
        return (
            self.session.query(
                Invoice
            )
            .filter(
                Invoice.id
                == invoice_id
            )
            .first()
        )