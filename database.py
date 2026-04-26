from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ------------------ DATABASE URL ------------------
# SQLite for local testing; in production, replace with PostgreSQL/MySQL
SQLALCHEMY_DATABASE_URL = "sqlite:///./tasks.db"

# ------------------ ENGINE ------------------
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Required for SQLite
)

# ------------------ SESSION ------------------
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ------------------ BASE CLASS ------------------
Base = declarative_base()

# ------------------ DEPENDENCY ------------------
def get_db():
    """
    FastAPI dependency to get a database session.
    Ensures session is closed after request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()