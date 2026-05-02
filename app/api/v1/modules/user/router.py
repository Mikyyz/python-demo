from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session

from .service import get_users, get_user as service_get_user, create_user as service_create_user
from .schema import UserSchema, UserCreate
from app.core.deps import get_db
from app.core.response_model import ResponseModel
from app.core.helper import success, error

router = APIRouter(prefix="/user", tags=["user"])

# 获取用户列表
@router.get('/', response_model=ResponseModel[list[UserSchema]])
def list_users(db: Session = Depends(get_db)):
    users = get_users(db)
    return success(users)

# 获取单个用户
@router.get('/{user_id}', response_model=ResponseModel[UserSchema])
def get_user(user_id: str = Path(..., min_length=5, max_length=8), db: Session = Depends(get_db)):
    user = service_get_user(db, user_id)
    if user is None:
        raise HTTPException(
            status_code=404,
            detail=f"用户未找到"
        )
    return success(user)

# 创建用户
@router.post('/create', response_model=ResponseModel[UserSchema])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = service_create_user(db, user)
    return success(user)