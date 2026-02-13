from sqlalchemy import (create_engine,
                        text)
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL =  (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


engine = create_engine(DATABASE_URL, echo=True)

#part ==== Testing Connection ====
# with engine.connect() as conn:
#     result = conn.execute(text("SELECT 1"))
#     print(result.scalar())