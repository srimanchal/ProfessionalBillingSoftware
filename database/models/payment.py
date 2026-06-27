from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from datetime import datetime
from database.base import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)

    invoice_id = Column(Integer, ForeignKey("invoices.id"))

    payment_date = Column(DateTime, default=datetime.utcnow)

    payment_mode = Column(String(50))

    reference_number = Column(String(100))

    amount = Column(Numeric(12, 2))

    notes = Column(String(500))