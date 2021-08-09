from fastapi import FastAPI, Depends, status, Response
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import false
import schemas,models
from database import SessionLocal, engine


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
    db.query(models.blog).filter(models.blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {'message':f'BBlog with id deleted'}

@app.put('/blog/{id}',status_code = status.HTTP_202_ACCEPTED)
def update(id: int, blog: schemas.blog, db:Session = Depends(get_db)):
    db.query(models.blog).filter(models.blog.id == id).update({'title':blog.title,'author' : blog.author},synchronize_session=False)
    db.commit()
    updated = db.query(models.blog).filter(models.blog.id == id).first()
    return {'message':{'updated data':updated}}

@app.get('/blog')
def show_all(db:Session = Depends(get_db),limit: int = 10):
    blogs = db.query(models.blog).limit(limit).all()
    return blogs

@app.get('/blog/{id}')
def show_blog(id : int, response: Response, db:Session = Depends(get_db)):
    blog_1 = db.query(models.blog).filter(models.blog.id == id).first()
    if not blog_1:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message':'Blog id is out of range'}
    return blog_1


# ### to run in different port
# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1",port=9000)