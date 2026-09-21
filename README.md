# FinLedger

FinLedger is a personal finance management project designed to help users track transactions, monitor balances, and manage financial records in a structured way. The project is built as a Python backend using FastAPI, SQLAlchemy, and PostgreSQL, with a clean folder structure that supports future expansion for categories, budgets, reports, and user accounts.

## Overview

This repository currently includes the foundational database configuration and ORM setup for a financial application. It is structured to support:

- tracking income and expenses
- storing transactions in a relational database
- defining reusable models and schemas
- extending the app with API endpoints and business logic
- scaling into a more complete finance dashboard over time

## Tech Stack

- Python 3.11+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn

## Project Structure

```text
FinLedger/
├── database.py          # database connection and session setup
├── models.py            # SQLAlchemy database models
├── schemas.py           # Pydantic request/response schemas
├── main.py              # FastAPI application entry point
├── requirements.txt     # Python dependencies
├── README.md            # project documentation
└── .env.example         # optional environment template (add if needed)
```

## Current Implementation Status

The repository is in its early stage and includes the database bootstrap configuration:

- PostgreSQL connection string is configured in `database.py`
- SQLAlchemy `SessionLocal` and `Base` are initialized
- `get_db()` provides dependency injection for database sessions
- `main.py`, `models.py`, and `schemas.py` are ready for the application logic and API development

## Prerequisites

Before running the project, make sure you have:

- Python 3.11 or newer installed
- PostgreSQL installed and running locally
- a database named `FinLedger` created in PostgreSQL
- access to a PostgreSQL user with permission to the database

## Setup

1. Clone the repository

```bash
git clone <repository-url>
cd FinLedger
```

2. Create and activate a virtual environment

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Configure the database

The current connection string in `database.py` is:

```python
DATABASE_URL = "postgresql://postgres:damian33@localhost:5432/FinLedger"
```

Update it if your local PostgreSQL credentials or database name differ.

5. Run the app

Once the FastAPI app is implemented in `main.py`, start the server with:

```bash
uvicorn main:app --reload
```

Then open:

```text
http://127.0.0.1:8000
```

## Recommended Next Steps

To turn this scaffold into a complete finance app, the next milestones are:

1. define transaction, category, and user models in `models.py`
2. create request/response schemas in `schemas.py`
3. build FastAPI routes in `main.py`
4. add endpoints for:
   - create transaction
   - list transactions
   - update transaction
   - delete transaction
   - summary by category
   - monthly balance report
5. add authentication and authorization for multi-user access
6. add validation, tests, and a front-end dashboard

## Example Database Model Concept

A typical transaction model might include:

- id
- title
- description
- amount
- type (income or expense)
- category
- created_at
- user_id

## Notes

This project is a strong starting point for a personal finance backend, and the structure is designed to be simple, scalable, and easy to extend. As the project evolves, the database schema, API routes, and validation layer can be expanded to support richer financial tracking features.

## License

This project currently does not include a license file. If you plan to share or distribute it publicly, add an appropriate open-source license such as MIT or Apache 2.0.


