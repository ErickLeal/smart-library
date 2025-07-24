from fastapi.exception_handlers import RequestValidationError
from fastapi import Request
from fastapi.responses import JSONResponse
from app.errors.base import AppError, DatabaseError, UnexpectedError
from app.errors.base import AppError

class SucessResponseEnvelope:
    def __init__(self, data=None, status_code=200):
        self.data = data
    def dict(self):
        return {"success": True, "data": self.data}

class ErrorResponseEnvelope:
    def __init__(self, error=None):
        self.error = error
    def dict(self):
        return {"success": False, "error": self.error}

def error_handler(request: Request, exc: Exception):
    if isinstance(exc, AppError):
        envelope = ErrorResponseEnvelope(error={
            "code": exc.code,
            "message": exc.message,
            "meta": exc.meta
        })
        return JSONResponse(status_code=exc.http_status, content=envelope.dict())

    envelope = ErrorResponseEnvelope(success=False, error={
        "code": "unexpected_error",
        "message": "Erro inesperado. Tente novamente mais tarde."
    })
    return JSONResponse(status_code=500, content=envelope.dict())


def pydantic_validation_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    envelope = ErrorResponseEnvelope(error={
        "code": "validation_error",
        "message": "Erro de validação nos campos",
        "meta": {"details": errors}
    })
    return JSONResponse(status_code=422, content=envelope.dict())
