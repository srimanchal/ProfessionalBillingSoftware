from datetime import datetime
from sqlalchemy import func

from database.session import SessionLocal

from database.models.invoice import Invoice
from database.models.product import Product
from database.models.customer import Customer


class DashboardService:

    def get_total_products(
        self,
    ):
        db = SessionLocal()

        try:
            return (
                db.query(Product)
                .count()
            )
        finally:
            db.close()

    def get_total_customers(
        self,
    ):
        db = SessionLocal()

        try:
            return (
                db.query(Customer)
                .count()
            )
        finally:
            db.close()

    def get_total_invoices(
        self,
    ):
        db = SessionLocal()

        try:
            return (
                db.query(Invoice)
                .count()
            )
        finally:
            db.close()

    def get_today_sales(
        self,
    ):
        db = SessionLocal()

        try:
            today = (
                datetime.now().date()
            )

            total = (
                db.query(
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

        finally:
            db.close()

    def get_month_sales(
        self,
    ):
        db = SessionLocal()

        try:
            now = datetime.now()

            total = (
                db.query(
                    func.sum(
                        Invoice.grand_total
                    )
                )
                .filter(
                    func.strftime(
                        "%Y",
                        Invoice.created_at,
                    )
                    == str(now.year)
                )
                .filter(
                    func.strftime(
                        "%m",
                        Invoice.created_at,
                    )
                    == f"{now.month:02d}"
                )
                .scalar()
            )

            return float(total or 0)

        finally:
            db.close()

    def get_low_stock_products(
        self,
    ):
        db = SessionLocal()

        try:
            return (
                db.query(Product)
                .filter(
                    Product.stock_quantity
                    <= Product.minimum_stock
                )
                .all()
            )

        finally:
            db.close()

    def get_recent_invoices(
        self,
        limit=10,
    ):
        db = SessionLocal()

        try:
            return (
                db.query(Invoice)
                .order_by(
                    Invoice.id.desc()
                )
                .limit(limit)
                .all()
            )

        finally:
            db.close()

    def get_monthly_sales_chart(
        self,
    ):
        db = SessionLocal()

        try:
            data = []

            current_year = (
                datetime.now().year
            )

            for month in range(
                1,
                13,
            ):
                total = (
                    db.query(
                        func.sum(
                            Invoice.grand_total
                        )
                    )
                    .filter(
                        func.strftime(
                            "%Y",
                            Invoice.created_at,
                        )
                        == str(
                            current_year
                        )
                    )
                    .filter(
                        func.strftime(
                            "%m",
                            Invoice.created_at,
                        )
                        == f"{month:02d}"
                    )
                    .scalar()
                )

                data.append(
                    float(total or 0)
                )

            return data

        finally:
            db.close()