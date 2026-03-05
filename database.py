# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# import os
# from dotenv import load_dotenv

# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")

# if not DATABASE_URL:
#     raise ValueError("DATABASE_URL not set in .env file")

# print("🔗 Connecting to database...")

# # helper to build engine for a given URL

# def make_engine(url: str):
#     if "sqlite" in url:
#         return create_engine(url, connect_args={"check_same_thread": False})
#     return create_engine(
#         url,
#         pool_pre_ping=True,
#         pool_recycle=300,
#         connect_args={"sslmode": "require"} if "supabase" in url else {}
#     )

# # try the primary database, fallback to sqlite if it fails
# try:
#     engine = make_engine(DATABASE_URL)
#     # test connection immediately
#     with engine.connect() as conn:
#         pass
#     print("✅ Connected to primary database")
# except Exception as exc:
#     print(f"⚠️ Primary DB unavailable: {exc}")
#     print("   falling back to local SQLite database.")
#     DATABASE_URL = "sqlite:///./fallback.db"
#     engine = make_engine(DATABASE_URL)

# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )

# Base = declarative_base()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found in .env file")

print("🔗 Connecting to database...")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300,
    connect_args={"sslmode": "require"}
)

# Test connection
try:
    with engine.connect() as conn:
        print("✅ Connected to Supabase database")
except Exception as e:
    print("❌ Database connection failed:", e)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()