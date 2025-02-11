import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_FILE = "userbot_database.db"  # Local database file

def start() -> scoped_session:
    # SQLite database connection
    engine = create_engine(f"sqlite:///{DATABASE_FILE}")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


try:
    BASE = declarative_base()
    SESSION = start()
except Exception as e:
    print("Error configuring the database.")
    print(str(e))
