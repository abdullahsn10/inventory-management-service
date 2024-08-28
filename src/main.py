from fastapi import FastAPI
from src.routers import inventory_item

app = FastAPI()

# register routes
app.include_router(inventory_item.router)
