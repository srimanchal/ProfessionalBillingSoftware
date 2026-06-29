from services.customer_service import (
    CustomerService
)


class CustomerViewModel:

    def __init__(self):
        self.service = CustomerService()

    def get_customers(self):
        return self.service.get_customers()

    def search_customers(
        self,
        text,
    ):
        return (
            self.service.search_customers(
                text
            )
        )

    def add_customer(
        self,
        data,
    ):
        return (
            self.service.add_customer(
                data
            )
        )

    def get_customer(
        self,
        customer_id,
    ):
        return (
            self.service.get_customer(
                customer_id
            )
        )

    def get_customer_by_phone(
        self,
        phone,
    ):
        return (
            self.service
            .get_customer_by_phone(
                phone
            )
        )

    def update_customer(
        self,
        customer_id,
        data,
    ):
        return (
            self.service.update_customer(
                customer_id,
                data,
            )
        )

    def delete_customer(
        self,
        customer_id,
    ):
        return (
            self.service.delete_customer(
                customer_id
            )
        )