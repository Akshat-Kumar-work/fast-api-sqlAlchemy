from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from os import getenv

# Load environment variables from the .env file
load_dotenv()

# Fetch database URL from the environment variable
DATABASE_URL = getenv("DB_URL")

# Ensure DATABASE_URL is not empty or None
if not DATABASE_URL:
    raise ValueError("DB_URL environment variable is not set or is empty")

# Create the SQLAlchemy engine using the database URL
engine = create_engine(DATABASE_URL, pool_pre_ping=True)  # Adding pool_pre_ping for connection health check

# Create a base class for declarative models
Base = declarative_base()

# Create a session factory bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the DB session (useful for frameworks like FastAPI)
def get_db():
    """
    Provides a database session. This function should be used in a context
    that properly manages the session lifecycle.
    """
    db = SessionLocal()  # Create a session
    try:
        yield db  # Yield the session to use in the app
    finally:
        db.close()  # Close the session after use

