"""Celery app"""

from celery import Celery


app = Celery('balance',
             broker='redis://127.0.0.1:6379/0',
             # backend='rpc://',
             include=['balance.tasks'])

app.conf.update(
    result_expires=3600,
)


if __name__ == '__main__':
    app.start()
