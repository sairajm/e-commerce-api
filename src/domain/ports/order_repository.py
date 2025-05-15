from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from ..models.order import Order, OrderStatus

class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order) -> Order:
        pass

    @abstractmethod
    def get_by_id(self, order_id: UUID) -> Optional[Order]:
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: UUID) -> List[Order]:
        pass

    @abstractmethod
    def update_status(self, order_id: UUID, status: OrderStatus) -> Order:
        pass 