from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QPushButton
)


class ProductDialog(QDialog):

    def __init__(
        self,
        product=None
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

        self.resize(400, 250)

        layout = QVBoxLayout()

        form = QFormLayout()

        self.name = QLineEdit()
        self.sku = QLineEdit()
        self.price = QLineEdit()
        self.stock = QLineEdit()

        form.addRow(
            "Product Name",
            self.name
        )

        form.addRow(
            "SKU",
            self.sku
        )

        form.addRow(
            "Selling Price",
            self.price
        )

        form.addRow(
            "Stock Quantity",
            self.stock
        )

        self.save_button = QPushButton(
            "Save"
        )

        self.save_button.clicked.connect(
            self.accept
        )

        layout.addLayout(form)
        layout.addWidget(
            self.save_button
        )

        self.setLayout(layout)

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