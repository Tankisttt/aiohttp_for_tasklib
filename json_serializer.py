import json


class TaskData:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class TaskEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


# Create an instance and serialize it with our new encoder
the_value = [TaskData("Paris", 120), TaskData("Paris", 120), TaskData("Paris", 120)]
jsonized = json.dumps(the_value, indent=4, cls=TaskEncoder)
print(jsonized)
