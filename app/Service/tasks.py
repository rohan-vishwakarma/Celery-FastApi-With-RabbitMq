from fastapi import APIRouter, Form
from typing import Annotated
from celery.utils.log import get_task_logger
from celery.result import AsyncResult

import asyncio
from app.CeleryApp import addition
task_router = APIRouter()
from app.CeleryApp import celery
@task_router.post('/')
async def addition_task(num1 : Annotated[str, Form()], num2: Annotated[str, Form()]):
    try:
        taskk = celery.send_task('app.CeleryApp.addition', kwargs={"num1" : int(num1), "num2" : int(num2)})
        print(f"Celery Task invoked for addition program, initial state is {taskk.status} & task Id is {taskk.id}")
        return {"Task Result is ": taskk.id, "status" : taskk.status }

        print("Task completed")
    except Exception as e:
        print(e)


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
