from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base


class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    id = Column(
        Integer,
        primary_key=True,
    )

    invoice_id = Column(
        Integer,
        ForeignKey(
            "invoices.id"
        ),
        nullable=False,
    )

    product_id = Column(
        Integer,
        ForeignKey(
            "products.id"
        ),
        nullable=False,
    )

    quantity = Column(
        Numeric(12, 2),
        default=0,
    )

    rate = Column(
        Numeric(12, 2),
        default=0,
    )

    discount = Column(
        Numeric(12, 2),
        default=0,
    )

    taxable_amount = Column(
        Numeric(12, 2),
        default=0,
    )

    gst_percentage = Column(
        Numeric(5, 2),
        default=0,
    )

    gst_amount = Column(
        Numeric(12, 2),
        default=0,
    )

    total = Column(
        Numeric(12, 2),
        default=0,
    )

    invoice = relationship(
        "Invoice",
        back_populates="items",
    )

    product = relationship(
        "Product"
    )