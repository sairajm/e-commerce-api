from dataclasses import dataclass
from typing import Optional
from uuid import UUID

@dataclass
class Product:
    id: Optional[UUID]
    name: str
    description: str
    price: float
    stock: int

    @classmethod
    def create(cls, name: str, description: str, price: float, stock: int) -> 'Product':
        return cls(
            id=None,
            name=name,
            description=description,
            price=price,
            stock=stock
        ) 