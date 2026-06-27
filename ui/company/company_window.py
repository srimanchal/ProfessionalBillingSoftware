from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QFormLayout,
    QTextEdit,
    QFileDialog,
    QMessageBox,
    QScrollArea,
)

from services.file_service import FileService
from ui.company.company_viewmodel import (
    CompanyViewModel
)


class CompanyWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.viewmodel = CompanyViewModel()

        self.logo_file = None
        self.signature_file = None

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(
            "Company Setup"
        )

        self.resize(
            700,
            800
        )

        main_layout = QVBoxLayout()

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        container = QWidget()

        form = QFormLayout()

        # Company Details

        self.company_name = QLineEdit()
        self.business_type = QLineEdit()
        self.gst_number = QLineEdit()
        self.pan_number = QLineEdit()
        self.email = QLineEdit()
        self.phone = QLineEdit()
        self.website = QLineEdit()
        self.address = QTextEdit()
        self.city = QLineEdit()
        self.state = QLineEdit()
        self.pincode = QLineEdit()
        self.country = QLineEdit()
        self.invoice_prefix = QLineEdit()
        self.financial_year = QLineEdit()
        self.currency = QLineEdit()
        self.tax_type = QLineEdit()

        # Logo

        self.logo_path = QLineEdit()
        self.logo_path.setReadOnly(True)

        self.logo_button = QPushButton(
            "Browse Logo"
        )

        self.logo_button.clicked.connect(
            self.browse_logo
        )

        # Signature

        self.signature_path = QLineEdit()
        self.signature_path.setReadOnly(True)

        self.signature_button = QPushButton(
            "Browse Signature"
        )

        self.signature_button.clicked.connect(
            self.browse_signature
        )

        # Bank Details

        self.bank_name = QLineEdit()
        self.bank_account = QLineEdit()
        self.ifsc_code = QLineEdit()
        self.branch_name = QLineEdit()
        self.upi_id = QLineEdit()

        # Terms

        self.terms_conditions = QTextEdit()

        # Form

        form.addRow(
            "Company Name",
            self.company_name
        )

        form.addRow(
            "Business Type",
            self.business_type
        )

        form.addRow(
            "GST Number",
            self.gst_number
        )

        form.addRow(
            "PAN Number",
            self.pan_number
        )

        form.addRow(
            "Email",
            self.email
        )

        form.addRow(
            "Phone",
            self.phone
        )

        form.addRow(
            "Website",
            self.website
        )

        form.addRow(
            "Address",
            self.address
        )

        form.addRow(
            "City",
            self.city
        )

        form.addRow(
            "State",
            self.state
        )

        form.addRow(
            "Pincode",
            self.pincode
        )

        form.addRow(
            "Country",
            self.country
        )

        form.addRow(
            "Invoice Prefix",
            self.invoice_prefix
        )

        form.addRow(
            "Financial Year",
            self.financial_year
        )

        form.addRow(
            "Currency",
            self.currency
        )

        form.addRow(
            "Tax Type",
            self.tax_type
        )

        form.addRow(
            "Company Logo",
            self.logo_button
        )

        form.addRow(
            "",
            self.logo_path
        )

        form.addRow(
            "Signature",
            self.signature_button
        )

        form.addRow(
            "",
            self.signature_path
        )

        form.addRow(
            "Bank Name",
            self.bank_name
        )

        form.addRow(
            "Account Number",
            self.bank_account
        )

        form.addRow(
            "IFSC Code",
            self.ifsc_code
        )

        form.addRow(
            "Branch Name",
            self.branch_name
        )

        form.addRow(
            "UPI ID",
            self.upi_id
        )

        form.addRow(
            "Terms & Conditions",
            self.terms_conditions
        )

        save_button = QPushButton(
            "Save Company"
        )

        save_button.clicked.connect(
            self.save_company
        )

        form.addRow(
            save_button
        )

        container.setLayout(
            form
        )

        scroll.setWidget(
            container
        )

        main_layout.addWidget(
            scroll
        )

        self.setLayout(
            main_layout
        )

    def browse_logo(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select Company Logo",
            "",
            "Images (*.png *.jpg *.jpeg)"
        )

        if file_name:
            self.logo_file = file_name
            self.logo_path.setText(
                file_name
            )

    def browse_signature(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select Signature",
            "",
            "Images (*.png *.jpg *.jpeg)"
        )

        if file_name:
            self.signature_file = file_name
            self.signature_path.setText(
                file_name
            )

    def save_company(self):

        if not self.company_name.text().strip():
            QMessageBox.warning(
                self,
                "Validation",
                "Company name is required."
            )
            return

        logo = FileService.save_logo(
            self.logo_file
        )

        signature = (
            FileService.save_signature(
                self.signature_file
            )
        )

        data = {
            "company_name":
                self.company_name.text(),

            "business_type":
                self.business_type.text(),

            "gst_number":
                self.gst_number.text(),

            "pan_number":
                self.pan_number.text(),

            "email":
                self.email.text(),

            "phone":
                self.phone.text(),

            "website":
                self.website.text(),

            "address":
                self.address.toPlainText(),

            "city":
                self.city.text(),

            "state":
                self.state.text(),

            "pincode":
                self.pincode.text(),

            "country":
                self.country.text(),

            "invoice_prefix":
                self.invoice_prefix.text(),

            "financial_year":
                self.financial_year.text(),

            "currency":
                self.currency.text(),

            "tax_type":
                self.tax_type.text(),

            "logo_path":
                logo,

            "signature_path":
                signature,

            "bank_name":
                self.bank_name.text(),

            "bank_account":
                self.bank_account.text(),

            "ifsc_code":
                self.ifsc_code.text(),

            "branch_name":
                self.branch_name.text(),

            "upi_id":
                self.upi_id.text(),

            "terms_conditions":
                self.terms_conditions.toPlainText(),
        }

        self.viewmodel.save_company(
            data
        )

        QMessageBox.information(
            self,
            "Success",
            "Company created successfully."
        )

        self.close()