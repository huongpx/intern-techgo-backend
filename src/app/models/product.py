from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from ..db.base_model import Base


class Product(Base):
    type: Mapped[int]
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str]
    price: Mapped[int]
    available: Mapped[int]
