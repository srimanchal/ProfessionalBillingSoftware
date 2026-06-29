from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QFrame,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
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

from app.signals import (
    app_signals,
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
        self.setup_signals()

    ########################################################
    # Signals
    ########################################################

    def setup_signals(self):
        app_signals.dashboard_refresh.connect(
            self.refresh_dashboard
        )

    ########################################################
    # Dashboard Refresh
    ########################################################

    def refresh_dashboard(self):
        old_layout = self.layout()

        if old_layout:
            QWidget().setLayout(
                old_layout
            )

        self.setup_ui()

    ########################################################
    # Company Header
    ########################################################

    def create_company_header(self):

        company = (
            self.company_service.get_company()
        )

        header = QFrame()
        header.setObjectName(
            "DashboardHeader"
        )

        layout = QGridLayout()

        layout.setContentsMargins(
            25,
            25,
            25,
            25,
        )

        layout.setHorizontalSpacing(
            30
        )

        ####################################################
        # Logo
        ####################################################

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
            and company.logo_path
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

        ####################################################
        # Company Details
        ####################################################

        details_layout = QVBoxLayout()

        company_name = QLabel(
            company.company_name
            if company
            else "Professional Billing Software"
        )

        company_name.setObjectName(
            "DashboardCompanyName"
        )

        details_layout.addWidget(
            company_name
        )

        if company:

            labels = [
                f"GSTIN : {company.gst_number or ''}",
                f"Phone : {company.phone or ''}",
                f"Email : {company.email or ''}",
                f"{company.address or ''}",
            ]

            for text in labels:
                lbl = QLabel(text)
                lbl.setObjectName(
                    "DashboardText"
                )
                details_layout.addWidget(
                    lbl
                )

        details_layout.addStretch()

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

    ########################################################
    # Dashboard Cards
    ########################################################

    def create_card(
        self,
        title,
        value,
    ):
        card = QFrame()

        card.setObjectName(
            "DashboardCard"
        )

        card.setMinimumHeight(
            130
        )

        layout = QVBoxLayout()

        title_label = QLabel(
            title
        )

        title_label.setObjectName(
            "DashboardCardTitle"
        )

        value_label = QLabel(
            str(value)
        )

        value_label.setObjectName(
            "DashboardCardValue"
        )

        layout.addWidget(
            title_label
        )

        layout.addStretch()

        layout.addWidget(
            value_label
        )

        card.setLayout(
            layout
        )

        return card

    ########################################################
    # UI
    ########################################################

    def setup_ui(self):

        layout = QVBoxLayout()

        layout.setContentsMargins(
            20,
            20,
            20,
            20,
        )

        layout.setSpacing(
            20
        )

        ####################################################
        # Company Header
        ####################################################

        layout.addWidget(
            self.create_company_header()
        )

        ####################################################
        # Dashboard Cards
        ####################################################

        grid = QGridLayout()
        grid.setSpacing(
            20
        )

        cards = [
            (
                "Products",
                self.viewmodel.get_total_products(),
            ),
            (
                "Customers",
                self.viewmodel.get_total_customers(),
            ),
            (
                "Invoices",
                self.viewmodel.get_total_invoices(),
            ),
            (
                "Today's Sales",
                self.viewmodel.get_today_sales(),
            ),
            (
                "Monthly Sales",
                self.viewmodel.get_month_sales(),
            ),
            (
                "Low Stock",
                len(
                    self.viewmodel
                    .get_low_stock_products()
                ),
            ),
        ]

        row = 0
        col = 0

        for title, value in cards:

            grid.addWidget(
                self.create_card(
                    title,
                    value,
                ),
                row,
                col,
            )

            col += 1

            if col > 2:
                col = 0
                row += 1

        layout.addLayout(
            grid
        )

        ####################################################
        # Monthly Sales Chart
        ####################################################

        chart_frame = QFrame()

        chart_frame.setObjectName(
            "DashboardCard"
        )

        chart_layout = QVBoxLayout()

        chart_title = QLabel(
            "Monthly Sales"
        )

        chart_title.setObjectName(
            "DashboardSectionTitle"
        )

        chart_layout.addWidget(
            chart_title
        )

        self.chart = pg.PlotWidget()

        self.chart.setMinimumHeight(
            320
        )

        self.chart.showGrid(
            x=True,
            y=True,
            alpha=0.3,
        )

        self.chart.setMouseEnabled(
            x=False,
            y=False,
        )

        self.chart.getPlotItem().hideButtons()

        sales = (
            self.viewmodel
            .get_monthly_sales_chart()
        )

        self.chart.plot(
            sales,
            pen=pg.mkPen(
                width=3
            ),
            symbol="o",
            symbolSize=8,
        )

        chart_layout.addWidget(
            self.chart
        )

        chart_frame.setLayout(
            chart_layout
        )

        layout.addWidget(
            chart_frame
        )

        ####################################################
        # Recent Invoices
        ####################################################

        table_frame = QFrame()

        table_frame.setObjectName(
            "DashboardCard"
        )

        table_layout = QVBoxLayout()

        recent_label = QLabel(
            "Recent Invoices"
        )

        recent_label.setObjectName(
            "DashboardSectionTitle"
        )

        table_layout.addWidget(
            recent_label
        )

        self.table = QTableWidget()

        self.table.setMinimumHeight(
            350
        )

        self.table.verticalHeader().setVisible(
            False
        )

        self.table.setAlternatingRowColors(
            True
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

        header = (
            self.table.horizontalHeader()
        )

        header.setSectionResizeMode(
            QHeaderView.Stretch
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

        table_layout.addWidget(
            self.table
        )

        table_frame.setLayout(
            table_layout
        )

        layout.addWidget(
            table_frame
        )

        self.setLayout(
            layout
        )