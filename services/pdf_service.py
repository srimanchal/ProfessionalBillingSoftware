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
            topMargin=20,
            bottomMargin=20,
        )

        styles = (
            getSampleStyleSheet()
        )

        elements = []

        # =================================
        # COMPANY HEADER
        # =================================

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
                logo = ""

        company_details = f"""
        <b>{company.company_name}</b><br/>
        {company.address or ''}<br/>
        {company.city or ''}, {company.state or ''}<br/>
        GSTIN : {company.gst_number or ''}<br/>
        Phone : {company.phone or ''}<br/>
        Email : {company.email or ''}<br/>
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

        # =================================
        # INVOICE TITLE
        # =================================

        title = Paragraph(
            "<b> TAX INVOICE </b>",
            styles["Title"],
        )

        elements.append(
            title
        )

        elements.append(
            Spacer(1, 10)
        )

        # =================================
        # BILL TO + INVOICE DETAILS
        # =================================

        customer_data = [
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
                f"Payment Status : {invoice.payment_status or ''}",
            ],
        ]

        customer_table = Table(
            customer_data,
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

        # =================================
        # ITEMS TABLE
        # =================================

        rows = [
            [
                "Sl",
                "Description",
                "Qty",
                "Rate",
                "Discount",
                "GST",
                "Amount",
            ]
        ]

        count = 1

        for item in items:
            rows.append(
                [
                    str(count),
                    item.product.product_name,
                    str(item.quantity),
                    str(item.rate),
                    str(
                        item.discount
                        or 0
                    ),
                    str(
                        item.tax
                        or 0
                    ),
                    str(item.total),
                ]
            )

            count += 1

        item_table = Table(
            rows,
            repeatRows=1,
            colWidths=[
                15 * mm,
                65 * mm,
                20 * mm,
                25 * mm,
                25 * mm,
                20 * mm,
                30 * mm,
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

        # =================================
        # TOTALS
        # =================================

        totals = [
            [
                "Subtotal",
                str(invoice.subtotal),
            ],
            [
                "Discount",
                str(invoice.discount),
            ],
            [
                "Tax",
                str(invoice.tax),
            ],
            [
                "Round Off",
                str(invoice.round_off),
            ],
            [
                "Grand Total",
                str(invoice.grand_total),
            ],
        ]

        totals_table = Table(
            totals,
            colWidths=[
                120 * mm,
                50 * mm,
            ],
        )

        totals_table.setStyle(
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
            totals_table
        )

        elements.append(
            Spacer(1, 15)
        )

        # =================================
        # BANK DETAILS
        # =================================

        if company.bank_name:

            bank_text = f"""
            <b>Bank Details</b><br/>
            Bank : {company.bank_name}<br/>
            Account : {company.bank_account}<br/>
            IFSC : {company.ifsc_code}<br/>
            UPI : {company.upi_id}
            """

            elements.append(
                Paragraph(
                    bank_text,
                    styles["Normal"],
                )
            )

            elements.append(
                Spacer(1, 15)
            )

        # =================================
        # TERMS
        # =================================

        if company.terms_conditions:

            elements.append(
                Paragraph(
                    "<b>Terms & Conditions</b>",
                    styles["Heading3"],
                )
            )

            elements.append(
                Paragraph(
                    company.terms_conditions,
                    styles["Normal"],
                )
            )

            elements.append(
                Spacer(1, 15)
            )

        # =================================
        # SIGNATURE
        # =================================

        if company.signature_path:

            try:
                sign = Image(
                    company.signature_path,
                    width=40 * mm,
                    height=20 * mm,
                )

                elements.append(
                    sign
                )

            except:
                pass

        elements.append(
            Paragraph(
                "Authorized Signatory",
                styles["Normal"],
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        # =================================
        # FOOTER
        # =================================

        elements.append(
            Paragraph(
                "Thank you for your business.",
                styles["Normal"],
            )
        )

        elements.append(
            Paragraph(
                "This is a computer generated invoice.",
                styles["Normal"],
            )
        )

        doc.build(
            elements
        )

        return pdf_path