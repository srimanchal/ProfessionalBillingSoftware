from database.repositories.base_repository import BaseRepository
from database.models.company import Company


class CompanyRepository(BaseRepository):

    def get_company(self):
        return self.session.query(Company).first()