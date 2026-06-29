from sqlalchemy import or_

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
                or_(
                    Customer.phone.ilike(
                        f"%{text}%"
                    ),
                    Customer.customer_name.ilike(
                        f"%{text}%"
                    ),
                )
            )
            .order_by(
                Customer.customer_name
            )
            .all()
        )

    def get_by_phone(
        self,
        phone,
    ):
        return (
            self.session.query(
                Customer
            )
            .filter(
                Customer.phone == phone
            )
            .first()
        )