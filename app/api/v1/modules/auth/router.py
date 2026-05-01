from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .service import login as service_login
from .schema import LoginDTO, LoginResponse
from app.core.response_model import ResponseModel
from app.core.deps import get_db
from app.core.helper import success

router = APIRouter()

@router.post('/login', response_model=ResponseModel[LoginResponse])
def user_login(payload: LoginDTO, db: Session = Depends(get_db)):
  result, error = service_login(db, payload)
  if error:
    raise HTTPException(
          status_code=400,
          detail=error
        )
  return success(result)