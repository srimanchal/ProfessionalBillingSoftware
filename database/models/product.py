from sqlalchemy import Column, Integer, String, Numeric, DateTime, Text
from datetime import datetime
from database.base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)

    product_name = Column(String(200), nullable=False)
    sku = Column(String(100), unique=True)
    barcode = Column(String(100))
    category = Column(String(100))
    hsn_code = Column(String(50))

    purchase_price = Column(Numeric(12, 2), default=0)
    selling_price = Column(Numeric(12, 2), default=0)

    gst_percentage = Column(Numeric(5, 2), default=0)

    stock_quantity = Column(Numeric(12, 2), default=0)
    minimum_stock = Column(Numeric(12, 2), default=0)

    unit = Column(String(50))

    description = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)