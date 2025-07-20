# Products API - Django REST Framework

A lightweight and optimized Product Management API built with Django and DRF. Supports complete CRUD operations along with filtering, pagination, bulk deletion, and external product import.

---

## Features

* Create new products
* Retrieve a list of products with search and filters
* Retrieve product details
* Update product information
* Delete single or multiple products
* Bulk import products from external API
* Clean and consistent response structure

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Pratik-Github1/storeapi-mybizz.git
cd mybizzerp-storeapi
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the Database

You have two options to configure the database schema:

#### Option A: Use Django's ORM

```bash
python manage.py makemigrations
python manage.py migrate
```

Make sure your model `Meta` class includes:

```python
class Meta:
    db_table = 'products'
    managed = True
```

#### Option B: Use the Provided SQL Script

Use the SQL script from the `mysql/` folder with a MySQL client to create the `products` table manually.

Set `managed = False` in the model’s `Meta` class to prevent Django from managing the schema:

```python
class Meta:
    db_table = 'products'
    managed = False
```

---

### 4. Run the Development Server

```bash
python manage.py runserver
```

---

## API Authentication

Currently, all endpoints are open and do not require authentication. You can integrate Token or JWT authentication as needed.

---

## API Endpoints

### 1. Create a Product

* `POST /api/create-product`

```json
{
  "title": "Red T-Shirt",
  "description": "Premium cotton fabric",
  "price": 499,
  "category": "clothing",
  "rating_rate": 4.7,
  "rating_count": 320
}
```

---

### 2. List Products

* `GET /api/product-list`

Query Parameters:

| Parameter  | Type   | Description                    |
| ---------- | ------ | ------------------------------ |
| search     | string | Search by title                |
| category   | string | Filter by exact category match |
| min\_price | float  | Filter by minimum price        |
| max\_price | float  | Filter by maximum price        |
| page       | int    | Page number                    |
| limit      | int    | Results per page               |

---

### 3. Retrieve Product Details

* `GET /api/product-details?product_id=<id>`

---

### 4. Update Product

* `PUT /api/update-product?product_id=<id>`

---

### 5. Delete a Single Product

* `DELETE /api/delete-product?product_id=<id>`

---

### 6. Bulk Delete Products

* `DELETE /api/bulk-delete-products`

```json
{
  "product_ids": [1, 3, 5]
}
```

---

### 7. Import Products from External API

* `GET /api/import-products`

Fetches products from `https://fakestoreapi.com/products` and inserts them in bulk (skipping duplicates based on title).

Returns:

```json
{
  "message": "Bulk import completed.",
  "products_created": 12,
  "products_skipped": 8
}
```

---

## Tech Stack

* Python 3.13.3
* Django 5.2
* Django REST Framework 3.16.0

---

## Project Configuration Overview

This project uses a clean and modular `settings.py` structure designed for security, flexibility, and ease of deployment across environments.

### Environment Loading Flow

1. `.env` is loaded to detect the environment type (e.g., `stagging`, `production`)
2. Based on the `ENV_TYPE`, secrets are loaded from:

   * `.env.stagging.secrets`
   * `.env.production.secrets`

```python
load_dotenv(dotenv_path=BASE_DIR / ".env")
ENV_TYPE = os.getenv("ENV_TYPE", "stagging").lower()

SECRETS_FILE_MAP = {
    "stagging": ".env.stagging.secrets",
    "production": ".env.production.secrets"
}

secret_file = SECRETS_FILE_MAP.get(ENV_TYPE)
if secret_file:
    load_dotenv(dotenv_path=BASE_DIR / secret_file, override=True)
else:
    raise Exception(f"Unknown ENV_TYPE: {ENV_TYPE}")
```

### Core Configs from ENV

```python
DEBUG = os.getenv('DEBUG', default=True)
SECRET_KEY = os.getenv('SECRET_KEY')

if not SECRET_KEY:
    raise ValueError("SECRET_KEY not set in environment variables")
```

This ensures secrets and sensitive configs are never hard-coded, making the app production-ready and secure by default.

---

## Author

**Pratik Kumar Pradhan**
Connect on [LinkedIn](https://www.linkedin.com/in/mr-pratikk/)
