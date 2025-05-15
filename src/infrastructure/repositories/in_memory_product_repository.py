from typing import List, Optional
from uuid import UUID, uuid4
from ...domain.models.product import Product
from ...domain.ports.product_repository import ProductRepository

class InMemoryProductRepository(ProductRepository):
    def __init__(self):
        self._products: dict[UUID, Product] = {}

    def save(self, product: Product) -> Product:
        if product.id is None:
            product.id = uuid4()
        self._products[product.id] = product
        return product

    def get_by_id(self, product_id: UUID) -> Optional[Product]:
        return self._products.get(product_id)

    def get_all(self) -> List[Product]:
        return list(self._products.values())

    def update(self, product: Product) -> Product:
        if product.id not in self._products:
            raise ValueError(f"Product with id {product.id} not found")
        self._products[product.id] = product
        return product

    def delete(self, product_id: UUID) -> None:
        if product_id not in self._products:
            raise ValueError(f"Product with id {product_id} not found")
        del self._products[product_id] 