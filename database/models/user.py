from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from datetime import datetime

from database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    username = Column(String(100), unique=True, nullable=False)

    password_hash = Column(String(500), nullable=False)

    full_name = Column(String(200))

    email = Column(String(200))

    role = Column(String(50), default="Administrator")

    is_active = Column(Boolean, default=True)

    last_login = Column(DateTime)

    created_at = Column(DateTime, default=datetime.utcnow)