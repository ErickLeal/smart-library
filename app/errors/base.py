from typing import Optional, Dict, Any

class AppError(Exception):
    def __init__(self, message: str, http_status: int = 500, code: str = "error", meta: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.message = message
        self.http_status = http_status
        self.code = code
        self.meta = meta or {}

class DatabaseError(AppError):
    def __init__(self, message: str = "Erro de banco de dados", http_status: int = 400, code: str = "db_error", meta: Optional[Dict[str, Any]] = None):
        super().__init__(message, http_status, code, meta)

class UnexpectedError(AppError):
    def __init__(self, message: str = "Erro inesperado", http_status: int = 500, code: str = "unexpected_error", meta: Optional[Dict[str, Any]] = None):
        super().__init__(message, http_status, code, meta)
