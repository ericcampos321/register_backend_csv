from fastapi import APIRouter, Query
from src.controller.OperatorController.operator_controller import OperatorController
from src.utils.response_handler import success_response, error_response

router = APIRouter()
controller = OperatorController()


@router.get("/operators/search")
def search_operator(search: str = Query(None, alias="search")):
    try:
        result = controller.search_operator(search)
        return success_response("Busca realizada com sucesso.", result)
    except Exception as e:
        return error_response("Erro ao buscar operadoras", str(e))
