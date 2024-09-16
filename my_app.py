# my_app.py

from app.crud import add_application, list_applications, update_application, delete_application

def print_separator():
    """Print a horizontal line separator."""
    print("-" * 50)

def main_menu():
    print_separator()
    print("Welcome to the Job Application Manager CLI!")
    print_separator()
    while True:
        print("Main Menu:")
        print("1. Add a job application")
        print("2. List all job applications")
        print("3. Update a job application")
        print("4. Delete a job application")
        print("5. Exit")

        choice = input("Please select an option (1-5): ")

        # Separator for better UX
        print_separator()

        if choice == '1':
            add_application_menu()
        elif choice == '2':
            list_application_menu()
        elif choice == '3':
            update_application_menu()
        elif choice == '4':
            delete_application_menu()
        elif choice == '5':
            print("Goodbye!")
            print_separator()
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 5.")
            
        print_separator()

def add_application_menu():
    company_name = input("Enter the company name: ").strip()
    position = input("Enter the job position: ").strip()

    # Separator for better UX
    print_separator()

    # Validate that neither company_name nor position is blank
    if not company_name or not position:
        print("Company name and position cannot be empty.")
        return

    add_application(company_name, position)
    print(f"Application for {position} at {company_name} added successfully.")

def list_application_menu():
    print("Listing all job applications:")
    
    # Separator for better UX
    print_separator()
    
    list_applications()

def update_application_menu():
    app_id = input("Enter the application ID to update: ").strip()
    status = input("Enter the new status (e.g., 'applied', 'interview', etc.): ").strip()

    # Separator for better UX
    print_separator()

    # Validate that neither app_id nor status is blank
    if not app_id or not status:
        print("Application ID and status cannot be empty.")
        return

    update_application(app_id, status)

def delete_application_menu():
    app_id = input("Enter the application ID to delete: ").strip()

    # Separator for better UX
    print_separator()

    # Validate that app_id is not blank
    if not app_id:
        print("Application ID cannot be empty.")
        return

    delete_application(app_id)

if __name__ == '__main__':
    main_menu()

























# #!/usr/bin/env python3
# import subprocess

# def main():
#     print("Welcome to the Job Application Tracker CLI!")
#     while True:
#         print("\nMain Menu:")
#         print("1. Add a job application")
#         print("2. List all job applications")
#         print("3. Update a job application")
#         print("4. Delete a job application")
#         print("5. Exit")

#         choice = input("\nPlease select an option (1-5): ")

#         if choice == "1":
#             company_name = input("Enter the company name: ")
#             position = input("Enter the job position: ")
#             subprocess.run(["python", "app/cli.py", "add", company_name, position])
#         elif choice == "2":
#             subprocess.run(["python", "app/cli.py", "list"])
#         elif choice == "3":
#             app_id = input("Enter the application ID to update: ")
#             status = input("Enter the new status: ")
#             subprocess.run(["python", "app/cli.py", "update", app_id, status])
#         elif choice == "4":
#             app_id = input("Enter the application ID to delete: ")
#             subprocess.run(["python", "app/cli.py", "delete", app_id])
#         elif choice == "5":
#             print("Exiting the application. Goodbye!")
#             break
#         else:
#             print("Invalid choice, please try again.")

# if __name__ == "__main__":
#     main()
