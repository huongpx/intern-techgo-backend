from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db.base_model import Base

if TYPE_CHECKING:
    from .order import Order


class PersonalInfoMixin:
    firstname: Mapped[str] = mapped_column(String(30))
    lastname: Mapped[str] = mapped_column(String(30))
    sex: Mapped[int] = mapped_column(Integer)
    email: Mapped[str] = mapped_column(String(100))
    phone_number: Mapped[str] = mapped_column(String(20))
    hashed_password: Mapped[str]


class Customer(PersonalInfoMixin, Base):
    orders: Mapped[Order] = relationship(back_populates="customer")


class Staff(PersonalInfoMixin, Base):
    role: Mapped[int]
    pay: Mapped[int]
    days_off: Mapped[int]
    worked_hours: Mapped[int]

    orders: Mapped[Order] = relationship(back_populates="staff")
