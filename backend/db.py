import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

DATABASE_URL = URL.create(
    "postgresql+psycopg",
    username="vigil",
    password=os.getenv("POSTGRES_PASSWORD"),
    host="localhost",
    port=5432,
    database="vigil",
)

engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass