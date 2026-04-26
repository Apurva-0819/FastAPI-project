 🚀 Smart Task Manager API (FastAPI)

A backend task management system built using FastAPI, featuring JWT Authentication, CRUD operations, and user-specific task handling.

📌 Features

-  User Registration & Login (JWT Authentication)
-  Create, Read, Update, Delete Tasks
- User-specific task management (Protected routes)
- FastAPI Dependency Injection
- Database integration using SQLAlchemy
- Background task support (email simulation)

🛠 Tech Stack

- Backend: FastAPI  
- Database: SQLite (via SQLAlchemy ORM)  
- Authentication: JWT (JSON Web Tokens)  
- Password Hashing: Passlib (bcrypt)  

📂 Project Structure

.
├── main.py        # Entry point (API routes)
├── auth.py        # Authentication (JWT, password hashing)
├── crud.py        # Database operations
├── models.py      # Database models
├── schemas.py     # Pydantic schemas
├── database.py    # DB connection

⚙️ Installation & Setup

1. Clone Repository
git clone https://github.com/your-username/smart-task-manager-api.git
cd smart-task-manager-api

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose

4. Run Server
uvicorn main:app --reload

 📬 API Endpoints

 Authentication
- POST /register → Register user
- POST /login → Login & get token

Tasks (Protected)
- POST /tasks → Create task
- GET /tasks → Get all tasks
- GET /tasks/{id} → Get single task
- PUT /tasks/{id} → Update task
- DELETE /tasks/{id} → Delete task

 🔑 Authentication

Use Bearer Token in header:
Authorization: Bearer <your_token>


