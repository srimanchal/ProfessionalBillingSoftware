from database.session import SessionLocal
from database.models.customer import Customer
from database.repositories.customer_repository import (
    CustomerRepository
)


class CustomerService:

    def __init__(self):
        self.db = SessionLocal()

        self.repository = (
            CustomerRepository(
                self.db
            )
        )

    def get_customers(self):
        return (
            self.repository
            .get_all_customers()
        )

    def search_customers(
        self,
        text,
    ):
        return self.repository.search(
            text
        )

    def add_customer(
        self,
        data,
    ):
        customer = Customer(**data)

        return self.repository.add(
            customer
        )

    def get_customer(
        self,
        customer_id,
    ):
        return (
            self.repository.get_by_id(
                Customer,
                customer_id,
            )
        )

    def update_customer(
        self,
        customer_id,
        data,
    ):
        customer = (
            self.get_customer(
                customer_id
            )
        )

        if not customer:
            return None

        for key, value in data.items():
            setattr(
                customer,
                key,
                value,
            )

        self.repository.update()

        return customer

    def delete_customer(
        self,
        customer_id,
    ):
        customer = (
            self.get_customer(
                customer_id
            )
        )

        if customer:
            self.repository.delete(
                customer
            )