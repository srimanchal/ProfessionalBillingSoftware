from decimal import Decimal

from database.session import SessionLocal
from database.models.product import Product
from database.repositories.product_repository import (
    ProductRepository
)


class ProductService:

    def __init__(self):
        self.db = SessionLocal()

        self.repository = ProductRepository(
            self.db
        )

    def get_products(self):
        return (
            self.repository
            .get_all_products()
        )

    def search_products(
        self,
        text,
    ):
        return self.repository.search(
            text
        )

    def add_product(
        self,
        data,
    ):
        product = Product(**data)

        return self.repository.add(
            product
        )

    def get_product(
        self,
        product_id,
    ):
        return self.repository.get_by_id(
            Product,
            product_id,
        )

    def update_product(
        self,
        product_id,
        data,
    ):
        product = self.get_product(
            product_id
        )

        if not product:
            return None

        for key, value in data.items():
            setattr(
                product,
                key,
                value,
            )

        self.repository.update()

        return product

    def delete_product(
        self,
        product_id,
    ):
        product = self.get_product(
            product_id
        )

        if product:
            self.repository.delete(
                product
            )

    def reduce_stock(
        self,
        product_id,
        quantity,
    ):
        product = self.repository.get_by_id(
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

        self.repository.update()