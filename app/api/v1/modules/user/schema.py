from pydantic import BaseModel, Field


class UserSchema(BaseModel):
  phone: str = Field(..., min_length=11, max_length=11)
  username: str | None = None

class UserCreate(BaseModel):
  phone: str = Field(..., min_length=11, max_length=11)
  password: str
  username: str | None = None