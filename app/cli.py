# cli.py
import click
from app.crud import add_application, list_applications, update_application, delete_application

@click.group()
def cli():
    """Job Application Management CLI"""
    pass

@cli.command()
@click.argument('company_name')
@click.argument('position')
def add(company_name, position):
    """Add a new job application."""
    add_application(company_name, position)
    click.echo(f"Added application for {position} at {company_name}.")

@cli.command()
def list():
    """List all job applications."""
    list_applications()

@cli.command()
@click.argument('app_id')
@click.argument('status')
def update(app_id, status):
    """Update the status of an application."""
    update_application(app_id, status)
    click.echo(f"Updated application {app_id} status to {status}.")

@cli.command()
@click.argument('app_id')
def delete(app_id):
    """Delete a job application."""
    delete_application(app_id)
    click.echo(f"Deleted application {app_id}.")

if __name__ == '__main__':
    cli()



































# import click
# from app.crud import add_application, list_applications, update_application, delete_application

# @click.group()
# def cli():
#     """Job Application Management CLI"""
#     pass

# @cli.command()
# @click.argument('company_name')
# @click.argument('position')
# def add(company_name, position):
#     """Add a new job application."""
#     add_application(company_name, position)
#     click.echo(f"Added application for {position} at {company_name}.")

# @cli.command()
# def list():
#     """List all job applications."""
#     list_applications()

# @cli.command()
# @click.argument('app_id')
# @click.argument('status')
# def update(app_id, status):
#     """Update the status of an application."""
#     update_application(app_id, status)
#     click.echo(f"Updated application {app_id} status to {status}.")

# @cli.command()
# @click.argument('app_id')
# def delete(app_id):
#     """Delete a job application."""
#     delete_application(app_id)
#     click.echo(f"Deleted application {app_id}.")

# if __name__ == '__main__':
#     cli()
