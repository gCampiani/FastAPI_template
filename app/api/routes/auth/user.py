from typing import List

from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app.db.session import get_session
from app.db.models.user import User
from app.schemas.user import UserBase, UserCreate, UserList
from app.services.security import authenticate_user, create_access_token, get_current_user

router = APIRouter()


@router.get("/list", response_model=List[UserList])
async def read_users(session: Session = Depends(get_session)):
    users = session.query(User).all()
    return [i.serialize for i in users]


@router.post("/create", status_code=201)
async def create_user(user: UserCreate, session: Session = Depends(get_session)):
    try:
        db_user = User(email=user.email, password=user.password, admin=user.admin)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return {"email": user.email}
    except:
        raise HTTPException(status_code=409, detail="Email already in use")


@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user = authenticate_user(session.query(User), form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user.serialize


