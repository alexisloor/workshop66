from task import Task

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        print("Task added successfully.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
            return
        for task in self.tasks:
            print(task)
            print("-" * 40)

    def mark_task_completed(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                print("Task marked as completed.")
                return
        print("Task not found.")
    
    def edit_task(self, task_id, new_title, new_description):
        for task in self.tasks:
            if task.id == task_id:
                task.title = new_title
                task.description = new_description
                print("Task updated successfully.")
                return
            print("Task not found.")

    def clear_tasks(self):
        self.tasks.clear()
        print("All tasks cleared.")
