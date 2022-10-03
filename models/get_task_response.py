import json


class GetTaskResponse:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.uuid = kwargs['uuid']
        self.description = kwargs['description']
        self.due = kwargs['due']
        self.priority = kwargs['priority']
        self.project = kwargs['project']
        self.tags = kwargs['tags']

    def toJSON(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True,
                          indent=4)