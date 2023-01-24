import datetime

from sqlalchemy import func, DateTime
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, onupdate=func.now())
    deleted_at: Mapped[datetime.datetime] = mapped_column(DateTime)
