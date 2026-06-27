from services.company_service import CompanyService


class DashboardViewModel:

    def __init__(self):
        self.company_service = CompanyService()

    def get_company(self):
        return self.company_service.get_company()