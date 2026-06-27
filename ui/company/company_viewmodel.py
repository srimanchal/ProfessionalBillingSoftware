from services.company_service import CompanyService


class CompanyViewModel:

    def __init__(self):
        self.service = CompanyService()

    def company_exists(self):
        return self.service.get_company() is not None

    def save_company(self, data):
        return self.service.create_company(
            data
        )