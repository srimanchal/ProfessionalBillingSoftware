from services.product_service import (
    ProductService
)


class ProductViewModel:

    def __init__(self):
        self.service = ProductService()

    def get_products(self):
        return self.service.get_products()

    def search_products(self, text):
        return (
            self.service.search_products(
                text
            )
        )

    def add_product(self, data):
        return self.service.add_product(
            data
        )

    def get_product(
        self,
        product_id
    ):
        return self.service.get_product(
            product_id
        )

    def update_product(
        self,
        product_id,
        data
    ):
        return (
            self.service.update_product(
                product_id,
                data
            )
        )

    def delete_product(
        self,
        product_id
    ):
        return (
            self.service.delete_product(
                product_id
            )
        )