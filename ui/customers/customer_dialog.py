from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QPushButton
)


class CustomerDialog(QDialog):

    def __init__(
        self,
        customer=None
    ):
        super().__init__()

        self.customer = customer

        self.setup_ui()

        if self.customer:
            self.load_customer()

    def setup_ui(self):
        self.setWindowTitle(
            "Customer"
        )

        self.resize(500, 350)

        layout = QVBoxLayout()

        form = QFormLayout()

        self.name = QLineEdit()
        self.phone = QLineEdit()
        self.email = QLineEdit()
        self.gst = QLineEdit()
        self.city = QLineEdit()

        form.addRow(
            "Customer Name",
            self.name
        )

        form.addRow(
            "Phone",
            self.phone
        )

        form.addRow(
            "Email",
            self.email
        )

        form.addRow(
            "GST Number",
            self.gst
        )

        form.addRow(
            "City",
            self.city
        )

        self.save_button = QPushButton(
            "Save Customer"
        )

        self.save_button.clicked.connect(
            self.accept
        )

        layout.addLayout(form)
        layout.addWidget(
            self.save_button
        )

        self.setLayout(layout)

    def load_customer(self):
        self.name.setText(
            self.customer.customer_name
            or ""
        )

        self.phone.setText(
            self.customer.phone
            or ""
        )

        self.email.setText(
            self.customer.email
            or ""
        )

        self.gst.setText(
            self.customer.gst_number
            or ""
        )

        self.city.setText(
            self.customer.city
            or ""
        )