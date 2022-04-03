"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from asyncio import current_task

from sqlalchemy import Column, MetaData, Integer, String, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_scoped_session
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

engine = create_async_engine(PG_CONN_URI, echo=True)
metadata = MetaData()
Base = declarative_base(bind=engine)

scoped_session_factory = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Session = async_scoped_session(scoped_session_factory, scopefunc=current_task)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    username = Column(String(), nullable=False)
    email = Column(String())
    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String(), nullable=False)
    body = Column(String(), nullable=False)
    user = relationship("User", back_populates="posts")



