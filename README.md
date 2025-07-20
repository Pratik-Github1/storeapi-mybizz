# Products API - Django REST Framework

A lightweight and optimized Product Management API built with Django and DRF. Supports complete CRUD operations along with filtering, pagination, and bulk deletion features.

---

## Features

* Create new products  
* Retrieve a list of products with search and filters  
* Retrieve product details  
* Update product information  
* Delete single or multiple products  
* Clean and consistent response structure

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Pratik-Github1/storeapi-mybizz.git
cd mybizzerp-storeapi
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the Database

You have two options to configure the database schema:

#### Option A: Use Django's ORM

Run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

Make sure your model `Meta` class includes:

```python
class Meta:
    db_table = 'products'
    managed = True  # Enable this when using Django migrations
```

#### Option B: Use the Provided SQL Script

If you prefer not to run Django migrations, execute the SQL script available inside the `mysql/` folder using any MySQL client (e.g., MySQL CLI or phpMyAdmin).
This will manually create the required `products` table in your database.

> **Important:** When using this method, set `managed = False` in your model’s `Meta` class to prevent Django from trying to manage the table schema.

---

### 4. Run the Development Server

```bash
python manage.py runserver
```

---

## API Authentication

All endpoints are currently open and do not require authentication. You can integrate Token or JWT authentication as needed.

---

## API Endpoints

### 1. Create a Product

* **Endpoint:** `POST /api/create-product`

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

* **Endpoint:** `GET /api/product-list`

**Query Parameters:**

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

* **Endpoint:** `GET /api/product-details?product_id=<id>`

---

### 4. Update Product

* **Endpoint:** `PUT /api/update-product?product_id=<id>`

---

### 5. Delete a Single Product

* **Endpoint:** `DELETE /api/delete-product?product_id=<id>`

---

### 6. Bulk Delete Products

* **Endpoint:** `DELETE /api/bulk-delete-products`

```json
{
  "product_ids": [1, 3, 5]
}
```

---

## Tech Stack

* Python 3.13.3
* Django 5.2x
* Django REST Framework \[ djangorestframework 3.16.0]

---

## 🔧 Project Configuration Overview

This project uses a clean and modular `settings.py` structure designed for security, flexibility, and ease of deployment across environments.

### 🔹 Environment Loading Flow

1. `.env` is first loaded to detect the environment type (e.g., `stagging`, `production`).
2. Based on the `ENV_TYPE`, the corresponding secrets file is loaded from:

   * `.env.stagging.secrets`
   * `.env.production.secrets`

```python
# Example flow from settings.py
BASE_DIR = Path(__file__).resolve().parent.parent

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

### 🔹 Core Configs from ENV

* `DEBUG` and `SECRET_KEY` values are loaded securely:

```python
DEBUG = os.getenv('DEBUG', default=True)
SECRET_KEY = os.getenv('SECRET_KEY')
```

* If `SECRET_KEY` is not defined, it raises an exception for safety:

```python
if not SECRET_KEY:
    raise ValueError("SECRET_KEY not set in environment variables")
```

This ensures secrets and sensitive configs are **never hard-coded**, making the app production-ready and secure by default.

---

## Author

**Pratik Kumar Pradhan**
Feel free to connect on [LinkedIn](https://www.linkedin.com/in/mr-pratikk/)
