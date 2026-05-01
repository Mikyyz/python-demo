from pydantic import BaseModel, Field
from app.core.orm_base import ORMBase

class LoginDTO(BaseModel, ORMBase):
  phone: str = Field(..., min_length=11, max_length=11)
  password: str = Field(..., min_length=6)

class LoginResponse(BaseModel):
  token: str
  user_id: str
  username: str