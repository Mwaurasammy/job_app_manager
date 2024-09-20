# app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    job_applications = relationship('JobApplication', back_populates='company', cascade="all, delete-orphan") # cascade deletes the company if a job application is deleted as well


class JobApplication(Base):
    __tablename__ = 'job_applications'

    id = Column(Integer, primary_key=True)
    position = Column(String)
    status = Column(String, default="applied")

    company_id = Column(Integer, ForeignKey('companies.id'))
    company = relationship('Company', back_populates='job_applications')

