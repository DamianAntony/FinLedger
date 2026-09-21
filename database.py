from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "postgresql://postgres:damian33@localhost:5432/FinLedger"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False , autoflush =False , bind=engine)

Base = declarative_base() # blue print class for tables to inherit from

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    



