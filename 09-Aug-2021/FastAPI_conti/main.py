from fastapi import FastAPI, Depends, status, Response,HTTPException
from sqlalchemy.orm import Session

import schemas,models
from database import SessionLocal, engine
from typing import List
from passlib import CryptContext


# initiating the FastAPI application
app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def welocme():
    return {'message':'App is working'}

#post decorator
@app.post('/blog',status_code=status.HTTP_201_CREATED)
def create_blog(blog:schemas.blog, db:Session = Depends(get_db)):
    new_blog = models.blog(title = blog.title, author = blog.author)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db:Session = Depends(get_db)):
    blog_delete = db.query(models.blog).filter(models.blog.id == id)

    if not blog_delete.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog id {id} not found")

    blog_delete.delete(synchronize_session=False)
    db.commit()
    return {'message':f'BBlog with id deleted'}

@app.put('/blog/{id}',status_code = status.HTTP_202_ACCEPTED)
def update(id: int, blog: schemas.blog, db:Session = Depends(get_db)):
    blog_update = db.query(models.blog).filter(models.blog.id == id)

    if not blog_update.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog id {id} not found")

    blog_update.update({'title':blog.title,'author' : blog.author},synchronize_session=False)
    db.commit()
    updated = db.query(models.blog).filter(models.blog.id == id).first()
    return {'message':{'updated data':updated}}

@app.get('/blog',response_model=List[schemas.ShowBlog])
def show_all(db:Session = Depends(get_db),limit: int = 10,):
    blogs = db.query(models.blog).limit(limit).all()
    return blogs

@app.get('/blog/{id}',response_model=schemas.ShowBlog)
def show_blog(id : int, response: Response, db:Session = Depends(get_db)):
    blog_1 = db.query(models.blog).filter(models.blog.id == id).first()

    if not blog_1:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message':'Blog id is out of range'}

    return blog_1

@app.post('/user',status_code=status.HTTP_201_CREATED)
def create_user(user:schemas.User,db:Session = Depends(get_db)):
    new_user = models.User(name = user.Name,email = user.email,password = user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user