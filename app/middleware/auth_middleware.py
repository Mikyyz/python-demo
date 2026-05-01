from functools import wraps
from flask import request
from utils.jwt_util import parse_token
from utils.redis_client import redis_client
from app.core.helper import error

def auth_required(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    token = request.headers.get("Authorization")  # 从请求头中获取token
    if not token:
      return error("未登录", 401)
    payload = parse_token(token)
    user_id = payload.get("user_id")
    redis_token = redis_client.get(user_id)
    # Redis登录态校验
    if redis_token != token:
      return error("登录已失效", 401)
    return func(*args, **kwargs)

  return wrapper