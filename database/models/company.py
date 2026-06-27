from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text,
)
from datetime import datetime

from database.base import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(
        Integer,
        primary_key=True,
    )

    company_name = Column(
        String(200),
        nullable=False,
    )

    business_type = Column(
        String(100)
    )

    gst_number = Column(
        String(50)
    )

    pan_number = Column(
        String(50)
    )

    email = Column(
        String(100)
    )

    phone = Column(
        String(50)
    )

    website = Column(
        String(100)
    )

    address = Column(
        String(500)
    )

    city = Column(
        String(100)
    )

    state = Column(
        String(100)
    )

    pincode = Column(
        String(20)
    )

    country = Column(
        String(100)
    )

    invoice_prefix = Column(
        String(50)
    )

    financial_year = Column(
        String(50)
    )

    currency = Column(
        String(20)
    )

    tax_type = Column(
        String(50)
    )

    # Branding

    logo_path = Column(
        String(500)
    )

    signature_path = Column(
        String(500)
    )

    # Banking

    bank_name = Column(
        String(200)
    )

    bank_account = Column(
        String(200)
    )

    ifsc_code = Column(
        String(100)
    )

    branch_name = Column(
        String(200)
    )

    upi_id = Column(
        String(200)
    )

    # Invoice Footer

    terms_conditions = Column(
        Text
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )