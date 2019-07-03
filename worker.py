from celery import Celery
app = Celery("task",
             include=['tasks'],
             broker='amqp://')
