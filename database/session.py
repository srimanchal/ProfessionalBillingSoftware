from sqlalchemy.orm import sessionmaker
from database.db import engine

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)