from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QFrame,
    QTableWidget,
    QTableWidgetItem,
)

from PySide6.QtGui import (
    QPixmap,
)

from PySide6.QtCore import Qt

import pyqtgraph as pg

from services.company_service import (
    CompanyService,
)

from ui.dashboard.dashboard_analytics_viewmodel import (
    DashboardAnalyticsViewModel,
)


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        self.viewmodel = (
            DashboardAnalyticsViewModel()
        )

        self.company_service = (
            CompanyService()
        )

        self.setup_ui()

    def create_company_header(self):

        company = (
            self.company_service.get_company()
        )

        header = QFrame()

        header.setStyleSheet("""
            QFrame{
                background-color:#ffffff;
                border:1px solid #dcdcdc;
                border-radius:15px;
                padding:20px;
            }
        """)

        layout = QGridLayout()

        # ==========================
        # Logo
        # ==========================

        logo_label = QLabel()
        logo_label.setFixedSize(
            120,
            120,
        )

        logo_label.setAlignment(
            Qt.AlignCenter
        )

        if (
            company
            and
            company.logo_path
        ):
            pixmap = QPixmap(
                company.logo_path
            )

            if not pixmap.isNull():

                pixmap = pixmap.scaled(
                    100,
                    100,
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation,
                )

                logo_label.setPixmap(
                    pixmap
                )

        # ==========================
        # Company Details
        # ==========================

        details_layout = QVBoxLayout()

        company_name = QLabel(
            company.company_name
            if company
            else "Professional Billing Software"
        )

        company_name.setStyleSheet("""
            font-size:26px;
            font-weight:bold;
        """)

        details_layout.addWidget(
            company_name
        )

        if company:

            gst = QLabel(
                f"GSTIN : {company.gst_number or ''}"
            )

            phone = QLabel(
                f"Phone : {company.phone or ''}"
            )

            email = QLabel(
                f"Email : {company.email or ''}"
            )

            address = QLabel(
                f"{company.address or ''}"
            )

            details_layout.addWidget(
                gst
            )

            details_layout.addWidget(
                phone
            )

            details_layout.addWidget(
                email
            )

            details_layout.addWidget(
                address
            )

        layout.addWidget(
            logo_label,
            0,
            0,
        )

        layout.addLayout(
            details_layout,
            0,
            1,
        )

        header.setLayout(
            layout
        )

        return header

    def create_card(
        self,
        title,
        value,
    ):

        card = QFrame()

        card.setStyleSheet("""
            QFrame{
                background-color:#ffffff;
                border:1px solid #dcdcdc;
                border-radius:15px;
                padding:15px;
            }
        """)

        layout = QVBoxLayout()

        title_label = QLabel(
            title
        )

        title_label.setStyleSheet("""
            color:#666666;
            font-size:14px;
            font-weight:bold;
        """)

        value_label = QLabel(
            str(value)
        )

        value_label.setStyleSheet("""
            color:#000000;
            font-size:30px;
            font-weight:bold;
        """)

        layout.addWidget(
            title_label
        )

        layout.addWidget(
            value_label
        )

        card.setLayout(
            layout
        )

        return card

    def setup_ui(self):

        layout = QVBoxLayout()

        # ==========================
        # Company Header
        # ==========================

        layout.addWidget(
            self.create_company_header()
        )

        # ==========================
        # Dashboard Cards
        # ==========================

        grid = QGridLayout()

        grid.addWidget(
            self.create_card(
                "Products",
                self.viewmodel.get_total_products(),
            ),
            0,
            0,
        )

        grid.addWidget(
            self.create_card(
                "Customers",
                self.viewmodel.get_total_customers(),
            ),
            0,
            1,
        )

        grid.addWidget(
            self.create_card(
                "Invoices",
                self.viewmodel.get_total_invoices(),
            ),
            0,
            2,
        )

        grid.addWidget(
            self.create_card(
                "Today's Sales",
                self.viewmodel.get_today_sales(),
            ),
            1,
            0,
        )

        grid.addWidget(
            self.create_card(
                "Monthly Sales",
                self.viewmodel.get_month_sales(),
            ),
            1,
            1,
        )

        grid.addWidget(
            self.create_card(
                "Low Stock",
                len(
                    self.viewmodel.get_low_stock_products()
                ),
            ),
            1,
            2,
        )

        layout.addLayout(
            grid
        )

        # ==========================
        # Sales Chart
        # ==========================

        chart_title = QLabel(
            "Monthly Sales"
        )

        chart_title.setStyleSheet("""
            font-size:18px;
            font-weight:bold;
        """)

        layout.addWidget(
            chart_title
        )

        chart = pg.PlotWidget()

        chart.setBackground(
            "w"
        )

        sales = (
            self.viewmodel
            .get_monthly_sales_chart()
        )

        chart.plot(
            sales,
            pen="b",
            symbol="o",
        )

        layout.addWidget(
            chart
        )

        # ==========================
        # Recent Invoices
        # ==========================

        recent_label = QLabel(
            "Recent Invoices"
        )

        recent_label.setStyleSheet("""
            font-size:18px;
            font-weight:bold;
        """)

        layout.addWidget(
            recent_label
        )

        self.table = (
            QTableWidget()
        )

        self.table.setColumnCount(
            3
        )

        self.table.setHorizontalHeaderLabels(
            [
                "Invoice Number",
                "Customer ID",
                "Total",
            ]
        )

        invoices = (
            self.viewmodel
            .get_recent_invoices()
        )

        self.table.setRowCount(
            len(invoices)
        )

        for row, invoice in enumerate(
            invoices
        ):
            self.table.setItem(
                row,
                0,
                QTableWidgetItem(
                    invoice.invoice_number
                ),
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(
                    str(
                        invoice.customer_id
                    )
                ),
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(
                    str(
                        invoice.grand_total
                    )
                ),
            )

        layout.addWidget(
            self.table
        )

        self.setLayout(
            layout
        )