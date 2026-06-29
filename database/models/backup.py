from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)
from datetime import datetime

from database.base import Base


class Backup(Base):
    __tablename__ = "backups"

    id = Column(
        Integer,
        primary_key=True,
    )

    file_name = Column(
        String(500)
    )

    backup_type = Column(
        String(50)
    )

    backup_date = Column(
        DateTime,
        default=datetime.utcnow,
    )

    size = Column(
        String(100)
    )