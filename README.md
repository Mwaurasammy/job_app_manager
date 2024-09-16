## 📝 Job Application Manager CLI
Overview
    The Job Application Manager CLI is a command-line application designed to help you efficiently manage your job applications. Applying to many jobs can get overwhelming, but with this system, you can easily track the companies you've applied to, the positions you're targeting, and the current status of each application (e.g., interview, callback, or rejected).

## Problem Statement
    Applying for multiple jobs can become difficult to track manually. You might lose track of which company called you back, which application led to an interview, or which ones were rejected. This CLI tool helps you organize and manage all your job applications by providing a simple and efficient way to add, update, list, and delete applications, all while staying organized.

## Key Features 🚀
    Add a job application: Record your job applications by entering company name and position.
    List job applications: View all your job applications and their current status.
    Update an application: Modify the status of a job application (e.g., callback, interview, or rejected).
    Delete an application: Remove job applications that you no longer want to track.
    Company auto-delete: When you delete an application, its associated company is also deleted automatically.

## Installation 🛠️
    Clone this repository to your local machine:

    **bash**
    git clone https://github.com/your-username/job_app_manager.git
    Navigate into the project directory:

    **bash**
    cd job-app-manager
    Set up the virtual environment using pipenv:

    **bash**
    pipenv install
    Activate the virtual environment:

    **bash**
    pipenv shell
    Run the database migrations to set up the database schema:

    **bash**
    alembic upgrade head

## Usage 💻
    Run the my_app.py script from the terminal to launch the CLI app:

    **bash**
    python my_app.py
    You'll see a menu like this:

    **plaintext**
    Welcome to the Job Application Tracker CLI!

    Main Menu:
    1. Add a job application
    2. List all job applications
    3. Update a job application
    4. Delete a job application
    5. Exit

    Please select an option (1-5):
    **Example Commands**
    Adding an application:

    Select option 1
    Input the company name and job position.
    Enter the company name: Microsoft
    Enter the job position: Software Engineer
    ---------------------------------------
    Added application for Software Engineer at Microsoft.
    Listing applications:

    Select option 2 to view all applications.
    ---------------------------------------
    ID: 1 | Company: Microsoft | Position: Software Engineer | Status: Pending
    ---------------------------------------
    Updating an application:

    Select option 3, enter the ID of the application, and the new status.
    Enter the application ID to update: 1
    Enter the new status (e.g., callback, interview, rejected): Interview
    ---------------------------------------
    Updated application 1 status to Interview.
    Deleting an application:

    Select option 4 and enter the ID of the application to delete.
    Enter the application ID to delete: 1
    ---------------------------------------
    Deleted application 1.

## Project Structure 📂
    job-app-tracker/
    │
    ├── app/
    │   ├── __init__.py
    │   ├── cli.py
    │   ├── crud.py
    │   ├── database.py
    │   └── models.py
    ├── alembic/
    │   └── versions/
    │       └── [migration files]
    ├── Pipfile
    ├── Pipfile.lock
    ├── alembic.ini
    └── my_app.py

## Contributing 🤝
    Contributions are welcome! Please fork this repository and submit a pull request with any improvements or bug fixes.


## Contact 💬
If you have any questions, feel free to reach out!

Email: mwaurasammy@gmail.com
GitHub: https://github.com/Mwaurasammy

Enjoy tracking your job applications with ease! 😄

