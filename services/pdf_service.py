from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import (
    getSampleStyleSheet,
)
from reportlab.platypus import (
    SimpleDocTemplate,
    Spacer,
    Paragraph,
    Table,
    TableStyle,
    Image,
)

from app.constants import (
    DOCUMENTS_DIR,
)


class PDFService:

    def get_safe_filename(
        self,
        invoice_number,
    ):
        return (
            invoice_number
            .replace("/", "-")
            .replace("\\", "-")
            .replace(":", "-")
            .replace("*", "")
            .replace("?", "")
            .replace('"', "")
            .replace("<", "")
            .replace(">", "")
            .replace("|", "")
        )

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

        safe_invoice_number = (
            self.get_safe_filename(
                invoice.invoice_number
            )
        )

        pdf_path = (
            invoice_dir
            / f"{safe_invoice_number}.pdf"
        )

        doc = SimpleDocTemplate(
            str(pdf_path),
            pagesize=A4,
            topMargin=20,
            bottomMargin=20,
        )

        styles = (
            getSampleStyleSheet()
        )

        elements = []

        # ==========================
        # Company Header
        # ==========================

        logo = ""

        if (
            company
            and company.logo_path
        ):
            try:
                logo = Image(
                    company.logo_path,
                    width=35 * mm,
                    height=35 * mm,
                )
            except:
                pass

        company_details = f"""
        <b>{company.company_name}</b><br/>
        {company.address or ''}<br/>
        {company.city or ''}, {company.state or ''}<br/>
        GSTIN : {company.gst_number or ''}<br/>
        Phone : {company.phone or ''}<br/>
        Email : {company.email or ''}
        """

        header = Table(
            [
                [
                    logo,
                    Paragraph(
                        company_details,
                        styles["Normal"],
                    ),
                ]
            ],
            colWidths=[
                45 * mm,
                135 * mm,
            ],
        )

        elements.append(
            header
        )

        elements.append(
            Spacer(1, 15)
        )

        elements.append(
            Paragraph(
                "<b>TAX INVOICE</b>",
                styles["Title"],
            )
        )

        elements.append(
            Spacer(1, 15)
        )

        # ==========================
        # Customer Details
        # ==========================

        customer_table = Table(
            [
                [
                    "Bill To",
                    "Invoice Details",
                ],
                [
                    customer.customer_name,
                    f"Invoice No : {invoice.invoice_number}",
                ],
                [
                    customer.phone or "",
                    f"Date : {invoice.invoice_date.strftime('%d-%m-%Y')}",
                ],
                [
                    customer.address or "",
                    f"Status : {invoice.payment_status}",
                ],
            ],
            colWidths=[
                90 * mm,
                90 * mm,
            ],
        )

        customer_table.setStyle(
            TableStyle(
                [
                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        1,
                        colors.black,
                    ),
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.lightgrey,
                    ),
                ]
            )
        )

        elements.append(
            customer_table
        )

        elements.append(
            Spacer(1, 15)
        )

        # ==========================
        # Items Table
        # ==========================

        rows = [
            [
                "Sl",
                "Product",
                "Qty",
                "Rate",
                "GST %",
                "GST",
                "Total",
            ]
        ]

        taxable_total = 0
        gst_total = 0

        for index, item in enumerate(
            items,
            start=1,
        ):
            taxable_total += float(
                item.taxable_amount
            )

            gst_total += float(
                item.gst_amount
            )

            rows.append(
                [
                    str(index),
                    item.product.product_name,
                    str(item.quantity),
                    str(item.rate),
                    str(
                        item.gst_percentage
                    ),
                    str(
                        item.gst_amount
                    ),
                    str(item.total),
                ]
            )

        item_table = Table(
            rows,
            repeatRows=1,
            colWidths=[
                15 * mm,
                60 * mm,
                20 * mm,
                25 * mm,
                20 * mm,
                25 * mm,
                25 * mm,
            ],
        )

        item_table.setStyle(
            TableStyle(
                [
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.HexColor(
                            "#1f4e78"
                        ),
                    ),
                    (
                        "TEXTCOLOR",
                        (0, 0),
                        (-1, 0),
                        colors.white,
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
            item_table
        )

        elements.append(
            Spacer(1, 15)
        )

        cgst = gst_total / 2
        sgst = gst_total / 2

        gst_table = Table(
            [
                [
                    "Taxable Amount",
                    f"{taxable_total:.2f}",
                ],
                [
                    "CGST",
                    f"{cgst:.2f}",
                ],
                [
                    "SGST",
                    f"{sgst:.2f}",
                ],
                [
                    "Total GST",
                    f"{gst_total:.2f}",
                ],
                [
                    "Grand Total",
                    f"{float(invoice.grand_total):.2f}",
                ],
            ],
            colWidths=[
                120 * mm,
                50 * mm,
            ],
        )

        gst_table.setStyle(
            TableStyle(
                [
                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        1,
                        colors.black,
                    ),
                    (
                        "BACKGROUND",
                        (0, -1),
                        (-1, -1),
                        colors.lightgrey,
                    ),
                ]
            )
        )

        elements.append(
            gst_table
        )

        doc.build(
            elements
        )

        return pdf_path