"""CRUD operations for Tasks"""
from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from task_service import TaskService

TASK_ID = 'task_id'

routes = web.RouteTableDef()
task_service = TaskService()


@routes.get(f'/{TASK_ID}')
async def get_by_task_id_handler(request: Request) -> Response:
    """Get Task by its id."""
    task_id = request.match_info[f'{TASK_ID}']
    task = task_service.get_task_by_id(task_id)

    return web.Response(text=f"Hello, get task with id: {task}")


@routes.get('/all')
async def get_all_tasks(request: Request) -> Response:
    """Get all tasks"""
    tasks = task_service.get_all_tasks()
    taskss = list(tasks)

    for t in taskss:
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
    task_uuid = task_service.create_task(await request.json())
    response = {'task_uuid': f'{task_uuid}'}
    return web.json_response(response)


@routes.patch(f'/{TASK_ID}')
async def update_task_handler(request: Request) -> Response:
    """Update Task by its id."""
    task_id = request.match_info[f'{TASK_ID}']
    task_service.update_task(task_id, )
    return web.HTTPNoContent()


@routes.delete(f'/{TASK_ID}')
async def delete_task_handler(request: Request) -> Response:
    """Delete Task by its id."""
    task_id = request.match_info[f'{TASK_ID}']
    task_service.delete_task(task_id)
    return web.HTTPNoContent()
