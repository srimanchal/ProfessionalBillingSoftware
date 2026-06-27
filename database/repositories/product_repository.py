from database.repositories.base_repository import (
    BaseRepository
)
from database.models.product import Product


class ProductRepository(
    BaseRepository
):

    def get_all_products(self):
        return (
            self.session.query(
                Product
            )
            .order_by(
                Product.product_name
            )
            .all()
        )

    def search(
        self,
        text,
    ):
        return (
            self.session.query(
                Product
            )
            .filter(
                Product.product_name.ilike(
                    f"%{text}%"
                )
            )
            .all()
        )