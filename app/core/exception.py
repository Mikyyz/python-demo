from fastapi.responses import JSONResponse
from fastapi import Request, HTTPException

async def http_exception_handler(request: Request, exc: HTTPException):
  return JSONResponse(
        status_code=exc.status_code,
        content={
            "status_code": exc.status_code,
            "msg": exc.detail,
            "data": None
        },
    )

# 全局异常
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "status_code": 500,
            "msg": "服务器异常",
            "data": None
        },
    )