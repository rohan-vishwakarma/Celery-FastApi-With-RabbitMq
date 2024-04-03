
try:
    import redis
    from fastapi import APIRouter, Form, Request
    from typing import Annotated
    from fastapi.responses import HTMLResponse, RedirectResponse

    from celery.utils.log import get_task_logger
    from celery.result import AsyncResult
    from redis import Redis
    import asyncio
    from app.CeleryApp import addition
    task_router = APIRouter()
    from app.CeleryApp import celery
    from fastapi.templating import Jinja2Templates

except Exception as e:
    print(e)
redis_instance = redis.Redis(host='localhost', port=6379, db='0')

templates = Jinja2Templates(directory="app/htmltemplates")




def on_raw_message(body):
    task_id = str(body['task_id'])
    text = str("celery-task-meta-") + task_id
    redis_key = text
    redis_value = redis_instance.get(redis_key)
    redis_instance.flushdb()

@task_router.post('/', response_class=HTMLResponse)
async def addition_task(request: Request,num1: Annotated[str, Form()], num2: Annotated[str, Form()]):
    try:

        taskk = celery.send_task('app.CeleryApp.addition', kwargs={"num1" : int(num1), "num2" : int(num2)}, retries=0)

        res = taskk.get(on_message = on_raw_message, propagate=False)
        print("Result of the task is " , res, "And Task id is :", taskk.id)
        print(f"Celery Task invoked for addition program, initial state is {taskk.status} & task Id is {taskk.id}")
        # return {"Task Result is ": taskk.id, "status" : taskk.status }
        print("Task completed")
        mess = str(f'Result of the task is {res} And Task id is  {taskk.id}')
        return templates.TemplateResponse(request=request, name='index.html', context={'mess': mess})


    except Exception as e:
        print(e)
        print("Something went wrong")


@task_router.get('/{id}')
def get_status(id):
    try:
        st = celery.AsyncResult(id)
        print(dir(st))
        print(st.state)
        return {"Task id" : st.task_id, "Result": st.result , "Kwargs" : st.kwargs, "args": st.args, "status" : st.state, "name": st.name,
                "Ready" : st.ready(), "on ready": st.on_ready, "Worker" : st.worker,
                "date done": st.date_done, "on fulfilled": st._on_fulfilled, "info": st.info, "as list": st.as_list}
    except Exception as e:
        print("Exception Occurred")
        print(e)
