from services.report_service import (
    ReportService
)


class ReportViewModel:

    def __init__(self):
        self.service = (
            ReportService()
        )

    def get_sales_summary(self):
        return (
            self.service
            .get_sales_summary()
        )

    def get_product_report(self):
        return (
            self.service
            .get_product_report()
        )

    def get_customer_report(self):
        return (
            self.service
            .get_customer_report()
        )

    def get_low_stock_report(self):
        return (
            self.service
            .get_low_stock_report()
        )