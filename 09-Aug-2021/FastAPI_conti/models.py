from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

class blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    author = Column(String)

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)