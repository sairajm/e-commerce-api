from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from uuid import UUID
from enum import Enum
from datetime import datetime

class OrderStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class ProductBase(BaseModel):
    name: str
    description: str
    price: float = Field(gt=0)
    stock: int = Field(ge=0)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = Field(default=None, gt=0)
    stock: Optional[int] = Field(default=None, ge=0)

class Product(ProductBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(min_length=8)

class UserUpdate(BaseModel):
    username: Optional[str] = Field(default=None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(default=None, min_length=8)

class User(UserBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class CartItemBase(BaseModel):
    product_id: UUID
    quantity: int = Field(gt=0)

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    quantity: Optional[int] = Field(default=None, gt=0)

class CartItem(CartItemBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class OrderItemBase(BaseModel):
    product_id: UUID
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    user_id: UUID
    status: OrderStatus = OrderStatus.PENDING

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    status: Optional[OrderStatus] = None

class Order(OrderBase):
    id: UUID
    items: List[OrderItem]
    total_amount: float = Field(gt=0)
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 