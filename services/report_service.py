from sqlalchemy import func

from database.session import SessionLocal
from database.models.invoice import Invoice
from database.models.product import Product
from database.models.customer import Customer


class ReportService:

    def __init__(self):
        self.db = SessionLocal()

    def get_sales_summary(self):
        total_sales = (
            self.db.query(
                func.sum(
                    Invoice.grand_total
                )
            )
            .scalar()
        )

        total_invoices = (
            self.db.query(
                Invoice
            )
            .count()
        )

        return {
            "sales":
                float(
                    total_sales or 0
                ),
            "invoices":
                total_invoices,
        }

    def get_product_report(self):
        return (
            self.db.query(Product)
            .all()
        )

    def get_customer_report(self):
        return (
            self.db.query(Customer)
            .all()
        )

    def get_low_stock_report(self):
        return (
            self.db.query(Product)
            .filter(
                Product.stock_quantity
                <= Product.minimum_stock
            )
            .all()
        )