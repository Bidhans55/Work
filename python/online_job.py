# This snippet represents a simplified version of the task creation component.

class Task:
    def __init__(self, title, description, assigned_to):
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        self.status = "Pending"

    def update_status(self, status):
        self.status = status

class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, title, description, assigned_to):
        if not title or not description or not assigned_to:
            raise ValueError("All fields are required")
        task = Task(title, description, assigned_to)
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

def main():
    task_manager = TaskManager()

    title = input("Enter task title: ")
    description = input("Enter task description: ")
    assigned_to = input("Enter assignee: ")

    try:
        task_manager.create_task(title, description, assigned_to)
    except ValueError as e:
        print(f"Error: {e}")
        return

    tasks = task_manager.get_tasks()
    for task in tasks:
        print(f"Title: {task.title} | Description: {task.description} | Assigned to: {task.assigned_to} | Status: {task.status}")

if __name__ == "__main__":
    main()