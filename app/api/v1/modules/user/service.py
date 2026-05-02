from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

from utils.generate_id import generate_id
from .model import User
from .schema import UserCreate


# 获取用户列表
def get_users(db: Session):
  return db.query(User).all()

# 获取单个用户
def get_user(db: Session, user_id: str):
  return db.query(User).filter(User.user_id == user_id).first()

# 创建用户
def create_user(db: Session, user: UserCreate):
  try:
      # 生成 user_id
      user_id = generate_id()

      # 密码加密
      password_hash = generate_password_hash(user.password)

      # 如果没有用户名,就使用手机号拼接生成一个
      if not user.username:
          user.username = f"user_{user.phone}"  # 更安全一点

      db_user = User(
          phone=user.phone,
          username=user.username,
          password_hash=password_hash,
          user_id=user_id
      )

      db.add(db_user)
      db.commit()
      db.refresh(db_user)

      return db_user

  except IntegrityError:
        db.rollback()
        raise ValueError("手机号已存在")