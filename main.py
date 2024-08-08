import uuid
from todo_list import ToDoList

def main():
    manager = ToDoList()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Clear all tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            manager.add_task(title, description)
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            task_id = input("Enter task ID to mark as completed: ")
            try:
                task_uuid = uuid.UUID(task_id)
                manager.mark_task_completed(task_uuid)
            except ValueError:
                print("Invalid ID format. Please enter a valid UUID.")
        elif choice == "4":
            manager.clear_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

