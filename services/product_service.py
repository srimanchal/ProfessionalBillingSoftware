from decimal import Decimal

from database.session import SessionLocal
from database.models.product import Product
from database.repositories.product_repository import (
    ProductRepository
)

from app.signals import app_signals


class ProductService:

    def get_products(self):
        db = SessionLocal()
        try:
            repository = ProductRepository(db)
            return repository.get_all_products()
        finally:
            db.close()

    def search_products(
        self,
        text,
    ):
        db = SessionLocal()
        try:
            repository = ProductRepository(db)
            return repository.search(text)
        finally:
            db.close()

    def add_product(
        self,
        data,
    ):
        db = SessionLocal()
        try:
            repository = ProductRepository(db)

            product = Product(**data)

            result = repository.add(
                product
            )

            app_signals.product_changed.emit()
            app_signals.dashboard_refresh.emit()

            return result
        finally:
            db.close()

    def get_product(
        self,
        product_id,
    ):
        db = SessionLocal()
        try:
            repository = ProductRepository(db)

            return repository.get_by_id(
                Product,
                product_id,
            )
        finally:
            db.close()

    def update_product(
        self,
        product_id,
        data,
    ):
        db = SessionLocal()
        try:
            repository = ProductRepository(db)

            product = repository.get_by_id(
                Product,
                product_id,
            )

            if not product:
                return None

            for key, value in data.items():
                setattr(
                    product,
                    key,
                    value,
                )

            repository.update()

            app_signals.product_changed.emit()
            app_signals.dashboard_refresh.emit()

            return product
        finally:
            db.close()

    def delete_product(
        self,
        product_id,
    ):
        db = SessionLocal()
        try:
            repository = ProductRepository(db)

            product = repository.get_by_id(
                Product,
                product_id,
            )

            if product:
                repository.delete(
                    product
                )

                app_signals.product_changed.emit()
                app_signals.dashboard_refresh.emit()
        finally:
            db.close()

    def reduce_stock(
        self,
        product_id,
        quantity,
    ):
        db = SessionLocal()

        try:
            repository = ProductRepository(db)

            product = repository.get_by_id(
                Product,
                product_id,
            )

            if not product:
                return

            current_stock = Decimal(
                str(
                    product.stock_quantity
                    or 0
                )
            )

            quantity = Decimal(
                str(quantity)
            )

            product.stock_quantity = (
                current_stock
                - quantity
            )

            repository.update()

            app_signals.product_changed.emit()
            app_signals.stock_changed.emit()
            app_signals.dashboard_refresh.emit()

        finally:
            db.close()