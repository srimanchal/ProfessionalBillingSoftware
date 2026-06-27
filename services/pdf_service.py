from pathlib import Path
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Spacer,
    Paragraph,
    Table,
    TableStyle,
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from app.constants import (
    DOCUMENTS_DIR
)


class PDFService:

    def generate_invoice(
        self,
        company,
        customer,
        invoice,
        items,
    ):
        year = datetime.now().strftime(
            "%Y"
        )

        month = datetime.now().strftime(
            "%m"
        )

        invoice_dir = (
            DOCUMENTS_DIR
            / "invoices"
            / year
            / month
        )

        invoice_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        pdf_path = (
            invoice_dir
            / f"{invoice.invoice_number}.pdf"
        )

        doc = SimpleDocTemplate(
            str(pdf_path),
            pagesize=A4,
        )

        styles = (
            getSampleStyleSheet()
        )

        elements = []

        elements.append(
            Paragraph(
                company.company_name,
                styles["Title"],
            )
        )

        elements.append(
            Paragraph(
                f"Invoice Number : "
                f"{invoice.invoice_number}",
                styles["Normal"],
            )
        )

        elements.append(
            Paragraph(
                f"Customer : "
                f"{customer.customer_name}",
                styles["Normal"],
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        data = [
            [
                "Product",
                "Qty",
                "Price",
                "Total",
            ]
        ]

        for item in items:
            data.append(
                [
                    item.product.product_name,
                    str(item.quantity),
                    str(item.rate),
                    str(item.total),
                ]
            )

        data.append(
            [
                "",
                "",
                "Grand Total",
                str(
                    invoice.grand_total
                ),
            ]
        )

        table = Table(
            data,
            repeatRows=1,
        )

        table.setStyle(
            TableStyle(
                [
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.lightgrey,
                    ),
                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        1,
                        colors.black,
                    ),
                ]
            )
        )

        elements.append(
            table
        )

        doc.build(elements)

        return pdf_path