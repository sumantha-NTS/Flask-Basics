from logging import log
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from fastapi import status
import schemas,models
from database import get_db
from hashing import Hash

from fastapi import APIRouter

router = APIRouter(
    prefix='/login',
    tags=['Authentication']
)

@router.post('/')
def login(login: schemas.Login,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == login.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{login.username} not found")

    if not Hash.verify(user.password,login.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="incorrect password")

    return user