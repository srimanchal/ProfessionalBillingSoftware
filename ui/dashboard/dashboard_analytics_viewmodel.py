from services.dashboard_service import (
    DashboardService
)


class DashboardAnalyticsViewModel:

    def __init__(self):
        self.service = DashboardService()

    def get_total_products(self):
        return (
            self.service
            .get_total_products()
        )

    def get_total_customers(self):
        return (
            self.service
            .get_total_customers()
        )

    def get_total_invoices(self):
        return (
            self.service
            .get_total_invoices()
        )

    def get_today_sales(self):
        return (
            self.service
            .get_today_sales()
        )

    def get_month_sales(self):
        return (
            self.service
            .get_month_sales()
        )

    def get_low_stock_products(self):
        return (
            self.service
            .get_low_stock_products()
        )

    def get_recent_invoices(self):
        return (
            self.service
            .get_recent_invoices()
        )

    def get_monthly_sales_chart(self):
        return (
            self.service
            .get_monthly_sales_chart()
        )