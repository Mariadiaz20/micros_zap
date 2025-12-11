from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
# importa modelos para registrarlos en metadata
import app.models.models  # noqa: F401

DATABASE_URL = "sqlite:///./faszap.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# crea tablas
Base.metadata.create_all(bind=engine)

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()