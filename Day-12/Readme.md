
# 📊 Day 12: SQL, PostgreSQL & Database Integration

---

## 🎯 Learning Objectives

* Understand **SQL fundamentals**
* Set up and manage a **PostgreSQL database**
* Integrate **Flask with PostgreSQL**
* Build a **real-world CRUD API**
* Implement **JWT Authentication for security**

---

## 📺 Recommended Learning Resources

### 🔍 YouTube Search Terms

* SQL tutorial for beginners
* PostgreSQL tutorial python
* SQL in 60 minutes
* Flask PostgreSQL integration
* psycopg2 tutorial

### 🎓 Recommended Channels

* Programming with Mosh
* Traversy Media
* Corey Schafer

---

## ⚙️ Setup & Installation

### 1️⃣ Install PostgreSQL

* Install locally OR use:

  * ElephantSQL (Free tier)
  * Supabase
  * Neon

---

### 2️⃣ Install Required Libraries

```bash
pip install psycopg2-binary sqlalchemy flask flask-sqlalchemy flask-jwt-extended
```

---

## 🧠 SQL Concepts Covered

### ✅ Basic Operations

* CREATE TABLE
* INSERT
* SELECT
* UPDATE
* DELETE

### ✅ Advanced Queries

* WHERE
* ORDER BY
* GROUP BY
* JOIN (INNER, LEFT, RIGHT)
* Aggregate Functions:

  * COUNT()
  * SUM()
  * AVG()

---

## 🧪 Practice Work

* Created **student/task database**
* Wrote **20+ SQL queries**
* Performed:

  * Filtering
  * Aggregation
  * Ranking
  * Subqueries

---

## 🔗 Flask + PostgreSQL Integration

* Connected Flask app with PostgreSQL using **SQLAlchemy**
* Configured database URI
* Created models (tables) using ORM

---

## 🚀 CRUD API Implementation

### 🔹 POST (Create)

* Add new record to database
* Input via JSON request

### 🔹 GET (Read)

* Retrieve all records
* Return data in JSON format

### 🔹 PUT (Update)

* Update existing record using ID

### 🔹 DELETE (Remove)

* Delete record from database

---

## 🔐 Bonus: JWT Authentication

* Implemented login system
* Generated access tokens
* Protected API routes using:

```python
@jwt_required()
```

---

## 📁 Project Structure

```
flask-sql-api/
│
├── app.py
├── requirements.txt
├── sql_queries.sql
└── README.md
```

---

## 🧾 Deliverables

* ✅ Flask API connected with PostgreSQL
* ✅ 20+ SQL queries file
* ✅ Working CRUD API
* ✅ JWT Authentication
* ✅ Postman Collection
* ✅ Database Schema

---

## 🧪 Sample API Flow

### 1️⃣ Login

```http
POST /login
```

### 2️⃣ Get Token → Use in Headers

```
Authorization: Bearer <token>
```

### 3️⃣ Perform CRUD

* GET /task
* POST /task
* PUT /task/{id}
* DELETE /task/{id}

---

## 📊 Results

* Successfully connected Flask with PostgreSQL
* CRUD operations executed without errors
* Data stored, retrieved, updated, and deleted dynamically
* Authentication secured endpoints

---

## 🧠 Key Learnings

* Difference between **SQL and ORM (SQLAlchemy)**
* Importance of **API structure in backend systems**
* Handling **HTTP methods (GET, POST, PUT, DELETE)**
* Debugging real-world errors (415, 404, DB errors)
* Understanding **client-server interaction**

---

## 🏁 Conclusion

This project demonstrates a **complete backend development workflow**, including:

* Database creation and management
* API development using Flask
* Integration with PostgreSQL
* Implementation of secure authentication

👉 This is a **job-ready backend project** that reflects real-world application development skills.

---

## 🚀 Next Steps

* Deploy the project (Render / Railway / AWS)
* Add frontend (React / HTML dashboard)
* Use environment variables for security
* Expand into microservices architecture

---

🔥 **Status: Completed & Production-Ready (Learning Level)**
