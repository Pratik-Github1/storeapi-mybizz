Here is a **clean, professional, and emoji-free** version of your `README.md`:

---

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
git clone https://github.com/your-username/storeapi-mybizz.git
cd storeapi-mybizz
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

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

* **Endpoint:** `POST /api/products/create`
* **Request Body:**

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

* **Response:**

```json
{
  "status": true,
  "message": "Product created successfully.",
  "error": ""
}
```

---

### 2. List Products

* **Endpoint:** `GET /api/products/list`
* **Query Parameters:**

| Parameter  | Type   | Description                    |
| ---------- | ------ | ------------------------------ |
| search     | string | Search by title                |
| category   | string | Filter by exact category match |
| min\_price | float  | Filter by minimum price        |
| max\_price | float  | Filter by maximum price        |
| page       | int    | Page number                    |
| limit      | int    | Results per page               |

* **Example:**

```
GET /api/products/list?search=shirt&category=clothing&min_price=100&max_price=1000&page=1&limit=10
```

* **Response:**

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 3,
      "title": "Red T-Shirt",
      "price": 499,
      "category": "clothing"
    }
  ]
}
```

---

### 3. Retrieve Product Details

* **Endpoint:** `GET /api/products/detail?product_id=<id>`
* **Example:** `GET /api/products/detail?product_id=3`
* **Response:**

```json
{
  "status": true,
  "message": "Product details fetched successfully.",
  "data": {
    "id": 3,
    "title": "Red T-Shirt",
    "description": "Premium cotton fabric",
    "price": 499,
    "category": "clothing",
    "rating_rate": 4.7,
    "rating_count": 320
  }
}
```

---

### 4. Update Product

* **Endpoint:** `PUT /api/products/update?product_id=<id>`
* **Request Body:**

```json
{
  "price": 550,
  "title": "Red T-Shirt XL"
}
```

* **Response:**

```json
{
  "status": true,
  "message": "Product updated successfully."
}
```

---

### 5. Delete a Single Product

* **Endpoint:** `DELETE /api/products/delete?product_id=<id>`
* **Response:**

```json
{
  "status": true,
  "message": "Product deleted successfully."
}
```

---

### 6. Bulk Delete Products

* **Endpoint:** `DELETE /api/products/delete-bulk`
* **Request Body:**

```json
{
  "product_ids": [1, 3, 5]
}
```

* **Response:**

```json
{
  "status": true,
  "message": "3 product(s) deleted successfully."
}
```

---

## Tech Stack

* Python 3.10+
* Django 4.x
* Django REST Framework

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contributions

Pull requests are welcome. For any significant changes, please open an issue first to discuss your proposal.

---

## 👤 Author

**Pratik Kumar Pradhan**
Feel free to connect on [LinkedIn](https://www.linkedin.com)