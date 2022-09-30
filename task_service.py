from tasklib import TaskWarrior, Task
from tasklib.task import TaskQuerySet


class TaskService:

    def __init__(self):
        self.tw = TaskWarrior(data_location='~/.task', create=True)

    def get_task_by_id(self, id : int) -> Task | None:
        try:
            return self.tw.tasks.get(id=id)
        finally:
            return None

    def get_task_by_uuid(self, uuid : str) -> Task | None:
        try:
            return self.tw.tasks.get(uuid=uuid)
        finally:
            return None

    def get_tasks_by_filter(self, **args) -> TaskQuerySet | None:
        try:
            return self.tw.tasks.filter(due=args['due'])
        finally:
            return None

    def get_all_tasks(self) -> TaskQuerySet | None:
        try:
            return self.tw.tasks.all()
        finally:
            return None


    def sync_standard(self) -> None:
        self.tw.execute_command(['sync'])

    def sync_custom(self) -> None:
        """делаем эндпоинт для синхронизации
        (не та синхронизация что из коробки, а передаём просто периjд времени и список задач)
        с указанием алгоритма/правила/стратегии синхронизации
        (insert/delete missing/merge и т.п. на твоё усмотрение просто сделай несколько режимов)"""
        pass

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

    def delete_task(self, id: int) -> None:
        task_to_delete = self.tw.tasks.get(id=id)
        self.tw.delete_task(task_to_delete)
