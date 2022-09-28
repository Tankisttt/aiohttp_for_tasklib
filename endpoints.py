"""CRUD operations for Tasks"""
from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from task_service import TaskService

TASK_ID = 'task_id'

routes = web.RouteTableDef()
taskwarrior_service = TaskService()

@routes.get(f'/{TASK_ID}')
async def get_by_task_id_handler(request: Request) -> Response:
    """Get Task by its id."""
    task_id = request.match_info[f'{TASK_ID}']
    taskwarrior_service.get_task()
    return web.Response(text=f"Hello, get task with id: {task_id}")


@routes.get('/')
async def get_tasks_handler(request: Request) -> Response:
    """Get Tasks."""
    taskwarrior_service.create_task()
    return web.json_response(text=f"typeof request is: {type(request)}")


@routes.post('/')
async def create_task_handler(request: Request) -> Response:
    """Create Task."""
    task_id = 222
    response = {'task_id': f'{task_id}'}
    return web.json_response(response)


@routes.patch(f'/{TASK_ID}')
async def update_task_handler(request: Request) -> Response:
    """Update Task by its id."""
    task_id = 222
    response = {'task_id': f'{task_id}'}
    return web.HTTPNoContent()


@routes.delete(f'/{TASK_ID}')
async def delete_task_handler(request: Request) -> Response:
    """Delete Task by its id."""
    task_id = 222
    response = {'task_id': f'{task_id}'}
    return web.HTTPNoContent()
