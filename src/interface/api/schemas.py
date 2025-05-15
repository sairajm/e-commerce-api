from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID
from enum import Enum

class OrderStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    stock: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: UUID

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: UUID

    class Config:
        orm_mode = True

class CartItemBase(BaseModel):
    product_id: UUID
    quantity: int

class CartItemCreate(CartItemBase):
    pass

class CartItem(CartItemBase):
    class Config:
        orm_mode = True

class OrderItemBase(BaseModel):
    product_id: UUID
    quantity: int
    price: float

class OrderItem(OrderItemBase):
    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    user_id: UUID
    items: List[OrderItem]
    total_amount: float
    status: OrderStatus

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: UUID

    class Config:
        orm_mode = True 