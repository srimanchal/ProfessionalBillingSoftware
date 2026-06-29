from database.session import SessionLocal
from database.models.customer import Customer
from database.repositories.customer_repository import (
    CustomerRepository
)

from app.signals import app_signals


class CustomerService:

    def get_customers(self):
        db = SessionLocal()

        try:
            repository = CustomerRepository(
                db
            )

            return (
                repository
                .get_all_customers()
            )

        finally:
            db.close()

    def search_customers(
        self,
        text,
    ):
        db = SessionLocal()

        try:
            repository = CustomerRepository(
                db
            )

            return repository.search(
                text
            )

        finally:
            db.close()

    def add_customer(
        self,
        data,
    ):
        db = SessionLocal()

        try:
            repository = CustomerRepository(
                db
            )

            customer = Customer(
                **data
            )

            result = repository.add(
                customer
            )

            app_signals.customer_changed.emit()
            app_signals.dashboard_refresh.emit()

            return result

        finally:
            db.close()

    def get_customer(
        self,
        customer_id,
    ):
        db = SessionLocal()

        try:
            repository = CustomerRepository(
                db
            )

            return repository.get_by_id(
                Customer,
                customer_id,
            )

        finally:
            db.close()

    def get_customer_by_phone(
        self,
        phone,
    ):
        db = SessionLocal()

        try:
            repository = CustomerRepository(
                db
            )

            return (
                repository.get_by_phone(
                    phone
                )
            )

        finally:
            db.close()

    def update_customer(
        self,
        customer_id,
        data,
    ):
        db = SessionLocal()

        try:
            repository = CustomerRepository(
                db
            )

            customer = (
                repository.get_by_id(
                    Customer,
                    customer_id,
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

            repository.update()

            app_signals.customer_changed.emit()
            app_signals.dashboard_refresh.emit()

            return customer

        finally:
            db.close()

    def delete_customer(
        self,
        customer_id,
    ):
        db = SessionLocal()

        try:
            repository = CustomerRepository(
                db
            )

            customer = (
                repository.get_by_id(
                    Customer,
                    customer_id,
                )
            )

            if customer:
                repository.delete(
                    customer
                )

                app_signals.customer_changed.emit()
                app_signals.dashboard_refresh.emit()

        finally:
            db.close()