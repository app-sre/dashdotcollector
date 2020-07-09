import os

from celery import Celery


RMQ_URL = os.environ['RABBITMQ_URL']

app = Celery('tasks', broker=RMQ_URL)
