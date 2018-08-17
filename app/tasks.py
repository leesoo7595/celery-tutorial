from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('config', broker='pyamqp://guest@localhost//')


@app.task
def add(x, y):
    return x + y