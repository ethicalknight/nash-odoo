from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ✅ Define the base class for models
Base = declarative_base()

# ✅ Create database engine (SQLite by default)
engine = create_engine("sqlite:///skill_swap.db", echo=True)

# ✅ Session factory
SessionLocal = sessionmaker(bind=engine)

# ✅ Optional: for initializing DB
def init_db():
    Base.metadata.create_all(bind=engine)
