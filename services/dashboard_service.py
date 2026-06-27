from datetime import datetime
from sqlalchemy import func

from database.session import SessionLocal

from database.models.invoice import Invoice
from database.models.product import Product
from database.models.customer import Customer


class DashboardService:

    def __init__(self):
        self.db = SessionLocal()

    def get_total_products(self):
        return (
            self.db.query(Product)
            .count()
        )

    def get_total_customers(self):
        return (
            self.db.query(Customer)
            .count()
        )

    def get_total_invoices(self):
        return (
            self.db.query(Invoice)
            .count()
        )

    def get_today_sales(self):
        today = datetime.now().date()

        total = (
            self.db.query(
                func.sum(
                    Invoice.grand_total
                )
            )
            .filter(
                func.date(
                    Invoice.created_at
                ) == today
            )
            .scalar()
        )

        return float(total or 0)

    def get_month_sales(self):
        now = datetime.now()

        total = (
            self.db.query(
                func.sum(
                    Invoice.grand_total
                )
            )
            .filter(
                func.strftime(
                    "%Y",
                    Invoice.created_at
                )
                == str(now.year)
            )
            .filter(
                func.strftime(
                    "%m",
                    Invoice.created_at
                )
                == f"{now.month:02d}"
            )
            .scalar()
        )

        return float(total or 0)

    def get_low_stock_products(self):
        return (
            self.db.query(Product)
            .filter(
                Product.stock_quantity
                <= Product.minimum_stock
            )
            .all()
        )

    def get_recent_invoices(
        self,
        limit=10,
    ):
        return (
            self.db.query(Invoice)
            .order_by(
                Invoice.id.desc()
            )
            .limit(limit)
            .all()
        )

    def get_monthly_sales_chart(self):

        data = []

        for month in range(
            1,
            13,
        ):
            total = (
                self.db.query(
                    func.sum(
                        Invoice.grand_total
                    )
                )
                .filter(
                    func.strftime(
                        "%Y",
                        Invoice.created_at
                    )
                    == str(
                        datetime.now().year
                    )
                )
                .filter(
                    func.strftime(
                        "%m",
                        Invoice.created_at
                    )
                    == f"{month:02d}"
                )
                .scalar()
            )

            data.append(
                float(total or 0)
            )

        return data