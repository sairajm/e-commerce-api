from dataclasses import dataclass
from typing import List, Optional
from uuid import UUID
from enum import Enum

class OrderStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

@dataclass
class OrderItem:
    product_id: UUID
    quantity: int
    price: float

@dataclass
class Order:
    id: Optional[UUID]
    user_id: UUID
    items: List[OrderItem]
    total_amount: float
    status: OrderStatus

    @classmethod
    def create(cls, user_id: UUID, items: List[OrderItem], total_amount: float) -> 'Order':
        return cls(
            id=None,
            user_id=user_id,
            items=items,
            total_amount=total_amount,
            status=OrderStatus.PENDING
        ) 