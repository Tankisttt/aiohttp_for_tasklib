"""CRUD operations for Tasks"""
from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from task_service import TaskService

routes = web.RouteTableDef()
task_service = TaskService()


@routes.get('/{task_id}')
async def get_by_task_id_handler(request: Request) -> Response:
    """Get Task by its id."""
    task_id = request.match_info['task_id']
    task = task_service.get_task_by_id(task_id)
    if task is None:
        return web.HTTPNotFound(Exception(f'task with id:{task_id}" is not found'))
    return web.Response(text=f"Hello, get task with id: {task_id}")


@routes.get('/all')
async def get_all_tasks(request: Request) -> Response:
    """Get all tasks"""
    tasks = task_service.get_all_tasks()
    tasks_as_list = list(tasks)

    for t in tasks_as_list:
        print(t['description'])

    return web.json_response()

@routes.get('/')
async def get_tasks_handler(request: Request) -> Response:
    """Get Tasks."""
    task_service.create_task()
    return web.json_response(text=f"typeof request is: {type(request)}")


@routes.post('/')
async def create_task_handler(request: Request) -> Response:
    """Create Task."""
    if not request.body_exists:
        return web.HTTPBadRequest()
    request_data = await request.json()

    task_id = task_service.create_task()
    response = {'created_task_id': f'{task_id}'}
    return web.json_response(response)


@routes.patch('/{task_id}')
async def update_task_handler(request: Request) -> Response:
    """Update Task by its id."""
    task_id = request.match_info['task_id']
    task_service.update_task(task_id, )
    return web.HTTPNoContent()


@routes.delete('/{task_id}')
async def delete_task_handler(request: Request) -> Response:
    """Delete Task by its id."""
    task_id = request.match_info['task_id']
    task_service.delete_task(task_id)
    return web.HTTPNoContent()
