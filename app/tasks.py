import time
from app import celery


@celery.task
def process(interval):
    time.sleep(int(interval))
