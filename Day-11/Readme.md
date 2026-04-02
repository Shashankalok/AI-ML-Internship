#  Flask API Basics Project

## Overview

This project demonstrates the basics of building REST APIs using Flask.
Each HTTP method is implemented in a **separate Python file** for clear understanding.

---

##  Concepts Covered

* Flask basics
* Routing
* REST API methods (GET, POST, PUT, DELETE)
* JSON handling
* API testing using Postman

---

## Project Structure

```
flask-api-basics/
│
├── hello.py          # Hello World Flask app
├── get.py            # Get all items
├── get_by_id.py      # Get item by ID
├── post.py           # Add new item
├── put.py            # Update item
├── delete.py         # Delete item
│
├── templates/        # HTML templates (for login example)
│   ├── index.html
│   └── login.html
│
├── requirements.txt
├── README.md
└── postman_collection.json
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/Shashankalok/AI-ML-Internship/tree/main-dev/Day-11
cd flask-api-basics
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ How to Run

Run any file individually:

```
python hello.py
python get.py
python post.py
python put.py
python delete.py
```

Server will start at:

```
http://127.0.0.1:5000
```

---

## 🔗 API Endpoints

###  1. Hello World

```
GET /
```

Returns:

```
Hello, World! This is my first Flask app.
```

---

###  2. Get All Items

```
GET /items
```

---

### 3. Get Item by ID

```
GET /items/<id>
```

---

### 4. Create Item

```
POST /items
```

Body:

```json
{
  "name": "Laptop"
}
```

---

### 5. Update Item

```
PUT /items/<id>
```

Body:

```json
{
  "name": "Updated Laptop"
}
```

---

###  6. Delete Item

```
DELETE /items/<id>
```

---

## Testing

All APIs are tested using Postman.

 Import:

```
postman_collection.json
```

---

## Important Notes

* Each file runs a separate Flask server
* Run only **one file at a time**
* Browser supports only GET → use Postman for POST, PUT, DELETE

---

## Learning Outcome

* Understood REST API structure
* Learned HTTP methods deeply
* Practiced real-world API testing

---

## Author

Shashank Alok

---

## Future Improvements

* Combine all endpoints into one app.py
* Add database (SQLite / MongoDB)
* Deploy API online

---
