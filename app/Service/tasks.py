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
    taskk = celery.send_task('app.CeleryApp.addition', kwargs={"num1" : int(num1), "num2" : int(num2)})
    print(f"Celery Task invoked for addition program, initial state is {taskk.status} & task Id is {taskk.id}")
    return {"Task Result is ": taskk.id}


@task_router.get('/{id}')
def get_status(id):
    try:
        st = celery.AsyncResult(id)
        print(st.state)
        return {f"the status for the  {id} is" : st.result}
    except Exception as e:
        print("Exception Occurred")
        print(e)
