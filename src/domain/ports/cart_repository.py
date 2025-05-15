from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID
from ..models.cart import Cart, CartItem

class CartRepository(ABC):
    @abstractmethod
    def save(self, cart: Cart) -> Cart:
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: UUID) -> Optional[Cart]:
        pass

    @abstractmethod
    def add_item(self, user_id: UUID, item: CartItem) -> Cart:
        pass

    @abstractmethod
    def remove_item(self, user_id: UUID, product_id: UUID) -> Cart:
        pass

    @abstractmethod
    def clear(self, user_id: UUID) -> None:
        pass 