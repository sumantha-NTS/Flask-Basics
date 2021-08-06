from fastapi import FastAPI, Depends
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
@app.post('/blog')
def create_blog(blog:schemas.blog, db:Session = Depends(get_db)):
    new_blog = models.blog(title = blog.title, author = blog.author)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog')
def show_blogs(db:Session = Depends(get_db)):
    blogs = db.query(models.blog).all()
    return blogs


# ### to run in different port
# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1",port=9000)