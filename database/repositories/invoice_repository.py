from sqlalchemy import or_

from database.repositories.base_repository import (
    BaseRepository
)

from database.models.invoice import (
    Invoice
)

from database.models.customer import (
    Customer
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

    def search_invoices(
        self,
        text,
    ):
        return (
            self.session.query(
                Invoice
            )
            .join(
                Customer,
                Invoice.customer_id
                == Customer.id,
            )
            .filter(
                or_(
                    Invoice.invoice_number.ilike(
                        f"%{text}%"
                    ),
                    Customer.customer_name.ilike(
                        f"%{text}%"
                    ),
                    Customer.phone.ilike(
                        f"%{text}%"
                    ),
                )
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

    def get_latest_invoice(
        self,
    ):
        return (
            self.session.query(
                Invoice
            )
            .order_by(
                Invoice.id.desc()
            )
            .first()
        )