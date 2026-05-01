from werkzeug.security import generate_password_hash

from app.core.orm_base import ORMBase
from sqlalchemy import Column, String
from app.core.database import Base


class Auth(ORMBase, Base):
  __tablename__ = "users"
  phone = Column(
    String(11),
    unique=True,
    nullable=False,
    index=True
  )
  password = Column(String(255), nullable=False)