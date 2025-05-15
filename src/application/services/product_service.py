from typing import List, Optional
from uuid import UUID
from ...domain.models.product import Product
from ...domain.ports.product_repository import ProductRepository

class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self._product_repository = product_repository

    def create_product(self, name: str, description: str, price: float, stock: int) -> Product:
        product = Product.create(name, description, price, stock)
        return self._product_repository.save(product)

    def get_product(self, product_id: UUID) -> Optional[Product]:
        return self._product_repository.get_by_id(product_id)

    def get_all_products(self) -> List[Product]:
        return self._product_repository.get_all()

    def update_product(self, product_id: UUID, name: str, description: str, price: float, stock: int) -> Product:
        product = self._product_repository.get_by_id(product_id)
        if product is None:
            raise ValueError(f"Product with id {product_id} not found")
        
        product.name = name
        product.description = description
        product.price = price
        product.stock = stock
        
        return self._product_repository.update(product)

    def delete_product(self, product_id: UUID) -> None:
        self._product_repository.delete(product_id) 