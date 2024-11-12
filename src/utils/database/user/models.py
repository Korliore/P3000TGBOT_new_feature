from __future__ import annotations


from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from utils.database.base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    birthday = Column(String, nullable=False)
    chat_id = Column(Integer, nullable=False)
    username = Column(String, nullable=True)
