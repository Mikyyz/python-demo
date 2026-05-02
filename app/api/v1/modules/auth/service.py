from sqlalchemy.orm import Session
from werkzeug.security import check_password_hash

from app.api.v1.modules.auth.model import Auth
from app.api.v1.modules.user.model import User
from utils.jwt_util import generate_token as jwt_generate_token
from utils.redis_client import redis_client

from .model import Auth
from .schema import LoginDTO, LoginResponse

def get_user_by_phone(db: Session, phone: str):
  return db.query(User).filter(User.phone == phone).first()

# 登录
def login(db: Session, payload: LoginDTO):
  # 获取user
  user = get_user_by_phone(db, payload.phone)
  if not user:
    return None, "用户不存在"
  # 密码校验
  if not check_password_hash(user.password_hash, payload.password):
    return None, "密码错误"
  
  # 生成token
  token = jwt_generate_token(user.user_id)
  # 存入redis
  redis_client.setex(f"login:{user.user_id}", 60 * 60 * 24 * 7, token)

  return LoginResponse(
    token=token,
    user_id=user.user_id,
    username=user.username
), None