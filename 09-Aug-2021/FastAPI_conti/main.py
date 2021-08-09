from fastapi import FastAPI, Depends, status, Response
from sqlalchemy.orm import Session
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


#post decorator
@app.post('/blog',status_code=status.HTTP_201_CREATED)
def create_blog(blog:schemas.blog, db:Session = Depends(get_db)):
    new_blog = models.blog(title = blog.title, author = blog.author)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog')
def show_all(db:Session = Depends(get_db),limit: int = 2):
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