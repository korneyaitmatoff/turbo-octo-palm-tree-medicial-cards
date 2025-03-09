from os import getenv

from dotenv import load_dotenv

load_dotenv()

POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD")
POSTGRES_USER = getenv("POSTGRES_USER")
POSTGRES_DB = getenv("POSTGRES_DB")
POSTGRES_HOST = getenv("POSTGRES_HOST")
