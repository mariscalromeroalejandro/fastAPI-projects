# FastAPI Users CRUD

A simple FastAPI application that provides CRUD operations for users using SQLAlchemy and SQLite.

![Pydantic](https://img.shields.io/badge/Pydantic-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-red)

## Features

- Create, read, update and delete users
- SQLite database with SQLAlchemy ORM
- Pydantic models for validation
- Automatic interactive docs with Swagger UI (/docs)

## Running the project

### 1. Install dependencies

```python
pip install -r requirements.txt
```

### 2. Start the server

```python
uvicorn main:app --reload
```

### 3. Open the API docs

Visit:
http://127.0.0.1:8000/docs

## Project Files

- main.py – FastAPI application and routes
- users.db – SQLite database (created automatically)
- requirements.txt – Dependencies
