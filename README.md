# 💳 Transaction Based Wallet Backend

A mini fintech wallet backend built using **FastAPI**, **SQLite**, and **JSON-based user storage** to understand how modern systems combine **SQL** and **NoSQL** databases.

This project demonstrates:

* Authentication using JWT
* User management using JSON documents
* Wallet and transaction management using SQLite
* ACID transactions
* Money transfers
* Service Layer Architecture
* Protected APIs
* REST API Design

---

# 🚀 Project Goal

Modern applications rarely store everything in one database.

Different types of data have different requirements.

### User Data

Usually flexible and document-like:

```json
{
  "id": "USR-123",
  "name": "Sarthak",
  "email": "sarthak@gmail.com",
  "preferences": {},
  "settings": {}
}
```

NoSQL systems are good for:

* User profiles
* Preferences
* Settings
* Metadata
* Dynamic schemas

---

### Transaction Data

Money requires:

* Consistency
* Atomicity
* Integrity
* Audit trails

SQL databases are good for:

* Wallets
* Transactions
* Payments
* Banking records
* Financial systems

This project intentionally uses:

* JSON → User information (NoSQL thinking)
* SQLite → Wallets & Transactions (SQL thinking)

to understand how real-world systems separate concerns.

---

# 🏗️ Architecture

```text
Client
   │
   ▼
FastAPI Backend
   │
   ├── Authentication Service
   │
   ├── User Service
   │      └── users.json
   │
   ├── Wallet Service
   │      └── SQLite
   │
   └── Transaction Service
          └── SQLite
```

---

# 📁 Project Structure

```text
transaction_based/
│
├── app.py
│
├── api/
│   └── routes.py
│
├── database/
│   ├── db.py
│   └── wallet.db
│
├── users/
│   ├── users.json
│   └── auth.py
│
├── schemas/
│   ├── user_schema.py
│   ├── wallet_schema.py
│   └── transaction_schema.py
│
├── services/
│   ├── user_service.py
│   ├── wallet_service.py
│   └── transaction_service.py
│
├── utils/
│   ├── generators.py
│   ├── hashing.py
│   └── jwt_handler.py
│
└── frontend/
    └── index.html
```

---

# 🛠️ Tech Stack

## Backend

* FastAPI
* Uvicorn
* SQLite
* JWT Authentication
* Pydantic
* Passlib (bcrypt)

## Frontend

* HTML
* Tailwind CSS
* JavaScript Fetch API

---

# 📦 Installation

## Clone Repository

```bash
git clone <repository-url>
cd transaction_based
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux/Mac

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install fastapi
pip install uvicorn
pip install python-jose
pip install passlib[bcrypt]
pip install pydantic
pip install email-validator
pip install tabulate
```

or

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
uv run uvicorn app:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# 🗄️ Database Design

## users.json

Stores user information.

Example:

```json
{
  "users": [
    {
      "id": "USR-a13f91cd",
      "name": "Sarthak",
      "email": "sarthak@gmail.com",
      "password": "$2b$12$...",
      "wallet_id": "WAL-8f92a7d1"
    }
  ]
}
```

---

## wallets

Stores current wallet balances.

| wallet_id | user_id | balance |
| --------- | ------- | ------- |
| WAL-123   | USR-123 | 1000    |

---

## transactions

Stores immutable financial history.

| transaction_id | sender_wallet | receiver_wallet | amount | transaction_type | status  |
| -------------- | ------------- | --------------- | ------ | ---------------- | ------- |
| TXN-001        | NULL          | WAL-123         | 1000   | DEPOSIT          | SUCCESS |

---

# 🔐 Authentication Flow

```text
Register
    │
    ▼
Create User
    │
    ▼
Hash Password
    │
    ▼
Create Wallet
    │
    ▼
Store User
```

---

```text
Login
    │
    ▼
Validate Credentials
    │
    ▼
Generate JWT
    │
    ▼
Return Access Token
```

---

```text
Protected Route
    │
    ▼
Bearer Token
    │
    ▼
Verify JWT
    │
    ▼
Access Resource
```

---

# 💰 Wallet Flow

## Deposit

```text
BEGIN
    │
    ▼
Update Balance
    │
    ▼
Insert Transaction
    │
    ▼
COMMIT
```

---

## Withdraw

```text
BEGIN
    │
    ▼
Check Balance
    │
    ▼
Deduct Amount
    │
    ▼
Insert Transaction
    │
    ▼
COMMIT
```

---

## Transfer

```text
BEGIN
    │
    ▼
Validate Sender
    │
    ▼
Validate Receiver
    │
    ▼
Deduct Sender
    │
    ▼
Credit Receiver
    │
    ▼
Insert Transaction
    │
    ▼
COMMIT
```

If any step fails:

```text
ROLLBACK
```

No money is lost.

---

# 🔄 ACID Transactions

This project demonstrates:

### Atomicity

Either all operations succeed or none do.

### Consistency

Wallet balances always remain valid.

### Isolation

Concurrent operations do not corrupt data.

### Durability

Committed transactions persist.

---

# 📡 API Endpoints

## Authentication

### Register

```http
POST /register
```

```json
{
  "name": "Sarthak",
  "email": "sarthak@gmail.com",
  "password": "admin123"
}
```

---

### Login

```http
POST /login
```

```json
{
  "email": "sarthak@gmail.com",
  "password": "admin123"
}
```

---

## Profile

```http
GET /profile
Authorization: Bearer <token>
```

---

## Wallet

```http
GET /wallet
Authorization: Bearer <token>
```

---

## Deposit

```http
POST /deposit
Authorization: Bearer <token>
```

```json
{
  "amount": 1000
}
```

---

## Withdraw

```http
POST /withdraw
Authorization: Bearer <token>
```

```json
{
  "amount": 300
}
```

---

## Transfer

```http
POST /transfer
Authorization: Bearer <token>
```

```json
{
  "receiver_wallet_id": "WAL-12345",
  "amount": 300
}
```

---

## Transaction History

```http
GET /transactions
Authorization: Bearer <token>
```

---

# 🎯 Learning Outcomes

By building this project, you will understand:

* FastAPI Fundamentals
* REST API Design
* JWT Authentication
* Password Hashing
* SQL vs NoSQL Trade-offs
* Service Layer Architecture
* SQLite Transactions
* ACID Properties
* Protected Routes
* Transaction History
* Wallet Systems
* Payment Workflows
* Money Transfer Logic
* Error Handling
* Backend Project Structure

---

# 🔮 Future Improvements

Possible production upgrades:

* PostgreSQL
* SQLAlchemy ORM
* Redis Caching
* Refresh Tokens
* Audit Logging
* Idempotency Keys
* Background Workers
* Message Queues
* Docker
* Kubernetes
* Microservices
* Rate Limiting
* Email Verification
* Two-Factor Authentication
* CI/CD Pipelines

---

# 📚 Educational Purpose

This project was built as a learning-oriented fintech backend to understand:

* How modern systems combine SQL and NoSQL databases.
* Why financial data requires ACID transactions.
* How authentication and authorization work.
* How digital wallets and payment systems maintain consistency.
* How backend services are structured in production systems.

---

# ⭐ Key Takeaway

**Users are documents. Money is a ledger.**

User information benefits from flexible storage, while financial operations demand strong consistency and transactional guarantees.

This project demonstrates both approaches within a single backend application.
