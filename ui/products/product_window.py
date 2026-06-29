from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QHeaderView,
)

from ui.products.product_viewmodel import (
    ProductViewModel
)

from ui.products.product_dialog import (
    ProductDialog
)

from app.signals import app_signals


class ProductWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.viewmodel = ProductViewModel()

        self.setup_ui()
        self.setup_signals()
        self.load_products()

    def setup_signals(self):
        app_signals.product_changed.connect(
            self.load_products
        )

    def setup_ui(self):
        self.setWindowTitle(
            "Products"
        )

        self.resize(
            1100,
            700,
        )

        layout = QVBoxLayout()

        # ==================================
        # Top Section
        # ==================================

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

        self.refresh_button = QPushButton(
            "Refresh"
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

        top_layout.addWidget(
            self.refresh_button
        )

        # ==================================
        # Product Table
        # ==================================

        self.table = QTableWidget()

        self.table.setColumnCount(
            6
        )

        self.table.setHorizontalHeaderLabels(
            [
                "ID",
                "Product Name",
                "SKU",
                "Price",
                "GST %",
                "Stock",
            ]
        )

        self.table.setSelectionBehavior(
            QTableWidget.SelectRows
        )

        self.table.setEditTriggers(
            QTableWidget.NoEditTriggers
        )

        self.table.verticalHeader().setVisible(
            False
        )

        self.table.verticalHeader().setDefaultSectionSize(
            35
        )

        self.table.setAlternatingRowColors(
            True
        )

        header = (
            self.table.horizontalHeader()
        )

        header.setSectionResizeMode(
            0,
            QHeaderView.ResizeToContents
        )

        header.setSectionResizeMode(
            1,
            QHeaderView.Stretch
        )

        header.setSectionResizeMode(
            2,
            QHeaderView.ResizeToContents
        )

        header.setSectionResizeMode(
            3,
            QHeaderView.ResizeToContents
        )

        header.setSectionResizeMode(
            4,
            QHeaderView.ResizeToContents
        )

        header.setSectionResizeMode(
            5,
            QHeaderView.ResizeToContents
        )

        layout.addLayout(
            top_layout
        )

        layout.addWidget(
            self.table
        )

        self.setLayout(
            layout
        )

        # ==================================
        # Events
        # ==================================

        self.add_button.clicked.connect(
            self.add_product
        )

        self.delete_button.clicked.connect(
            self.delete_product
        )

        self.refresh_button.clicked.connect(
            self.load_products
        )

        self.search_box.textChanged.connect(
            self.search_products
        )

        self.table.cellDoubleClicked.connect(
            self.edit_product
        )

    # ==================================
    # Load Products
    # ==================================

    def load_products(self):
        if self.search_box.text().strip():
            self.search_products()
            return

        products = (
            self.viewmodel.get_products()
        )

        self.populate_table(
            products
        )

    # ==================================
    # Populate Table
    # ==================================

    def populate_table(
        self,
        products,
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

            self.table.setItem(
                row,
                4,
                QTableWidgetItem(
                    str(
                        product.gst_percentage
                        or 0
                    )
                ),
            )

            self.table.setItem(
                row,
                5,
                QTableWidgetItem(
                    str(
                        product.stock_quantity
                        or 0
                    )
                ),
            )

    # ==================================
    # Search Products
    # ==================================

    def search_products(self):
        products = (
            self.viewmodel.search_products(
                self.search_box.text()
            )
        )

        self.populate_table(
            products
        )

    # ==================================
    # Add Product
    # ==================================

    def add_product(self):
        dialog = ProductDialog()

        if dialog.exec():

            data = (
                dialog.get_data()
            )

            self.viewmodel.add_product(
                data
            )

    # ==================================
    # Edit Product
    # ==================================

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

            data = (
                dialog.get_data()
            )

            self.viewmodel.update_product(
                product_id,
                data,
            )

    # ==================================
    # Delete Product
    # ==================================

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