from fastapi import APIRouter,status,HTTPException,Depends
from sqlalchemy.orm import Session
from hashing import Hash
from typing import List
import schemas,models,oauth2
from database import get_db


router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.post('/',status_code=status.HTTP_201_CREATED)
def create_user(user:schemas.User,db:Session = Depends(get_db)):
    
    new_user = models.User(name = user.name,email = user.email,password = Hash.bcrypt(user.password),DOB = user.DOB)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}',response_model=schemas.ShowUser)
def show_user(id: int, db:Session = Depends(get_db),current_user = Depends(oauth2.get_current_user)):
    user_1 = db.query(models.User).filter(models.User.id == id).first()
    if not user_1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid user id")
    return user_1

@router.get('/',response_model=List[schemas.ShowUser])
def show_all_users(db:Session = Depends(get_db),current_user = Depends(oauth2.get_current_user)):
    return db.query(models.User).all()