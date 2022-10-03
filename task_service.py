from tasklib import TaskWarrior, Task
from tasklib.backends import TaskWarriorException
from tasklib.task import TaskQuerySet

'''
=======================================================================================================================
Columns     Type    Modifiable Supported Formats Example
=======================================================================================================================
depends     string  Modifiable list*             1 2 10
                               count             [3]
                               indicator         D
=======================================================================================================================
description string  Modifiable combined*         Move your clothes down on to the lower peg
                                                   2015-12-28 Immediately before your lunch
                                                   2015-12-28 If you are playing in the match this afternoon
                                                   2015-12-28 Before you write your letter home
                                                   2015-12-28 If you're not getting your hair cut
                               desc              Move your clothes down on to the lower peg
                               oneline           Move your clothes down on to the lower peg 2015-12-28 Immediately before your lunch 2015-12-28 If you are playing in the match this afternoon 2015-12-28 Before you write your letter home 2015-12-28 If you're not getting your hair cut
                               truncated         Move your clothes do...
                               count             Move your clothes down on to the lower peg [4]
                               truncated_count   Move your clothes do... [4]
=======================================================================================================================                               
due         date    Modifiable formatted*        2015-12-28
                               julian            2457385.04894
                               epoch             1451308228
                               iso               20151228T131028Z
                               age               2min
                               relative          -2min
                               remaining
                               countdown         PT2M5S
=======================================================================================================================
start       date    Modifiable formatted*        2015-12-28
                               julian            2457385.04894
                               epoch             1451308228
                               iso               20151228T131028Z
                               age               2min
                               relative          -2min
                               remaining
                               countdown         PT2M5S
                               active            *
=======================================================================================================================                                
end         date    Modifiable formatted*        2015-12-28
                               julian            2457385.04894
                               epoch             1451308228
                               iso               20151228T131028Z
                               age               2min
                               relative          -2min
                               remaining
                               countdown         PT2M5S
=======================================================================================================================                               
entry       date    Modifiable formatted*        2015-12-28
                               julian            2457385.04894
                               epoch             1451308228
                               iso               20151228T131028Z
                               age               2min
                               relative          -2min
                               remaining
                               countdown         PT2M5S
=======================================================================================================================                               
id          numeric Read Only  number*           123
=======================================================================================================================                               
uuid        string  Read Only  long*             f30cb9c3-3fc0-483f-bfb2-3bf134f00694
                               short             f30cb9c3
=======================================================================================================================
imask       numeric Read Only  number*           12
=======================================================================================================================
mask        string  Read Only  default*          ++++---
=======================================================================================================================
modified    date    Modifiable formatted*        2015-12-28
                               julian            2457385.04894
                               epoch             1451308228
                               iso               20151228T131028Z
                               age               2min
                               relative          -2min
                               remaining
                               countdown         PT2M5S
=======================================================================================================================                               
parent      string  Read Only  long*             f30cb9c3-3fc0-483f-bfb2-3bf134f00694
                               short             f30cb9c3
=======================================================================================================================                               
priority    string  Modifiable default*
                               indicator
=======================================================================================================================                               
project     string  Modifiable full*             home.garden
                               parent            home
                               indented          home.garden
=======================================================================================================================                               
recur       string  Modifiable duration*         weekly
                               indicator         R
=======================================================================================================================                               
scheduled   date    Modifiable formatted*        2015-12-28
                               julian            2457385.04894
                               epoch             1451308228
                               iso               20151228T131028Z
                               age               2min
                               relative          -2min
                               remaining
                               countdown         PT2M5S
=======================================================================================================================                                                            
status      string  Modifiable long*             Pending
                               short             P
=======================================================================================================================                               
tags        string  Modifiable list*             home @chore next
                               indicator         +
                               count             [2]
=======================================================================================================================                               
until       date    Modifiable formatted*        2015-12-28
                               julian            2457385.04894
                               epoch             1451308228
                               iso               20151228T131028Z
                               age               2min
                               relative          -2min
                               remaining
                               countdown         PT2M5S
=======================================================================================================================                               
wait        date    Modifiable formatted*        2015-12-28
                               julian            2457385.04894
                               epoch             1451308228
                               iso               20151228T131028Z
                               age               2min
                               relative          -2min
                               remainingx
                               countdown         PT2M5S
=======================================================================================================================                               
                               
Modifiable default Means default format, and therefore optional.
For example, 'due' and 'due.formatted' are equivalent.

'''

class TaskService:

    def __init__(self):
        self._tw = TaskWarrior(data_location='~/.task', create=True)

    def get_task_by_id(self, id : int) -> Task | None:
        task = None
        try:
            task = self._tw.tasks.get(id=id)
        finally:
            return task

    def get_task_by_uuid(self, uuid : str) -> Task | None:
        task = None
        try:
            task = self._tw.tasks.get(uuid=uuid)
        finally:
            return task

    def get_tasks_by_filter(self, **args) -> TaskQuerySet | None:
        tasks = None
        try:
            tasks = self._tw.tasks.filter(due=args['due'])
        finally:
            return tasks

    def get_all_tasks(self) -> TaskQuerySet | None:
        tasks = None
        try:
            tasks = self._tw.tasks.all()
        finally:
            return tasks

    def try_sync_standard(self) -> bool:
        """Try to sync """
        try:
            self._tw.execute_command(['sync'])
        except TaskWarriorException:
            return False
        return True


    def sync_custom(self) -> None:
        """делаем эндпоинт для синхронизации
        (не та синхронизация что из коробки, а передаём просто периjд времени и список задач)
        с указанием алгоритма/правила/стратегии синхронизации
        (insert/delete missing/merge и т.п. на твоё усмотрение просто сделай несколько режимов)"""
        pass

    def create_task(self, create_task_request) -> int:
        """Create Tasks. Returns id of created task"""
        new_task = Task(self._tw)
        new_task['description'] = create_task_request['description']
        new_task['due'] = create_task_request['due']
        new_task['priority'] = create_task_request['priority']
        new_task['project'] = create_task_request['project']
        new_task['tags'] = create_task_request['tags']
        new_task.save()
        return new_task['id']

    def update_task(self, id: int, update_task_request) -> None:
        task_to_update = self._tw.tasks.get(id=id)
        task_to_update['project'] = update_task_request['project']
        task_to_update['description'] = update_task_request['description']
        task_to_update['due'] = update_task_request['due']
        task_to_update['priority'] = update_task_request['priority']
        task_to_update['tags'] = update_task_request['tags']
        task_to_update.save()

    def delete_task(self, id: int) -> None:
        task_to_delete = self._tw.tasks.get(id=id)
        self._tw.delete_task(task_to_delete)

    def start_task(self, id: int) -> None:
        task_to_start : Task = self._tw.tasks.get(id=id)
        task_to_start.start()
