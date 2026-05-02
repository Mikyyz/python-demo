from sqlalchemy import Column, Integer, String
from app.core.database import Base
from pydantic import BaseModel

class Auth(Base):
    __tablename__ = "auth"

    id = Column(Integer, primary_key=True, index=True)  # ✅ 必须有
    phone = Column(String(11), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)

class AuthSchema(BaseModel):
    phone: str
    password: str