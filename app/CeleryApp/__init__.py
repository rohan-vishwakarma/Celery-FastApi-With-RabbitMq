from celery import Celery
import time
from celery.utils.log import get_task_logger
from app.CeleryApp.celeryconfig import *
from celery.schedules import crontab

celery = Celery('tasks', broker='pyamqp://guest:guest@localhost//', backend='redis://localhost:6379/2')
celery.config_from_object('app.CeleryApp.celeryconfig')
#
# celery.conf.beat_schedule = {
#     'add-every-minutes': {
#             'task': 'app.CeleryApp.schedule_job',
#             'schedule': crontab(),
#             'args': ("hello", "rohan")
#         },
# }

logger = get_task_logger(__name__)

@celery.task(bind=True)
def addition(self, num1, num2):
    logger.info("TASK STARTED EXECUTING FOR ADDITION OF PROGRAM")
    time.sleep(5)
    self.update_state(state="PROGRESS", meta={'progress': 50})
    time.sleep(5)
    self.update_state(state="PROGRESS", meta={'progress': 90})
    time.sleep(1)
    return num1 + num2

@celery.task
def schedule_job(num1, num2) -> str:
    logger.info("CELERY BEAT STARTED")
    time.sleep(5)
    logger.info("Celery task Complete")
    return num1 + num2
