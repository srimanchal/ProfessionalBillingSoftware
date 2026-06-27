from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Numeric
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from database.base import Base


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True)

    invoice_number = Column(String(100), unique=True)

    customer_id = Column(Integer, ForeignKey("customers.id"))

    invoice_date = Column(DateTime, default=datetime.utcnow)

    subtotal = Column(Numeric(12, 2), default=0)
    discount = Column(Numeric(12, 2), default=0)
    tax = Column(Numeric(12, 2), default=0)
    round_off = Column(Numeric(12, 2), default=0)
    grand_total = Column(Numeric(12, 2), default=0)
    paid_amount = Column(Numeric(12, 2), default=0)
    balance_amount = Column(Numeric(12, 2), default=0)

    payment_status = Column(String(50))
    invoice_type = Column(String(50))

    notes = Column(String(1000))

    created_at = Column(DateTime, default=datetime.utcnow)

    customer = relationship("Customer")
    items = relationship(
    "InvoiceItem",
    back_populates="invoice",
    cascade="all, delete-orphan"
)