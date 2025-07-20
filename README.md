# storeapi-mybizz
A lightweight and optimized Product Management API built with Django and DRF. Includes full CRUD operations with filtering, pagination, and bulk deletion support.


````markdown
# 🛍️ Products API - Django REST Framework

A lightweight and optimized Product Management API built with Django and DRF. Includes full CRUD operations with filtering, pagination, and bulk deletion support.

---

## 📦 Features

- ✅ Create a new product
- 🔍 List products with powerful filtering and pagination
- 📄 Retrieve product details
- ✏️ Update product info
- ❌ Delete single or multiple products
- 📊 Clean response format with consistent structure

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/products-api.git
cd products-api
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the Server

```bash
python manage.py runserver
```

---

## 🔐 API Authentication

> Currently all endpoints are **open** (no auth). You can integrate Token or JWT auth as needed.

---

## 📘 API Endpoints & Usage

### 1. 📥 Create a Product

**URL:** `POST /api/products/create`

**Request:**

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

**Response:**

```json
{
  "status": true,
  "message": "Product created successfully.",
  "error": ""
}
```

---

### 2. 📃 List Products (with Filters)

**URL:** `GET /api/products/list`

**Query Parameters:**

| Param       | Type   | Description                      |
| ----------- | ------ | -------------------------------- |
| `search`    | string | Search by product title          |
| `category`  | string | Filter by category (exact match) |
| `min_price` | float  | Minimum price filter             |
| `max_price` | float  | Maximum price filter             |
| `page`      | int    | Page number                      |
| `limit`     | int    | Items per page                   |

**Example:**

```
GET /api/products/list?search=shirt&category=clothing&min_price=100&max_price=1000&page=1&limit=10
```

**Response:**

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
      "category": "clothing",
      ...
    }
  ]
}
```

---

### 3. 📄 Retrieve Product Details

**URL:** `GET /api/products/detail?product_id=<id>`

**Example:**
`GET /api/products/detail?product_id=3`

**Response:**

```json
{
  "status": true,
  "message": "Product details fetched successfully.",
  "data": {
    "id": 3,
    "title": "Red T-Shirt",
    ...
  }
}
```

---

### 4. ✏️ Update Product

**URL:** `PUT /api/products/update?product_id=<id>`

**Request Body:**

```json
{
  "price": 550,
  "title": "Red T-Shirt XL"
}
```

**Response:**

```json
{
  "status": true,
  "message": "Product updated successfully."
}
```

---

### 5. ❌ Delete a Single Product

**URL:** `DELETE /api/products/delete?product_id=<id>`

**Response:**

```json
{
  "status": true,
  "message": "Product deleted successfully."
}
```

---

### 6. ❌ Bulk Delete Products

**URL:** `DELETE /api/products/delete-bulk`

**Request Body:**

```json
{
  "product_ids": [1, 3, 5]
}
```

**Response:**

```json
{
  "status": true,
  "message": "3 product(s) deleted successfully."
}
```

---

## 🛠 Tech Stack

* Python 3.10+
* Django 4.x
* Django REST Framework

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Contribution

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 👤 Author

**Pratik Kumar Pradhan**
Feel free to connect on [LinkedIn](https://www.linkedin.com)

```

---

Let me know once your GitHub repo is ready, and I’ll help you tailor the repo name and license reference too.
```
