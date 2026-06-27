from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from datetime import datetime
from database.base import Base


class StockMovement(Base):
    __tablename__ = "stock_movements"

    id = Column(Integer, primary_key=True)

    product_id = Column(Integer, ForeignKey("products.id"))

    movement_type = Column(String(50))

    quantity = Column(Numeric(12, 2))

    reference = Column(String(200))

    created_at = Column(DateTime, default=datetime.utcnow)