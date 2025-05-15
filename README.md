# E-Commerce API

A FastAPI-based e-commerce API implementing hexagonal architecture principles.

## Features

- Product management (CRUD operations)
- User management
- Shopping cart functionality
- Order processing
- RESTful API endpoints
- Swagger UI documentation

## Project Structure

```
src/
├── application/          # Application layer (use cases)
│   └── services/        # Business logic services
├── domain/              # Domain layer (core business logic)
│   └── models/         # Domain models
├── infrastructure/      # Infrastructure layer
│   └── repositories/   # Data access implementations
└── interface/          # Interface layer
    └── api/           # API endpoints and schemas
```

## Prerequisites

- Python 3.12 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the server:
```bash
python run.py
```

The API will be available at:
- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Products
- `POST /products/` - Create a new product
- `GET /products/` - Get all products
- `GET /products/{product_id}` - Get a specific product
- `PUT /products/{product_id}` - Update a product
- `DELETE /products/{product_id}` - Delete a product

### Users
- `POST /users/` - Create a new user
- `GET /users/{user_id}` - Get a specific user

### Cart
- `POST /carts/{user_id}/items` - Add item to cart
- `GET /carts/{user_id}` - Get user's cart
- `DELETE /carts/{user_id}/items/{product_id}` - Remove item from cart

### Orders
- `POST /orders/` - Create a new order
- `GET /orders/{order_id}` - Get a specific order
- `GET /users/{user_id}/orders` - Get user's orders
- `PUT /orders/{order_id}/status` - Update order status

## Testing the API

You can test the API using the Swagger UI at http://localhost:8000/docs or using cURL commands:

1. Create a product:
```bash
curl -X POST "http://localhost:8000/products/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"name\": \"Test Product\", \"description\": \"A test product\", \"price\": 29.99, \"stock\": 100}"
```

2. Create a user:
```bash
curl -X POST "http://localhost:8000/users/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"username\": \"testuser\", \"email\": \"test@example.com\", \"password\": \"Str0ng!P@ssw0rd\"}"
```

## Architecture

This project follows hexagonal architecture (also known as ports and adapters) principles:

- **Domain Layer**: Contains the core business logic and models
- **Application Layer**: Implements use cases and orchestrates the domain layer
- **Infrastructure Layer**: Provides implementations for external interfaces
- **Interface Layer**: Handles HTTP requests and responses

## Dependencies

- FastAPI: Web framework
- Uvicorn: ASGI server
- Pydantic: Data validation

## License

MIT License 