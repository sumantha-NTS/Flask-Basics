from pydantic import BaseModel

class blog(BaseModel):
    title: str
    author: str

class ShowBlog(blog):
    class Config:
        orm_mode = True

class User(BaseModel):
    Name: str
    email:str
    password:str