from typing import Any, Optional, Dict

from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc: APIException, context: Any) -> Optional[Response]:
    response = exception_handler(exc, context)
    try:
        if response is not None:
            response.data = {}
            errors: Dict[str, Any] = {}
            error_key = "error"
            if isinstance(exc, APIException):
                error_key = exc.default_code
            if isinstance(exc.detail, dict):
                errors[error_key] = {key: value for key, value in exc.detail.items()}
            elif isinstance(exc.detail, str):
                errors[error_key] = [exc.detail]
            else:
                errors[error_key] = exc.detail

            response.data["errors"] = errors
            response.data["status_code"] = response.status_code
    except Exception:
        raise exc
    return response


class ServerError(APIException):
    status_code = 500
    default_detail = {"error": "Something wrong"}
    default_code = "server_error"
