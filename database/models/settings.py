from sqlalchemy import Column, Integer, String
from database.base import Base


class Settings(Base):
    __tablename__ = "settings"

    id = Column(Integer, primary_key=True)

    key = Column(String(100), unique=True)
    value = Column(String(1000))