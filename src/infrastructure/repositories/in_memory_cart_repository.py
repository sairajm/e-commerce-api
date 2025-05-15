from typing import Optional
from uuid import UUID, uuid4
from ...domain.models.cart import Cart, CartItem
from ...domain.ports.cart_repository import CartRepository

class InMemoryCartRepository(CartRepository):
    def __init__(self):
        self._carts: dict[UUID, Cart] = {}

    def save(self, cart: Cart) -> Cart:
        if cart.id is None:
            cart.id = uuid4()
        self._carts[cart.id] = cart
        return cart

    def get_by_user_id(self, user_id: UUID) -> Optional[Cart]:
        for cart in self._carts.values():
            if cart.user_id == user_id:
                return cart
        return None

    def add_item(self, user_id: UUID, item: CartItem) -> Cart:
        cart = self.get_by_user_id(user_id)
        if cart is None:
            cart = Cart.create(user_id)
            cart = self.save(cart)

        # Check if product already in cart
        for cart_item in cart.items:
            if cart_item.product_id == item.product_id:
                cart_item.quantity += item.quantity
                return cart

        cart.items.append(item)
        return cart

    def remove_item(self, user_id: UUID, product_id: UUID) -> Cart:
        cart = self.get_by_user_id(user_id)
        if cart is None:
            raise ValueError(f"Cart for user {user_id} not found")

        cart.items = [item for item in cart.items if item.product_id != product_id]
        return cart

    def clear(self, user_id: UUID) -> None:
        cart = self.get_by_user_id(user_id)
        if cart is not None:
            del self._carts[cart.id] 