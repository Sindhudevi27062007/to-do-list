import os

# ToDo List Class
class ToDoList:
    def __init__(self):
        self.tasks = []  # List to store tasks

    def display_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            print("\nYour To-Do List:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully.")

    def update_task(self, task_number, updated_task):
        if task_number <= len(self.tasks):
            self.tasks[task_number - 1] = updated_task
            print(f"Task {task_number} updated to '{updated_task}'.")
        else:
            print("Invalid task number!")

    def delete_task(self, task_number):
        if task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed successfully.")
        else:
            print("Invalid task number!")

# Menu to interact with the ToDo List
def display_menu():
    print("\nTo-Do List Menu")
    print("1. View tasks")
    print("2. Add a new task")
    print("3. Update an existing task")
    print("4. Delete a task")
    print("5. Exit")

# Main function to run the To-Do List application
def main():
    todo_list = ToDoList()
    
    while True:
        display_menu()
        choice = input("Please select an option (1-5): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task = input("Enter the task to add: ")
            todo_list.add_task(task)
        elif choice == '3':
            task_number = int(input("Enter task number to update: "))
            updated_task = input("Enter the updated task: ")
            todo_list.update_task(task_number, updated_task)
        elif choice == '4':
            task_number = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
