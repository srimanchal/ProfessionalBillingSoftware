from database.session import SessionLocal
from database.models.company import Company
from database.repositories.company_repository import (
    CompanyRepository
)


class CompanyService:

    def __init__(self):
        self.db = SessionLocal()
        self.repository = CompanyRepository(
            self.db
        )

    def get_company(self):
        return self.repository.get_company()

    def create_company(self, data):

        company = Company(**data)

        return self.repository.add(company)