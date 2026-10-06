class Task:
    def __init__(self , name: str):
        self.name = name
        self.task_depends_on = []

class Workflow:
    def __init__(self):
        self.tasks = {}
    
    def add_tasks(self , task :  Task):
        self.tasks[task.name]= task
        