from src.services.OperatorService.operator_service import OperatorService

class OperatorController:
    def __init__(self):
        self.service = OperatorService()

    def search_operator(self, search: str):
        return self.service.search_operator(search)