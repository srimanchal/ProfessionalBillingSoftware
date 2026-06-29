from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QTextEdit,
)


class CustomerDialog(QDialog):

    def __init__(
        self,
        customer=None,
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

        self.resize(
            600,
            500,
        )

        layout = QVBoxLayout()

        form = QFormLayout()

        self.name = QLineEdit()
        self.phone = QLineEdit()
        self.email = QLineEdit()
        self.gst = QLineEdit()
        self.city = QLineEdit()
        self.state = QLineEdit()
        self.address = QTextEdit()

        self.name.setPlaceholderText(
            "Customer Name"
        )

        self.phone.setPlaceholderText(
            "Phone Number"
        )

        self.email.setPlaceholderText(
            "Email Address"
        )

        self.gst.setPlaceholderText(
            "GST Number"
        )

        self.city.setPlaceholderText(
            "City"
        )

        self.state.setPlaceholderText(
            "State"
        )

        self.address.setPlaceholderText(
            "Address"
        )

        form.addRow(
            "Customer Name",
            self.name,
        )

        form.addRow(
            "Phone",
            self.phone,
        )

        form.addRow(
            "Email",
            self.email,
        )

        form.addRow(
            "GST Number",
            self.gst,
        )

        form.addRow(
            "City",
            self.city,
        )

        form.addRow(
            "State",
            self.state,
        )

        form.addRow(
            "Address",
            self.address,
        )

        self.save_button = QPushButton(
            "Save Customer"
        )

        self.save_button.clicked.connect(
            self.validate_and_save
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

        self.state.setText(
            getattr(
                self.customer,
                "state",
                ""
            )
            or ""
        )

        self.address.setPlainText(
            getattr(
                self.customer,
                "address",
                ""
            )
            or ""
        )

    def validate_and_save(self):
        if not self.name.text().strip():
            return

        self.accept()

    def get_data(self):
        return {
            "customer_name":
                self.name.text().strip(),

            "phone":
                self.phone.text().strip(),

            "email":
                self.email.text().strip(),

            "gst_number":
                self.gst.text().strip(),

            "city":
                self.city.text().strip(),

            "state":
                self.state.text().strip(),

            "address":
                self.address.toPlainText().strip(),
        }