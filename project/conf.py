from celery import Celery

app = Celery('project',
             broker='redis://127.0.0.1:6379',
             backend='redis://127.0.0.1:6379',
             include=['project.tasks'])


if __name__ == '__main__':
    app.start()