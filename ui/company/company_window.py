from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox
)

from ui.company.company_viewmodel import (
    CompanyViewModel
)


class CompanyWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.viewmodel = CompanyViewModel()

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(
            "Company Setup"
        )

        self.resize(500, 450)

        layout = QVBoxLayout()

        title = QLabel(
            "Create Company"
        )

        self.company_name = QLineEdit()
        self.company_name.setPlaceholderText(
            "Company Name"
        )

        self.gst = QLineEdit()
        self.gst.setPlaceholderText(
            "GST Number"
        )

        self.phone = QLineEdit()
        self.phone.setPlaceholderText(
            "Phone"
        )

        self.email = QLineEdit()
        self.email.setPlaceholderText(
            "Email"
        )

        self.city = QLineEdit()
        self.city.setPlaceholderText(
            "City"
        )

        save_button = QPushButton(
            "Save Company"
        )

        save_button.clicked.connect(
            self.save_company
        )

        layout.addWidget(title)
        layout.addWidget(self.company_name)
        layout.addWidget(self.gst)
        layout.addWidget(self.phone)
        layout.addWidget(self.email)
        layout.addWidget(self.city)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def save_company(self):

        if not self.company_name.text().strip():
            QMessageBox.warning(
                self,
                "Validation",
                "Company name is required."
            )
            return

        data = {
            "company_name":
                self.company_name.text(),

            "gst_number":
                self.gst.text(),

            "phone":
                self.phone.text(),

            "email":
                self.email.text(),

            "city":
                self.city.text()
        }

        self.viewmodel.save_company(data)

        QMessageBox.information(
            self,
            "Success",
            "Company created successfully."
        )

        self.close()