from __future__ import annotations

from fastapi import APIRouter

from .endpoints import accounts, login, orders, products

api_router = APIRouter()


api_router.include_router(products.router, prefix="/products", tags=["products"])
