from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from uuid import UUID

from src.domain.models.order import OrderStatus as DomainOrderStatus
from src.application.services.product_service import ProductService
from src.application.services.user_service import UserService
from src.application.services.cart_service import CartService
from src.application.services.order_service import OrderService
from src.infrastructure.repositories.in_memory_product_repository import InMemoryProductRepository
from src.infrastructure.repositories.in_memory_user_repository import InMemoryUserRepository
from src.infrastructure.repositories.in_memory_cart_repository import InMemoryCartRepository
from src.infrastructure.repositories.in_memory_order_repository import InMemoryOrderRepository
from .schemas import (
    Product, ProductCreate,
    User, UserCreate,
    CartItem, CartItemCreate,
    Order, OrderCreate,
    OrderStatus
)

app = FastAPI(title="E-Commerce API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency injection
def get_product_service():
    return ProductService(InMemoryProductRepository())

def get_user_service():
    return UserService(InMemoryUserRepository())

def get_cart_service():
    return CartService(InMemoryCartRepository(), InMemoryProductRepository())

def get_order_service():
    return OrderService(
        InMemoryOrderRepository(),
        InMemoryCartRepository(),
        InMemoryProductRepository()
    )

# Product endpoints
@app.post("/products/", response_model=Product)
def create_product(
    product: ProductCreate,
    product_service: ProductService = Depends(get_product_service)
):
    try:
        return product_service.create_product(
            product.name,
            product.description,
            product.price,
            product.stock
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/products/", response_model=List[Product])
def get_products(product_service: ProductService = Depends(get_product_service)):
    return product_service.get_all_products()

@app.get("/products/{product_id}", response_model=Product)
def get_product(
    product_id: UUID,
    product_service: ProductService = Depends(get_product_service)
):
    product = product_service.get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put("/products/{product_id}", response_model=Product)
def update_product(
    product_id: UUID,
    product: ProductCreate,
    product_service: ProductService = Depends(get_product_service)
):
    try:
        return product_service.update_product(
            product_id,
            product.name,
            product.description,
            product.price,
            product.stock
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/products/{product_id}")
def delete_product(
    product_id: UUID,
    product_service: ProductService = Depends(get_product_service)
):
    try:
        product_service.delete_product(product_id)
        return {"message": "Product deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# User endpoints
@app.post("/users/", response_model=User)
def create_user(
    user: UserCreate,
    user_service: UserService = Depends(get_user_service)
):
    try:
        return user_service.create_user(
            user.username,
            user.email,
            user.password
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/users/{user_id}", response_model=User)
def get_user(
    user_id: UUID,
    user_service: UserService = Depends(get_user_service)
):
    user = user_service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Cart endpoints
@app.post("/carts/{user_id}/items")
def add_to_cart(
    user_id: UUID,
    item: CartItemCreate,
    cart_service: CartService = Depends(get_cart_service)
):
    try:
        cart_service.add_to_cart(user_id, item.product_id, item.quantity)
        return {"message": "Item added to cart successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/carts/{user_id}")
def get_cart(
    user_id: UUID,
    cart_service: CartService = Depends(get_cart_service)
):
    cart = cart_service.get_cart(user_id)
    if cart is None:
        return []
    return cart

@app.delete("/carts/{user_id}/items/{product_id}")
def remove_from_cart(
    user_id: UUID,
    product_id: UUID,
    cart_service: CartService = Depends(get_cart_service)
):
    try:
        cart_service.remove_from_cart(user_id, product_id)
        return {"message": "Item removed from cart successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# Order endpoints
@app.post("/orders/", response_model=Order)
def create_order(
    user_id: UUID,
    order_service: OrderService = Depends(get_order_service)
):
    try:
        return order_service.create_order(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/orders/{order_id}", response_model=Order)
def get_order(
    order_id: UUID,
    order_service: OrderService = Depends(get_order_service)
):
    order = order_service.get_order(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.get("/users/{user_id}/orders", response_model=List[Order])
def get_user_orders(
    user_id: UUID,
    order_service: OrderService = Depends(get_order_service)
):
    return order_service.get_user_orders(user_id)

@app.put("/orders/{order_id}/status")
def update_order_status(
    order_id: UUID,
    status: OrderStatus,
    order_service: OrderService = Depends(get_order_service)
):
    try:
        domain_status = DomainOrderStatus(status.value)
        order_service.update_order_status(order_id, domain_status)
        return {"message": "Order status updated successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) 