from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text
from app.core.database import Base
class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  # 业务ID（对外暴露）
  user_id = Column(String(12), unique=True, index=True)
  # 登录标识
  phone = Column(String(11), unique=True, index=True)
  # 密码（存 hash，不是明文）
  password_hash = Column(String(512))
  username = Column(String(50), nullable=True)
  # 用户头像
  avatar = Column(Text, default='https://p3-pc-sign.douyinpic.com/aweme-avatar/tos-cn-avt-0015_4ef34667bb36bfe28b21f558fe79fe86~tplv-8yspqt5zfm-300x300.webp?lk3s=93de098e&x-expires=1777827600&x-signature=Y7BquO6DKk6N1jN3wDoL%2FtkwYRU%3D&from=2480802190&s=profile&se=false&sc=avatar&l=20260502011828CC2C36B537F67F3ECC16')
  # 用户状态
  is_active = Column(Boolean, default=True)
  # 时间
  created_at = Column(DateTime, default=datetime.now, nullable=False)