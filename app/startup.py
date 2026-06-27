from database.base import Base
from database.db import engine

import database.models


def initialize_database():
    Base.metadata.create_all(bind=engine)