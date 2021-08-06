from fastapi import FastAPI
import schemas,models
from database import engine


# initiating the FastAPI application
app = FastAPI()

models.Base.metadata.create_all(engine)

#post decorator
@app.post('/blog')
def create_blog(blog:schemas.blog):
    title = blog.title
    author = blog.author
    result = {'Blog title': title}
    result.update({'blog Author':author})
    return result



# ### to run in different port
# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1",port=9000)