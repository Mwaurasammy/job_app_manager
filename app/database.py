# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

# Create the database engine
engine = create_engine("sqlite:///job_applications.db")

# Session factory
Session = sessionmaker(bind=engine)

# Create all tables
Base.metadata.create_all(engine)
