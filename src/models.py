import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(50), nullable=False) 
    email = Column(String(50), nullable=False) 

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))   
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user_relation = relationship('user')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    media_relation = relationship('media')
    comment_relation = relationship('comment')
    user_relation = relationship('user')

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    tipo = Column(Integer, nullable=False)  
    url = Column(String(50), nullable=False)  
    post_id = Column(Integer, ForeignKey('post.id')) 
    post_relation = relationship('post')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    post_relation = relationship('post')
    user_relation = relationship('user') 

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
