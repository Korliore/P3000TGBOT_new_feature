from typing import Optional, Any
from envparse import env

env.read_envfile("../.env")


class Telegram:
    TOKEN = env("TOKEN")


class Database:
    DB_NAME = env("POSTGRES_DB")
    DB_USER = env("POSTGRES_USER")
    DB_PASSWORD = env("POSTGRES_PASSWORD")
    DB_HOST = env("POSTGRES_HOST")
    DB_PORT = env("POSTGRES_PORT")
    DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


databases = Database()