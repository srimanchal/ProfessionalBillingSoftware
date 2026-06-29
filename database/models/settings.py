from sqlalchemy import (
    Column,
    Integer,
    String,
)

from database.base import Base


class Setting(Base):
    __tablename__ = "settings"

    id = Column(
        Integer,
        primary_key=True,
    )

    key = Column(
        String(200),
        unique=True,
        nullable=False,
    )

    value = Column(
        String(1000)
    )