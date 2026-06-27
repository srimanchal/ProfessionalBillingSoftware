from sqlalchemy import Column, Integer, String, Numeric, DateTime
from datetime import datetime
from database.base import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)

    expense_date = Column(DateTime, default=datetime.utcnow)

    category = Column(String(100))

    description = Column(String(500))

    amount = Column(Numeric(12, 2))