from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, JSON, DateTime, Boolean, DDL, event
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Dog(Base):
    __tablename__ = "dogs"
    
    dog_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    characteristics = Column(JSON, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), default=func.now())
    is_expired = Column(Boolean, default=False)
    is_busy = Column(Boolean, default=False)
    last_activity_at = Column(DateTime, default=func.now())

    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)

    user = relationship("User")

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), default=func.now())

class Comment(Base):
    __tablename__ = "comments"

    comment_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    dog_id = Column(Integer, nullable=False)
    vote_count = Column(Integer, default=0)
    created_at = Column(DateTime, server_default=func.now(), default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), default=func.now())

class Vote(Base):
    __tablename__ = "votes"

    vote_id = Column(Integer, index=True, autoincrement=True)
    comment_id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), default=func.now())

