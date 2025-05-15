from typing import List, Optional
from uuid import UUID
from ...domain.models.order import Order, OrderItem, OrderStatus
from ...domain.ports.order_repository import OrderRepository
from ...domain.ports.cart_repository import CartRepository
from ...domain.ports.product_repository import ProductRepository

class OrderService:
    def __init__(
        self,
        order_repository: OrderRepository,
        cart_repository: CartRepository,
        product_repository: ProductRepository
    ):
        self._order_repository = order_repository
        self._cart_repository = cart_repository
        self._product_repository = product_repository

    def create_order(self, user_id: UUID) -> Order:
        cart = self._cart_repository.get_by_user_id(user_id)
        if cart is None or not cart.items:
            raise ValueError("Cart is empty")

        # Convert cart items to order items and calculate total
        order_items = []
        total_amount = 0

        for cart_item in cart.items:
            product = self._product_repository.get_by_id(cart_item.product_id)
            if product is None:
                raise ValueError(f"Product with id {cart_item.product_id} not found")
            
            if product.stock < cart_item.quantity:
                raise ValueError(f"Not enough stock for product {cart_item.product_id}")
            
            # Update product stock
            product.stock -= cart_item.quantity
            self._product_repository.update(product)
            
            # Create order item
            order_item = OrderItem(
                product_id=cart_item.product_id,
                quantity=cart_item.quantity,
                price=product.price
            )
            order_items.append(order_item)
            total_amount += product.price * cart_item.quantity

        # Create and save order
        order = Order.create(user_id, order_items, total_amount)
        order = self._order_repository.save(order)

        # Clear the cart
        self._cart_repository.clear(user_id)

        return order

    def get_order(self, order_id: UUID) -> Optional[Order]:
        return self._order_repository.get_by_id(order_id)

    def get_user_orders(self, user_id: UUID) -> List[Order]:
        return self._order_repository.get_by_user_id(user_id)

    def update_order_status(self, order_id: UUID, status: OrderStatus) -> Order:
        return self._order_repository.update_status(order_id, status) 