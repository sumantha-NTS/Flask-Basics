from fastapi import APIRouter,Depends,status, HTTPException,Response
from sqlalchemy.orm import Session
from typing import List
import schemas,models
from database import get_db


router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

@router.get('/',response_model=List[schemas.ShowBlog])
def show_all(db:Session = Depends(get_db),limit: int = 10,):
    blogs = db.query(models.blog).limit(limit).all()
    return blogs

#post decorator
@router.post('/',status_code=status.HTTP_201_CREATED)
def create_blog(blog:schemas.blog, db:Session = Depends(get_db)):
    new_blog = models.blog(title = blog.title, body = blog.body,user_id =1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db:Session = Depends(get_db)):
    blog_delete = db.query(models.blog).filter(models.blog.id == id)

    if not blog_delete.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog id {id} not found")

    blog_delete.delete(synchronize_session=False)
    db.commit()
    return {'message':f'BBlog with id deleted'}

@router.put('/{id}',status_code = status.HTTP_202_ACCEPTED)
def update(id: int, blog: schemas.blog, db:Session = Depends(get_db)):
    blog_update = db.query(models.blog).filter(models.blog.id == id)

    if not blog_update.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog id {id} not found")

    blog_update.update({'title':blog.title,'body' : blog.body},synchronize_session=False)
    db.commit()
    updated = db.query(models.blog).filter(models.blog.id == id).first()
    return {'message':{'updated data':updated}}

@router.get('/{id}',response_model=schemas.ShowBlog)
def show_blog(id : int, response: Response, db:Session = Depends(get_db)):
    blog_1 = db.query(models.blog).filter(models.blog.id == id).first()

    if not blog_1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Out of range")

    return blog_1