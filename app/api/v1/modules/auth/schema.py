from pydantic import BaseModel, Field

class LoginDTO(BaseModel):
  phone: str = Field(..., min_length=11, max_length=11)
  password: str = Field(..., min_length=6)

class LoginResponse(BaseModel):
  token: str
  user_id: str
  username: str