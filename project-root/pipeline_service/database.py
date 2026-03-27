import os
from sqlalchemy import create_engine
import time

from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:password@postgres:5432/customer_db"
)


engine = None

for i in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        conn = engine.connect()
        conn.close()
        print("✅ Connected to DB")
        break
    except Exception as e:
        print("⏳ Waiting for DB...", e)
        time.sleep(3)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()