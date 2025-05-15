from dataclasses import dataclass
from typing import List, Optional
from uuid import UUID

@dataclass
class CartItem:
    product_id: UUID
    quantity: int

@dataclass
class Cart:
    id: Optional[UUID]
    user_id: UUID
    items: List[CartItem]

    @classmethod
    def create(cls, user_id: UUID) -> 'Cart':
        return cls(
            id=None,
            user_id=user_id,
            items=[]
        ) 