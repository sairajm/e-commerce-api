from typing import Optional
from uuid import UUID
from ...domain.models.cart import Cart, CartItem
from ...domain.ports.cart_repository import CartRepository
from ...domain.ports.product_repository import ProductRepository

class CartService:
    def __init__(self, cart_repository: CartRepository, product_repository: ProductRepository):
        self._cart_repository = cart_repository
        self._product_repository = product_repository

    def get_cart(self, user_id: UUID) -> Optional[Cart]:
        return self._cart_repository.get_by_user_id(user_id)

    def add_to_cart(self, user_id: UUID, product_id: UUID, quantity: int) -> Cart:
        product = self._product_repository.get_by_id(product_id)
        if product is None:
            raise ValueError(f"Product with id {product_id} not found")
        
        if product.stock < quantity:
            raise ValueError(f"Not enough stock for product {product_id}")
        
        item = CartItem(product_id=product_id, quantity=quantity)
        return self._cart_repository.add_item(user_id, item)

    def remove_from_cart(self, user_id: UUID, product_id: UUID) -> Cart:
        return self._cart_repository.remove_item(user_id, product_id)

    def clear_cart(self, user_id: UUID) -> None:
        self._cart_repository.clear(user_id) 