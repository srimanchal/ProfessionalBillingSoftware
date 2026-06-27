from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from datetime import datetime

from database.base import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)

    company_name = Column(String(200), nullable=False)

    business_type = Column(String(100))

    gst_number = Column(String(50))

    pan_number = Column(String(50))

    email = Column(String(100))

    phone = Column(String(50))

    website = Column(String(100))

    address = Column(String(500))

    city = Column(String(100))

    state = Column(String(100))

    pincode = Column(String(20))

    country = Column(String(100))

    invoice_prefix = Column(String(50))

    financial_year = Column(String(50))

    currency = Column(String(20))

    tax_type = Column(String(50))

    logo_path = Column(String(500))

    created_at = Column(DateTime, default=datetime.utcnow)