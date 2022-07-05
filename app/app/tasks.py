import settings
from celery import Celery
import time

celery_app = Celery("tasks", broker=settings.CELERY_BROKER_URL)


@celery_app.task
def sleeper_task(sleep_seconds):
    time.sleep(sleep_seconds)
