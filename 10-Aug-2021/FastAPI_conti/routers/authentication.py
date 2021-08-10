from logging import log
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from fastapi import status
import models,token_1
from database import get_db
from hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm

from fastapi import APIRouter

router = APIRouter(
    prefix='/login',
    tags=['Authentication']
)

@router.post('/')
def login(login: OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == login.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{login.username} not found")

    if not Hash.verify(user.password,login.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="incorrect password")

    access_token = token_1.create_access_token(data={"sub": user.email}    )
    return {"access_token": access_token, "token_type": "bearer"}