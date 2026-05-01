from pydantic import BaseModel
from typing import Generic, Optional, TypeVar

T = TypeVar("T")

class ResponseModel(BaseModel, Generic[T]):
  code: int = 0
  message: str = 'success'
  data: Optional[T] = None