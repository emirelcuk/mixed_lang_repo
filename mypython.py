import datetime

# Task class
class Task:
    def __init__(self, title, description, due_date, priority='Medium'):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def complete(self):
        self.completed = True


    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return (f"{self.title} | {status} | Priority: {self.priority} | "
                f"Due Date: {self.due_date} \nDescription: {self.description}")

# Task manager class
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date, priority='Medium'):
        task = Task(title, description, due_date, priority)
        self.tasks.append(task)
        self.sort_tasks()
        print(f"Task '{title}' has been added.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")

    def complete_task(self, index):
        if self._is_valid_index(index):
            self.tasks[index].complete()
            print(f"Task '{self.tasks[index].title}' has been completed.")
        else:
            print("Invalid task number.")

    def update_task(self, index, title=None, description=None, due_date=None, priority=None):
        if self._is_valid_index(index):
            self.tasks[index].update(title, description, due_date, priority)
            self.sort_tasks()
            print(f"Task '{self.tasks[index].title}' has been updated.")
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if self._is_valid_index(index):
            task = self.tasks.pop(index)
            print(f"Task '{task.title}' has been deleted.")
        else:
            print("Invalid task number.")

    def sort_tasks(self):
        # Sort tasks by completion status, priority, and due date
        priority_order = {'High': 0, 'Medium': 1, 'Low': 2}
        self.tasks.sort(
            key=lambda task: (task.completed, priority_order.get(task.priority, 1), task.due_date))

    def _is_valid_index(self, index):
        # Check if the index is valid
        return 0 <= index < len(self.tasks)

# Input validation functions


def get_valid_date(prompt):
    while True:
        try:
            date_str = input(prompt)
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_valid_priority():
    priorities = ['Low', 'Medium', 'High']
    priority = input("Priority (Low, Medium, High): ").capitalize()
    if priority not in priorities:
        print("Invalid priority. Defaulting to 'Medium'.")
        return 'Medium'
    return priority

# User interface
def main():
    manager = TaskManager()

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == '1':
            title = input("Task Title: ")
            description = input("Task Description: ")
            due_date = get_valid_date("Due Date (YYYY-MM-DD): ")
            priority = get_valid_priority()
            manager.add_task(title, description, due_date, priority)

        elif choice == '2':
            manager.list_tasks()

        elif choice == '3':
            manager.list_tasks()
            index = get_valid_int("Enter the number of the task to complete: ", 1, len(manager.tasks))
            manager.complete_task(index)

        elif choice == '4':
            manager.list_tasks()
            index = get_valid_int("Enter the number of the task to update: ", 1, len(manager.tasks))
            title = input("New Task Title (leave blank to keep current): ")
            description = input("New Task Description (leave blank to keep current): ")
            due_date = input("New Due Date (YYYY-MM-DD) (leave blank to keep current): ")
            priority = get_valid_priority() if input("Change priority? (Y/N): ").lower() == 'y' else None
            due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date() if due_date else None
            manager.update_task(index, title=title, description=description, due_date=due_date, priority=priority)

        elif choice == '5':
            manager.list_tasks()
            index = get_valid_int("Enter the number of the task to delete: ", 1, len(manager.tasks))
            manager.delete_task(index)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the main program
if __name__ == "__main__":
    main()
