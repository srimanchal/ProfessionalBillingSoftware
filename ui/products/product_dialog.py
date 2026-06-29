from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QPushButton,
)


class ProductDialog(QDialog):

    def __init__(
        self,
        product=None,
    ):
        super().__init__()

        self.product = product

        self.setup_ui()

        if self.product:
            self.load_product()

    def setup_ui(self):
        self.setWindowTitle(
            "Product"
        )

        self.resize(
            500,
            350,
        )

        layout = QVBoxLayout()

        form = QFormLayout()

        self.name = QLineEdit()

        self.sku = QLineEdit()

        self.price = QLineEdit()

        self.stock = QLineEdit()

        self.gst = QLineEdit()

        self.gst.setText(
            "18"
        )

        self.name.setPlaceholderText(
            "Product Name"
        )

        self.sku.setPlaceholderText(
            "SKU"
        )

        self.price.setPlaceholderText(
            "Selling Price"
        )

        self.stock.setPlaceholderText(
            "Stock Quantity"
        )

        self.gst.setPlaceholderText(
            "GST Percentage"
        )

        form.addRow(
            "Product Name",
            self.name,
        )

        form.addRow(
            "SKU",
            self.sku,
        )

        form.addRow(
            "Selling Price",
            self.price,
        )

        form.addRow(
            "Stock Quantity",
            self.stock,
        )

        form.addRow(
            "GST %",
            self.gst,
        )

        self.save_button = QPushButton(
            "Save Product"
        )

        self.save_button.clicked.connect(
            self.accept
        )

        layout.addLayout(
            form
        )

        layout.addWidget(
            self.save_button
        )

        self.setLayout(
            layout
        )

    def load_product(self):
        self.name.setText(
            self.product.product_name
            or ""
        )

        self.sku.setText(
            self.product.sku
            or ""
        )

        self.price.setText(
            str(
                self.product.selling_price
                or 0
            )
        )

        self.stock.setText(
            str(
                self.product.stock_quantity
                or 0
            )
        )

        self.gst.setText(
            str(
                self.product.gst_percentage
                or 18
            )
        )

    def get_data(self):
        return {
            "product_name":
                self.name.text().strip(),

            "sku":
                self.sku.text().strip(),

            "selling_price":
                float(
                    self.price.text()
                    or 0
                ),

            "stock_quantity":
                float(
                    self.stock.text()
                    or 0
                ),

            "gst_percentage":
                float(
                    self.gst.text()
                    or 18
                ),
        }