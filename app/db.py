# app/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()  # read .env from project root

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./cafeteria.db")

# echo=True if you want SQL logging
engine = create_engine(DATABASE_URL, echo=False, future=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
