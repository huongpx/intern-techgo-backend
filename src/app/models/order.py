from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db.base_model import Base

if TYPE_CHECKING:
    from .account import Customer, Staff
    from .product import Product


class Order(Base):
    code: Mapped[str]
    type: Mapped[int]
    status: Mapped[int]
    customer_id = mapped_column(ForeignKey("customer.id"))
    staff_id = mapped_column(ForeignKey("staff.id"))
    total: Mapped[int]

    customer: Mapped[Customer] = relationship(back_populates="orders")
    staff: Mapped[Staff] = relationship(back_populates="orders")
    items: Mapped[list[Item]] = relationship(back_populates="order")


class Item(Base):
    order_id = mapped_column(ForeignKey("order.id"))
    product_id = mapped_column(ForeignKey("product.id"))
    quantity: Mapped[int]
    total: Mapped[int]

    order: Mapped[Order] = relationship(back_populates="items")
    product: Mapped[Product] = relationship()
