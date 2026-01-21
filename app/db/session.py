from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# For now, we use SQLite for local development
DATABASE_URL = "sqlite:///./dev.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # Needed for SQLite with FastAPI
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
