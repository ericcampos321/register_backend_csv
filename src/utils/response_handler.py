def success_response(message: str, data: list | dict = None):
    return {"msg": message, "status": 1, "data": data if data is not None else []}


def error_response(message: str, error: str = "", data: list | dict = None):
    return {
        "msg": message,
        "status": 0,
        "error": error,
        "data": data if data is not None else [],
    }
