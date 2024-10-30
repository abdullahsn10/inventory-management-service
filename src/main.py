from fastapi import FastAPI
from src.routers import inventory_item
from src.settings.settings import OPENAPI_URL, ROOT_PATH

app = FastAPI(
    openapi_url=OPENAPI_URL,
    root_path=ROOT_PATH,
)

# register routes
app.include_router(inventory_item.router)
