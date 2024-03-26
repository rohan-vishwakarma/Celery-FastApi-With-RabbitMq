from celery import Celery
import time
from celery.utils.log import get_task_logger
from app.CeleryApp.celeryconfig import *

celery = Celery('tasks', broker='pyamqp://guest:guest@localhost//', backend='redis://localhost:6379/0')
celery.config_from_object('app.CeleryApp.celeryconfig')
logger = get_task_logger(__name__)


@celery.task
def addition(num1, num2):
    return num1 + num2
