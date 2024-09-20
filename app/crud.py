# app/crud.py
from app.models import Company, JobApplication
from app.database import Session

def add_application(company_name, position):
    session = Session()
    company = session.query(Company).filter_by(name=company_name).first()
    if not company:
        company = Company(name=company_name)
        session.add(company)
    job_application = JobApplication(company=company, position=position)
    session.add(job_application)
    session.commit()
    session.close()

def list_applications():
    session = Session()
    applications = session.query(JobApplication).all()
    for app in applications:
        print(f"ID: {app.id}, Company: {app.company.name}, Position: {app.position}, Status: {app.status}")
    session.close()

def update_application(app_id, status):
    session = Session()
    job_application = session.query(JobApplication).filter_by(id=app_id).first()
    if job_application:
        job_application.status = status
        session.commit()
        print(f"Updated application ID {app_id} to status: {status}")
    else:
        print(f"Application ID {app_id} not found.")
    session.close()

def delete_application(app_id):
    session = Session()
    job_application = session.query(JobApplication).filter_by(id=app_id).first()
    
    if job_application:
        company = job_application.company
        session.delete(job_application)
        session.commit()

        # Check if the company has any other applications left
        remaining_applications = session.query(JobApplication).filter_by(company_id=company.id).count()
        if remaining_applications == 0:
            session.delete(company)
            session.commit()
            print(f"Deleted company {company.name} as well because it had no more job applications.")
        else:
            print(f"Deleted application ID {app_id}.")
    else:
        print(f"Application ID {app_id} not found.")

    session.close()

