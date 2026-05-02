from fastapi import FastAPI
from starlette.exceptions import HTTPException

from app.api.v1.router import api_router
from app.core.exception import (
    http_exception_handler,
    global_exception_handler
)

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")

# HTTP异常
app.add_exception_handler(
    HTTPException,
    http_exception_handler
)

# 全局异常
app.add_exception_handler(
    Exception,
    global_exception_handler
)