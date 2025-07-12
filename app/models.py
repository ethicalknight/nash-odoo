from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from .db import Base  # ✅ works now

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    location = Column(String)
    photo = Column(String)
    is_public = Column(Boolean)
    is_admin = Column(Boolean)
    # skills = relationship(...)  # continue as needed
