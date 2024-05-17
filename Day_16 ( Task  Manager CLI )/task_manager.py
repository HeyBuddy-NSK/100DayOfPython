import click
import pickle
import os

# Path to the tasks file
TASKS_FILE = 'tasks.pkl'

# creating class for tasks
class TaskManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    # Function to load a task
    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'rb') as file:
                return pickle.load(file)
        return []

    # function to save a task
    def save_tasks(self):
        with open(self.file_path, 'wb') as file:
            pickle.dump(self.tasks, file)

    # function to add a task
    def add_task(self, task):
        task_id = len(self.tasks) + 1
        self.tasks.append({'id': task_id, 'task': task, 'completed': False})
        self.save_tasks()

    # Function to list a task
    def list_tasks(self):
        for task in self.tasks:
            status = '✓' if task['completed'] else '✗'
            click.echo(f"{task['id']}. {task['task']}  [{status}]")

    # function to add flag if task is completed
    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                click.echo(f"Task {task_id} marked as complete.")
                return
        click.echo(f"Task {task_id} not found.")

    # function to delete a task
    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        self.save_tasks()
        if task_id in self.tasks:
            click.echo(f"Task {task_id} deleted.")
        else:
            click.echo("Task not present in list.")

    # function to search a task
    def search_tasks(self, keyword):
        results = [task for task in self.tasks if keyword.lower() in task['task'].lower()]
        for task in results:
            status = '✓' if task['completed'] else '✗'
            click.echo(f"{task['id']}. {task['task']} [{status}]")

# creating object for class
task_manager = TaskManager(TASKS_FILE)

# Creating commands group
@click.group()
def cli_group():
    pass

# command for add
@click.command()
def add():
    task = click.prompt('Please enter the task')
    task_manager.add_task(task)
    click.echo(f'Task added:)')

# Command for listing tasks
@click.command()
def list():
    task_manager.list_tasks()

# command for complete task
@click.command()
def complete():
    task_id = click.prompt('Please enter the task ID to mark as complete', type=int)
    task_manager.complete_task(task_id)

# command for deleting task
@click.command()
def delete():
    task_id = click.prompt('Please enter the task ID to delete', type=int)
    task_manager.delete_task(task_id)

# command for searching task
@click.command()
def search():
    keyword = click.prompt('Please enter the keyword to search for')
    task_manager.search_tasks(keyword)

# adding all commands to group
cli_group.add_command(add)
cli_group.add_command(list)
cli_group.add_command(complete)
cli_group.add_command(delete)
cli_group.add_command(search)

if __name__ == '__main__':
    cli_group()
