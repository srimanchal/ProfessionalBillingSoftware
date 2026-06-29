from database.session import SessionLocal
from database.models.company import Company
from database.repositories.company_repository import (
CompanyRepository
)

class CompanyService:


    def get_company(
        self,
    ):
        db = SessionLocal()

        try:
            repository = (
                CompanyRepository(
                    db
                )
            )

            return (
                repository.get_company()
            )

        finally:
            db.close()

def create_company(
    self,
    data,
):
    db = SessionLocal()

    try:
        repository = (
            CompanyRepository(
                db
            )
        )

        company = Company(
            **data
        )

        return repository.add(
            company
        )

    finally:
        db.close()
