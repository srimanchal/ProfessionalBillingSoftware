from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QFrame,
    QTableWidget,
    QTableWidgetItem,
)

import pyqtgraph as pg

from ui.dashboard.dashboard_analytics_viewmodel import (
    DashboardAnalyticsViewModel
)


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        self.viewmodel = (
            DashboardAnalyticsViewModel()
        )

        self.setup_ui()

    def create_card(
        self,
        title,
        value,
        ):
        card = QFrame()

        card.setStyleSheet("""
            QFrame{
                background-color:#ffffff;
                border:1px solid #cccccc;
                border-radius:12px;
                padding:15px;
            }
        """)

        layout = QVBoxLayout()

        title_label = QLabel(title)
        title_label.setStyleSheet("""
            color:#666666;
            font-size:14px;
            font-weight:bold;
            background:transparent;
        """)

        value_label = QLabel(str(value))
        value_label.setStyleSheet("""
            color:#000000;
            font-size:30px;
            font-weight:bold;
            background:transparent;
        """)

        layout.addWidget(title_label)
        layout.addWidget(value_label)

        card.setLayout(layout)

        return card

    def setup_ui(self):

        layout = QVBoxLayout()

        grid = QGridLayout()

        grid.addWidget(
            self.create_card(
                "Products",
                self.viewmodel
                .get_total_products(),
            ),
            0,
            0,
        )

        grid.addWidget(
            self.create_card(
                "Customers",
                self.viewmodel
                .get_total_customers(),
            ),
            0,
            1,
        )

        grid.addWidget(
            self.create_card(
                "Invoices",
                self.viewmodel
                .get_total_invoices(),
            ),
            0,
            2,
        )

        grid.addWidget(
            self.create_card(
                "Today's Sales",
                self.viewmodel
                .get_today_sales(),
            ),
            1,
            0,
        )

        grid.addWidget(
            self.create_card(
                "Monthly Sales",
                self.viewmodel
                .get_month_sales(),
            ),
            1,
            1,
        )

        grid.addWidget(
            self.create_card(
                "Low Stock",
                len(
                    self.viewmodel
                    .get_low_stock_products()
                ),
            ),
            1,
            2,
        )

        layout.addLayout(grid)

        # ======================
        # Sales Chart
        # ======================

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
            QLabel(
                "Monthly Sales"
            )
        )

        layout.addWidget(
            chart
        )

        # ======================
        # Recent Invoices
        # ======================

        layout.addWidget(
            QLabel(
                "Recent Invoices"
            )
        )

        self.table = (
            QTableWidget()
        )

        self.table.setColumnCount(3)

        self.table.setHorizontalHeaderLabels(
            [
                "Invoice",
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

        self.setLayout(layout)