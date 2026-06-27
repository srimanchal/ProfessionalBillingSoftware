from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
)

from ui.products.product_window import (
    ProductWindow
)


class ProductsPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(
            ProductWindow()
        )

        self.setLayout(layout)