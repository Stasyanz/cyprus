"""Celery app"""

import os

from celery import Celery


app = Celery('balance',
             broker=os.getenv("CELERY_BROKER"),
             # backend=os.getenv("CELERY_BACKEND"),
             include=['balance.tasks'])

app.conf.update(
    result_expires=3600,
)


if __name__ == '__main__':
    app.start()
