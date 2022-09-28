from datetime import datetime
from tasklib import TaskWarrior, Task

class TaskService:

    def __init__(self):
        self.tw = TaskWarrior(data_location='~/.task', create=False)

    def get_task_by_id(self):
        pass

    def get_task(self):
        pass

    def get_tasks_by_filter(self):
        pass

    def get_all_tasks(self):
        pass

    def create_task(self) -> int:
        """Create Tasks. Returns id of created task"""
        # complex_task = Task(tw, description="finally fix the shower", due=datetime(2015, 2, 14, 8, 0, 0), priority='H')
        new_task = Task(self.tw, description="throw out the trash")
        new_task.save()
        return new_task['id']

    def update_task(self, id: int, task) -> int:
        task_to_update = self.tw.tasks.get(id=id)
        task_to_update['description'] = task['description']
        task_to_update['due'] = task['due']
        task_to_update['priority'] = task['priority'] # 'H'
        task_to_update.save()
        return task_to_update['id']
