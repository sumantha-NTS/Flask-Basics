from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Date
from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

class blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer,ForeignKey('User.id'))
    creator = relationship('User', back_populates='Blogs')


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    email = Column(String,unique=True)
    password = Column(String)
    DOB = Column(Date)
    Blogs = relationship('blog',back_populates='creator')