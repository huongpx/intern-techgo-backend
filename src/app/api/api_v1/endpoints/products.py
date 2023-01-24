from fastapi import APIRouter
from sqlalchemy import select

from ....db.session import LocalSession, engine
from .... import models, schemas

router = APIRouter()


@router.get("/", response_model=list[schemas.Product], summary="Lấy danh sách sản phẩm")
async def get_products(type: int = 0, limit: int = 10, offset: int = 0):
    """
    API lấy danh sách sản phẩm

    **params**

        * type: loại sản phẩm
            * type = 0 => điện thoại, default
            * type = 1 => laptop
            * type = 2 => máy tính bảng
            * type = 3 => phụ kiện khác (đồng hồ, tai nghe)
        * limit: mặc định = 10, dùng để giới hạn sản phẩm hiển thị trong 1 trang
        * offset: dùng để phân trang
    """
    with LocalSession as db:
        stmt = select(models.Product).filter_by(type == type)
        products = db.scalars(stmt).all()
        return products
