import os
from dotenv import load_dotenv


# load environment variables
load_dotenv()

# load database settings
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_SERVICE = os.getenv("DB_SERVICE")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# database url
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_SERVICE}/{POSTGRES_DB}"
)

# database settings
DATABASE_SETTINGS = {
    "URL": SQLALCHEMY_DATABASE_URL,
}

# security settings
PUBLIC_KEY = os.getenv("PUBLIC_KEY")


JWT_TOKEN_SETTINGS = {
    "PUBLIC_KEY": PUBLIC_KEY,
    "ALGORITHM": os.getenv("ALGORITHM"),
    "ACCESS_TOKEN_EXPIRE_MINUTES": os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"),
}

# docs settings
OPENAPI_URL = os.getenv("OPENAPI_URL")
ROOT_PATH = os.getenv("ROOT_PATH")
