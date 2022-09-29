from datetime import datetime
from tasklib import TaskWarrior, Task


class TaskService:

    def __init__(self):
        self.tw = TaskWarrior(data_location='~/.task', create=True)

    def get_task_by_id(self, id: int):
        return self.tw.tasks.get(id=id)

    def get_task(self):
        pass

    def get_tasks_by_filter(self):
        pass

    def get_all_tasks(self):
        tasks = self.tw.tasks.all()
        return tasks

    def create_task(self, create_task_request) -> int:
        """Create Tasks. Returns id of created task"""
        new_task = Task(self.tw)
        new_task['description'] = create_task_request['description']
        new_task['due'] = create_task_request['due']
        new_task['priority'] = create_task_request['priority']
        new_task.save()
        return new_task['id']

    def update_task(self, id: int, update_task_request) -> None:
        task_to_update = self.tw.tasks.get(id=id)
        task_to_update['description'] = update_task_request['description']
        task_to_update['due'] = update_task_request['due']
        task_to_update['priority'] = update_task_request['priority']
        task_to_update.save()

    def delete_task(self, uuid: int) -> None:
        task_to_delete = self.tw.tasks.get(uuid=id)
        self.tw.delete_task(task_to_delete)
