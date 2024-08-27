# Inventory Management Service

This is a microservice for managing inventory in a coffee shop. It provides endpoints to fully manage inventory items in a coffee shop, including creating, updating, and deleting items.
## Features

- Manage inventory items within coffee shops.

## Technology Stack

- **FastAPI**: Web framework for building APIs.
- **PostgreSQL**: Relational database management system.
- **SQLAlchemy**: ORM for database interactions.
- **Alembic**: Database migrations.
- **Docker**: Containerization for development and deployment.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/abdullahsn10/inventory-management-service
   cd inventory-management-service
   ```

2. **Set up a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the environment variables:**

   Create a `.env` file in the project root and define the necessary environment variables:

   ```bash
    SQLALCHEMY_DATABASE_URL=postgresql://user:password@localhost:5432/inventory_service_db
    PUBLIC_KEY_PATH='path/to/public.pem'
    ALGORITHM = "RS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
   ```

## Environment Variables

Make sure to define the following environment variables in your `.env` file:

- `SQLALCHEMY_DATABASE_URL`: The URL for connecting to your PostgreSQL database.
- `PUBLIC_KEY_PATH`: The public key used for JWT decryption.
## Running the Application

To run the application locally:

```bash
python server.py
```

This will start the FastAPI application and serve it at `http://127.0.0.1:8000`.

## API Endpoints

### Users

- `GET /inventory-items/`: Get all inventory items.
- `POST /inventory-items/`: Create a new inventory item.
- `PUT /inventory-items/{inventory_item_id}`: Update an inventory item.
- `DELETE /inventory-items/{inventory_item_id}`: Delete an inventory item.


## Database Migrations

This project uses Alembic for database migrations. Follow these steps to manage migrations:

1. **Initialize Alembic** (if not already done):
   ```bash
   cd src
   alembic init migrations
   ```

   This will create an `migrations` directory with configuration files. But it is already done.

2. **Configure Alembic**:

   Edit the `alembic.ini` file and update the `sqlalchemy.url` variable with your database URL:

   ```ini
   sqlalchemy.url = postgresql://user:password@localhost:5432/coffee_shop_db
   ```

   Alternatively, you can set it in your `.env` file and configure Alembic to use it.

3. **Create a New Migration**:

   Whenever you make changes to your SQLAlchemy models, generate a new migration script:

   ```bash
   alembic revision --autogenerate -m "describe your changes"
   ```

4. **Apply Migrations**:

   To apply migrations and update the database schema, run:

   ```bash
   alembic upgrade head
   ```

5. **Downgrade Migrations**:

   If you need to revert a migration, use:

   ```bash
   alembic downgrade -1
   ```

