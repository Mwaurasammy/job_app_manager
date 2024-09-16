# # from sqlalchemy import create_engine
# # from sqlalchemy.ext.declarative import declarative_base
# # from sqlalchemy.orm import sessionmaker
# # from .cli import add_application, list_applications, update_application, delete_application


# # # Set up the SQLite database
# # engine = create_engine('sqlite:///job_applications.db')
# # Session = sessionmaker(bind=engine)
# # Base = declarative_base()

# # # Import the models and create the tables
# # from app.models import Company, JobApplication
# # Base.metadata.create_all(engine)


# # app/__init__.py
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from app.models import Base, Company, JobApplication

# engine = create_engine("sqlite:///job_applications.db")
# Session = sessionmaker(bind=engine)

# # If needed, you can initialize tables here
# Base.metadata.create_all(engine)
