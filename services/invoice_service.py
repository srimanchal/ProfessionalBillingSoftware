from datetime import datetime

from database.session import SessionLocal
from database.models.invoice import Invoice

from database.repositories.invoice_repository import (
InvoiceRepository,
)

from services.invoice_item_service import (
InvoiceItemService,
)

from services.product_service import (
ProductService,
)

from services.company_service import (
CompanyService,
)

from services.customer_service import (
CustomerService,
)

from services.pdf_service import (
PDFService,
)

from app.constants import (
DOCUMENTS_DIR,
)

from app.signals import app_signals

class InvoiceService:

    def __init__(self):
        self.item_service = InvoiceItemService()
        self.product_service = ProductService()
        self.company_service = CompanyService()
        self.customer_service = CustomerService()
        self.pdf_service = PDFService()

#################################################
# Get All Invoices
#################################################

    def get_invoices(self):
        db = SessionLocal()

        try:
            repository = InvoiceRepository(db)

            return (
                repository
                .get_all_invoices()
            )

        finally:
            db.close()

#################################################
# Search Invoices
#################################################

    def search_invoices(
        self,
        text,
    ):
        db = SessionLocal()

        try:
            repository = InvoiceRepository(db)

            return (
                repository
                .search_invoices(
                    text
                )
            )

        finally:
            db.close()

#################################################
# Get Invoice
#################################################

    def get_invoice(
        self,
        invoice_id,
    ):
        db = SessionLocal()

        try:
            repository = InvoiceRepository(db)

            return (
                repository
                .get_invoice(
                    invoice_id
                )
            )

        finally:
            db.close()

#################################################
# Generate Invoice Number
#################################################

    def generate_invoice_number(
        self,
    ):
        db = SessionLocal()

        try:
            repository = InvoiceRepository(db)

            last_invoice = (
                repository
                .get_latest_invoice()
            )

            today = datetime.now()

            if today.month >= 4:
                fy_start = today.year
                fy_end = (
                    today.year + 1
                ) % 100
            else:
                fy_start = (
                    today.year - 1
                )
                fy_end = (
                    today.year
                ) % 100

            financial_year = (
                f"{fy_start}-{fy_end:02d}"
            )

            sequence = 1

            if last_invoice:
                try:
                    invoice_no = (
                        last_invoice
                        .invoice_number
                    )

                    if financial_year in invoice_no:
                        sequence = int(
                            invoice_no.split("/")[-1]
                        ) + 1

                except:
                    sequence = 1

            return (
                f"INV/"
                f"{financial_year}/"
                f"{sequence:06d}"
            )

        finally:
            db.close()

#################################################
# Create Invoice
#################################################

    def create_invoice(
        self,
        invoice_data,
        items,
    ):
        db = SessionLocal()

        try:
            repository = InvoiceRepository(db)

            invoice = Invoice(
                **invoice_data
            )

            invoice = (
                repository.add(
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
                    "gst_percentage":
                        item.get(
                            "gst_percentage",
                            0,
                        ),
                    "gst_amount":
                        item.get(
                            "gst_amount",
                            0,
                        ),
                    "taxable_amount":
                        item.get(
                            "taxable_amount",
                            item["total"],
                        ),
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
                repository.get_invoice(
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

            app_signals.invoice_changed.emit()
            app_signals.dashboard_refresh.emit()
            app_signals.report_refresh.emit()

            return invoice

        finally:
            db.close()

#################################################
# Get PDF Path
#################################################

    def get_pdf_path(
        self,
        invoice_number,
    ):
        invoices_dir = (
            DOCUMENTS_DIR
            / "invoices"
        )

        safe_invoice_number = (
            invoice_number
            .replace("/", "-")
            .replace("\\", "-")
        )

        if not invoices_dir.exists():
            return None

        for file in invoices_dir.rglob(
            "*.pdf"
        ):
            if (
                file.stem
                == safe_invoice_number
            ):
                return file

        return None
