import uuid

class Task:
    def __init__(self, title, description):
        self.id = uuid.uuid4()
        self.title = title
        self.description = description
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"ID: {self.id}\nTitle: {self.title}\nDescription: {self.description}\nStatus: {status}"
