from __future__ import annotations

from config import databases
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.database.base import Base

engine = create_engine(databases.DB_URL)

SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
)

