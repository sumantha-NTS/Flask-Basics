from fastapi import FastAPI

import models
from database import engine
from routers import blogs, user, authentication


# initiating the FastAPI application
app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blogs.router)
app.include_router(user.router)


@app.get('/')
def welocme():
    return {'message':'App is working'}