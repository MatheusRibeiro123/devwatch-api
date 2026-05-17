from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from app.exceptions.database_exceptions import DatabaseConnectionError
import logging

logger = logging.getLogger(__name__)

def register_handlers(app):

    @app.exception_handler(DatabaseConnectionError)
    async def database_connection_exception_handler(request: Request, exc: DatabaseConnectionError):
        
        logger.exception(f"unexpected error: {exc}")
        
        return JSONResponse(
            status_code=503,
            content={"error": "Ocorreu um erro de conexão com o banco de dados."}
        )
    
    @app.exception_handler(SQLAlchemyError)
    async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
        
        logger.exception(f"unexpected error: {exc}")
        
        return JSONResponse(
            status_code=500,
            content={"error": "Ocorreu um erro relacionado ao banco de dados."}
        )
    
    
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        
        logger.exception(f"unexpected error: {exc}")
        
        return JSONResponse(
            status_code=500,
            content={"error": "Ocorreu um erro interno no servidor."}
        )

    