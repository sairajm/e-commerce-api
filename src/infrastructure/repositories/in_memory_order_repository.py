from typing import List, Optional
from uuid import UUID, uuid4
from ...domain.models.order import Order, OrderStatus
from ...domain.ports.order_repository import OrderRepository

class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self._orders: dict[UUID, Order] = {}

    def save(self, order: Order) -> Order:
        if order.id is None:
            order.id = uuid4()
        self._orders[order.id] = order
        return order

    def get_by_id(self, order_id: UUID) -> Optional[Order]:
        return self._orders.get(order_id)

    def get_by_user_id(self, user_id: UUID) -> List[Order]:
        return [order for order in self._orders.values() if order.user_id == user_id]

    def update_status(self, order_id: UUID, status: OrderStatus) -> Order:
        if order_id not in self._orders:
            raise ValueError(f"Order with id {order_id} not found")
        order = self._orders[order_id]
        order.status = status
        return order 