import datetime

# Task class (Assuming a simple Task class implementation)
class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False



# Task manager class
class TaskManager:
    
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def complete_task(self, index):
        if self._is_valid_index(index):
            task = self.tasks[index]
            task.complete()
            print(f"Task '{task.title}' has been completed.")
        else:
            print("Invalid task number.")

    def update_task(self, index, title=None, description=None, due_date=None, priority=None):
        if not self._is_valid_index(index):
            print("Invalid task number.")
            return

        task = self.tasks[index]

        if title:
            task.title = title
        if description:
            task.description = description
        if due_date:
            task.due_date = due_date
        if priority:
            task.priority = priority

        self.sort_tasks()
        print(f"Task '{task.title}' has been updated.")

    def delete_task(self, index):
        if not self._is_valid_index(index):
            print("Invalid task number.")
            return

        task = self.tasks.pop(index)
        print(f"Task '{task.title}' has been deleted.")

    def sort_tasks(self):
        priority_order = {'High': 0, 'Medium': 1, 'Low': 2}
        self.tasks.sort(
            key=lambda task: (task.completed, priority_order.get(task.priority, 1), task.due_date)
        )

    def _is_valid_index(self, index):
        return 0 <= index < len(self.tasks)

# Input validation functions
def get_valid_date(prompt):
    while True:
        date_str = input(prompt)
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_valid_priority():
    priorities = ['Low', 'Medium', 'High']
    while True:
        priority = input("Priority (Low, Medium, High): ").capitalize()
        if priority in priorities:
            return priority
        print("Invalid priority. Please choose from 'Low', 'Medium', or 'High'.")

def get_valid_int(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value - 1  # to match zero-indexing
            print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

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
            if manager.tasks:
                index = get_valid_int("Enter the number of the task to complete: ", 1, len(manager.tasks))
                manager.complete_task(index)

        elif choice == '4':
            manager.list_tasks()
            if manager.tasks:
                index = get_valid_int("Enter the number of the task to update: ", 1, len(manager.tasks))
                title = input("New Task Title (leave blank to keep current): ") or None
                description = input("New Task Description (leave blank to keep current): ") or None
                due_date = input("New Due Date (YYYY-MM-DD) (leave blank to keep current): ") or None
                priority = get_valid_priority() if input("Change priority? (Y/N): ").lower() == 'y' else None
                due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date() if due_date else None
                manager.update_task(index, title, description, due_date, priority)

        elif choice == '5':
            manager.list_tasks()
            if manager.tasks:
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
