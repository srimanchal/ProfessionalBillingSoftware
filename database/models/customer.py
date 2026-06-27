from sqlalchemy import Column, Integer, String, Numeric, DateTime
from datetime import datetime
from database.base import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)

    customer_name = Column(String(200), nullable=False)
    phone = Column(String(30))
    email = Column(String(100))
    gst_number = Column(String(50))
    address = Column(String(500))
    city = Column(String(100))
    state = Column(String(100))
    pincode = Column(String(20))

    credit_limit = Column(Numeric(12, 2), default=0)
    outstanding_amount = Column(Numeric(12, 2), default=0)

    created_at = Column(DateTime, default=datetime.utcnow)