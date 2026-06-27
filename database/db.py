from sqlalchemy import create_engine
from app.constants import DATABASE_FILE

DATABASE_URL = f"sqlite:///{DATABASE_FILE}"

engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True
)