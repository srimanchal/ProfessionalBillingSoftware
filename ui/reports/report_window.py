from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
    QMessageBox
)

from openpyxl import Workbook

from ui.reports.report_viewmodel import (
    ReportViewModel
)


class ReportWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.viewmodel = (
            ReportViewModel()
        )

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        summary = (
            self.viewmodel
            .get_sales_summary()
        )

        self.sales_label = QLabel(
            f"Total Sales : ₹{summary['sales']}"
        )

        self.invoice_label = QLabel(
            f"Total Invoices : {summary['invoices']}"
        )

        self.export_button = QPushButton(
            "Export Product Report"
        )

        layout.addWidget(
            self.sales_label
        )

        layout.addWidget(
            self.invoice_label
        )

        layout.addWidget(
            self.export_button
        )

        self.setLayout(layout)

        self.export_button.clicked.connect(
            self.export_products
        )

    def export_products(self):

        products = (
            self.viewmodel
            .get_product_report()
        )

        workbook = Workbook()

        sheet = workbook.active
        sheet.title = "Products"

        sheet.append(
            [
                "ID",
                "Product",
                "SKU",
                "Price",
                "Stock",
            ]
        )

        for product in products:
            sheet.append(
                [
                    product.id,
                    product.product_name,
                    product.sku,
                    float(
                        product.selling_price
                        or 0
                    ),
                    float(
                        product.stock_quantity
                        or 0
                    ),
                ]
            )

        file_name, _ = (
            QFileDialog.getSaveFileName(
                self,
                "Save Report",
                "products.xlsx",
                "Excel (*.xlsx)"
            )
        )

        if file_name:
            workbook.save(
                file_name
            )

            QMessageBox.information(
                self,
                "Success",
                "Report exported."
            )