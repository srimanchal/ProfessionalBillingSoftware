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

from ui.customers.customer_viewmodel import (
    CustomerViewModel
)

from ui.customers.customer_dialog import (
    CustomerDialog
)


class CustomerWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.viewmodel = (
            CustomerViewModel()
        )

        self.setup_ui()

        self.load_customers()

    def setup_ui(self):
        layout = QVBoxLayout()

        top_layout = QHBoxLayout()

        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText(
            "Search customers..."
        )

        self.add_button = QPushButton(
            "Add Customer"
        )

        self.delete_button = QPushButton(
            "Delete Customer"
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

        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels(
            [
                "ID",
                "Customer Name",
                "Phone",
                "Email",
                "City",
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

        self.add_button.clicked.connect(
            self.add_customer
        )

        self.delete_button.clicked.connect(
            self.delete_customer
        )

        self.search_box.textChanged.connect(
            self.search_customers
        )

        self.table.cellDoubleClicked.connect(
            self.edit_customer
        )

    def load_customers(self):
        customers = (
            self.viewmodel.get_customers()
        )

        self.populate_table(
            customers
        )

    def populate_table(
        self,
        customers
    ):
        self.table.setRowCount(
            len(customers)
        )

        for row, customer in enumerate(
            customers
        ):
            self.table.setItem(
                row,
                0,
                QTableWidgetItem(
                    str(customer.id)
                )
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(
                    customer.customer_name
                    or ""
                )
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(
                    customer.phone
                    or ""
                )
            )

            self.table.setItem(
                row,
                3,
                QTableWidgetItem(
                    customer.email
                    or ""
                )
            )

            self.table.setItem(
                row,
                4,
                QTableWidgetItem(
                    customer.city
                    or ""
                )
            )

        self.table.resizeColumnsToContents()

    def search_customers(self):
        text = self.search_box.text()

        customers = (
            self.viewmodel.search_customers(
                text
            )
        )

        self.populate_table(
            customers
        )

    def add_customer(self):
        dialog = CustomerDialog()

        if dialog.exec():

            data = {
                "customer_name":
                    dialog.name.text(),

                "phone":
                    dialog.phone.text(),

                "email":
                    dialog.email.text(),

                "gst_number":
                    dialog.gst.text(),

                "city":
                    dialog.city.text(),
            }

            self.viewmodel.add_customer(
                data
            )

            self.load_customers()

    def edit_customer(
        self,
        row,
        column,
    ):
        customer_id = int(
            self.table.item(
                row,
                0
            ).text()
        )

        customer = (
            self.viewmodel.get_customer(
                customer_id
            )
        )

        if not customer:
            return

        dialog = CustomerDialog(
            customer
        )

        if dialog.exec():

            data = {
                "customer_name":
                    dialog.name.text(),

                "phone":
                    dialog.phone.text(),

                "email":
                    dialog.email.text(),

                "gst_number":
                    dialog.gst.text(),

                "city":
                    dialog.city.text(),
            }

            self.viewmodel.update_customer(
                customer_id,
                data
            )

            self.load_customers()

    def delete_customer(self):
        row = (
            self.table.currentRow()
        )

        if row < 0:
            QMessageBox.warning(
                self,
                "Delete Customer",
                "Please select a customer.",
            )
            return

        customer_id = int(
            self.table.item(
                row,
                0
            ).text()
        )

        result = QMessageBox.question(
            self,
            "Delete Customer",
            "Delete selected customer?",
            QMessageBox.Yes
            | QMessageBox.No,
        )

        if result == QMessageBox.Yes:

            self.viewmodel.delete_customer(
                customer_id
            )

            self.load_customers()