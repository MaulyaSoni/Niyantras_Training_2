from typing import Optional
from core import Workflow , Task

class WorkflowBuilder:
    def __init__(self):
        self.workflow = Workflow()
        self.current_task = None

    def add_task_step(self , name : str):
        task = Task(name)
        self.workflow.add_tasks(task)        
        self.current_task = task
        return self
    
    def depends_on(self , task_name : str):
        if not self.current_task:
            raise ValueError("Not in current task")

        if task_name not in self.workflow.tasks:
            raise ValueError("Task not present in workflow")

        dependency = self.workflow.tasks[task_name]
        self.current_task.task_depends_on.append(dependency)
        return self 
    
    def build(self):
        return self.workflow