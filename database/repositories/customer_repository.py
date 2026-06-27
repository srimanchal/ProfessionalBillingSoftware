from database.repositories.base_repository import (
    BaseRepository
)

from database.models.customer import (
    Customer
)


class CustomerRepository(
    BaseRepository
):

    def get_all_customers(self):
        return (
            self.session.query(
                Customer
            )
            .order_by(
                Customer.customer_name
            )
            .all()
        )

    def search(
        self,
        text,
    ):
        return (
            self.session.query(
                Customer
            )
            .filter(
                Customer.customer_name.ilike(
                    f"%{text}%"
                )
            )
            .all()
        )