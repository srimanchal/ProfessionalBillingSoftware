from sqlalchemy import Column, Integer, String
from database.base import Base


class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True)

    vendor_name = Column(String(200))
    phone = Column(String(50))
    email = Column(String(100))
    address = Column(String(500))
    gst_number = Column(String(50))