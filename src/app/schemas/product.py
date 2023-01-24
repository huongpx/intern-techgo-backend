from pydantic import BaseModel

# shared properties
class ProductBase(BaseModel):
    name: str
    description: str
    price: int


# for creating products
class ProductCreate(ProductBase):
    pass


# base properties stored in db
class ProductInDBBase(ProductBase):
    available: int


# properties return to client
class Product(ProductInDBBase):
    pass


# properties store in db
class ProductInDB(ProductInDBBase):
    type: int
