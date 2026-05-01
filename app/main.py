from fastapi import FastAPI, HTTPException
from app.api.v1.router import api_router as user_router
from app.core.exception import http_exception_handler, global_exception_handler

app = FastAPI()

app.include_router(user_router, prefix="/api/v1")

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)