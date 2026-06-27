from uuid import uuid4
from pathlib import Path

from database.session import SessionLocal
from database.models.invoice import Invoice
from database.models.invoice_item import InvoiceItem

from database.repositories.invoice_repository import (
    InvoiceRepository
)

from services.invoice_item_service import (
    InvoiceItemService
)

from services.product_service import (
    ProductService
)

from services.company_service import (
    CompanyService
)

from services.customer_service import (
    CustomerService
)

from services.pdf_service import (
    PDFService
)

from app.constants import DOCUMENTS_DIR


class InvoiceService:

    def __init__(self):
        self.db = SessionLocal()

        self.repository = InvoiceRepository(
            self.db
        )

        self.item_service = (
            InvoiceItemService()
        )

        self.product_service = (
            ProductService()
        )

        self.company_service = (
            CompanyService()
        )

        self.customer_service = (
            CustomerService()
        )

        self.pdf_service = PDFService()

    def get_invoices(self):
        return (
            self.repository
            .get_all_invoices()
        )

    def get_invoice(
        self,
        invoice_id,
    ):
        return (
            self.repository
            .get_invoice(
                invoice_id
            )
        )

    def generate_invoice_number(
        self,
    ):
        return (
            "INV-"
            + uuid4()
            .hex[:10]
            .upper()
        )

    def create_invoice(
        self,
        invoice_data,
        items,
    ):
        invoice = Invoice(
            **invoice_data
        )

        invoice = (
            self.repository.add(
                invoice
            )
        )

        for item in items:

            item_data = {
                "invoice_id":
                    invoice.id,
                "product_id":
                    item["product_id"],
                "quantity":
                    item["quantity"],
                "rate":
                    item["price"],
                "total":
                    item["total"],
            }

            self.item_service.create_item(
                item_data
            )

            self.product_service.reduce_stock(
                item["product_id"],
                item["quantity"],
            )

        invoice = (
            self.repository.get_invoice(
                invoice.id
            )
        )

        company = (
            self.company_service
            .get_company()
        )

        customer = (
            self.customer_service
            .get_customer(
                invoice.customer_id
            )
        )

        self.pdf_service.generate_invoice(
            company,
            customer,
            invoice,
            invoice.items,
        )

        return invoice

    def get_pdf_path(
        self,
        invoice_number,
    ):
        invoices_dir = (
            DOCUMENTS_DIR
            / "invoices"
        )

        for file in invoices_dir.rglob(
            "*.pdf"
        ):
            if (
                file.stem
                == invoice_number
            ):
                return file

        return None