from flask import Flask, jsonify
from app.config import Config

from celery import Celery

celery = Celery(
    __name__,
    broker=Config.CELERY_BROKER_URL,
    backend=Config.CELERY_RESULT_BACKEND,
    include=['app.tasks']
)


def create_app():
    app = Flask(__name__)
    celery.conf.update(app.config)

    @app.route('/')
    def index():
        return 'Hello Flask Celery'

    @app.route('/process/<interval>')
    def process(interval):
        from .tasks import process
        task = process.delay(interval)
        return jsonify({
            'task_id': task.id
        })

    return app
