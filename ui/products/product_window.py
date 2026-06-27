from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
)

from ui.products.product_viewmodel import ProductViewModel
from ui.products.product_dialog import ProductDialog


class ProductWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.viewmodel = ProductViewModel()

        self.setup_ui()
        self.load_products()

    def setup_ui(self):
        layout = QVBoxLayout()

        # ======================
        # Top Section
        # ======================

        top_layout = QHBoxLayout()

        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText(
            "Search products..."
        )

        self.add_button = QPushButton(
            "Add Product"
        )

        self.delete_button = QPushButton(
            "Delete Product"
        )

        top_layout.addWidget(
            self.search_box
        )

        top_layout.addWidget(
            self.add_button
        )

        top_layout.addWidget(
            self.delete_button
        )

        # ======================
        # Product Table
        # ======================

        self.table = QTableWidget()

        self.table.setColumnCount(4)

        self.table.setHorizontalHeaderLabels(
            [
                "ID",
                "Product Name",
                "SKU",
                "Selling Price",
            ]
        )

        self.table.setSelectionBehavior(
            QTableWidget.SelectRows
        )

        self.table.setEditTriggers(
            QTableWidget.NoEditTriggers
        )

        layout.addLayout(
            top_layout
        )

        layout.addWidget(
            self.table
        )

        self.setLayout(layout)

        # ======================
        # Events
        # ======================

        self.add_button.clicked.connect(
            self.add_product
        )

        self.delete_button.clicked.connect(
            self.delete_product
        )

        self.search_box.textChanged.connect(
            self.search_products
        )

        self.table.cellDoubleClicked.connect(
            self.edit_product
        )

    # ======================
    # Load Products
    # ======================

    def load_products(self):
        products = (
            self.viewmodel.get_products()
        )

        self.populate_table(
            products
        )

    # ======================
    # Populate Table
    # ======================

    def populate_table(
        self,
        products
    ):
        self.table.setRowCount(
            len(products)
        )

        for row, product in enumerate(
            products
        ):
            self.table.setItem(
                row,
                0,
                QTableWidgetItem(
                    str(product.id)
                ),
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(
                    product.product_name
                    or ""
                ),
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(
                    product.sku
                    or ""
                ),
            )

            self.table.setItem(
                row,
                3,
                QTableWidgetItem(
                    str(
                        product.selling_price
                        or 0
                    )
                ),
            )

        self.table.resizeColumnsToContents()

    # ======================
    # Search Products
    # ======================

    def search_products(self):
        text = self.search_box.text()

        products = (
            self.viewmodel.search_products(
                text
            )
        )

        self.populate_table(
            products
        )

    # ======================
    # Add Product
    # ======================

    def add_product(self):
        dialog = ProductDialog()

        if dialog.exec():

            data = {
                "product_name":
                    dialog.name.text(),

                "sku":
                    dialog.sku.text(),

                "selling_price":
                    float(
                        dialog.price.text()
                        or 0
                    ),

                "stock_quantity":
                    float(
                        dialog.stock.text()
                        or 0
                    ),
            }

            self.viewmodel.add_product(
                data
            )

            self.load_products()

    # ======================
    # Edit Product
    # ======================

    def edit_product(
        self,
        row,
        column,
    ):
        product_id = int(
            self.table.item(
                row,
                0
            ).text()
        )

        product = (
            self.viewmodel.get_product(
                product_id
            )
        )

        if not product:
            return

        dialog = ProductDialog(
            product
        )

        if dialog.exec():

            data = {
                "product_name":
                    dialog.name.text(),

                "sku":
                    dialog.sku.text(),

                "selling_price":
                    float(
                        dialog.price.text()
                        or 0
                    ),

                "stock_quantity":
                    float(
                        dialog.stock.text()
                        or 0
                    ),
            }

            self.viewmodel.update_product(
                product_id,
                data,
            )

            self.load_products()

    # ======================
    # Delete Product
    # ======================

    def delete_product(self):
        row = (
            self.table.currentRow()
        )

        if row < 0:
            QMessageBox.warning(
                self,
                "Delete Product",
                "Please select a product.",
            )
            return

        product_id = int(
            self.table.item(
                row,
                0
            ).text()
        )

        result = QMessageBox.question(
            self,
            "Delete Product",
            "Are you sure you want to delete this product?",
            QMessageBox.Yes
            | QMessageBox.No,
        )

        if result == QMessageBox.Yes:

            self.viewmodel.delete_product(
                product_id
            )

            self.load_products()