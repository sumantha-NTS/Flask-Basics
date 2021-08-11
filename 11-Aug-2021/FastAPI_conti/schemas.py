from datetime import date
from typing import List, Optional
from pydantic import BaseModel

class blog(BaseModel):
    title: str
    body: str
    class Config:
        orm_mode = True

class User(BaseModel):
    name: str
    email:str
    password:str
    DOB :date

class ShowUser(BaseModel):
    name: str
    email: str
    Blogs: List[blog] = []
    class Config:
        orm_mode = True

class ShowUser1(BaseModel):
    name: str
    email: str
    class Config:
        orm_mode = True
        
class ShowBlog(blog):
    creator: ShowUser1
    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None