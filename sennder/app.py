import logging

from celery import Celery
from flask import Flask
from flask_restful import Api

from sennder.configs import celeryconfig
from sennder.resources import Movies, HomeController
from sennder.db import close_db, init_db_command

logging.basicConfig(level=logging.DEBUG)


def create_app():
    app = Flask('sennder')
    app.config.from_object('sennder.configs.config')
    app = add_resources(app)
    init_app(app)
    return app


def add_resources(app):
    api = Api(app)
    api.add_resource(HomeController, "/")
    api.add_resource(Movies, "/movies")
    return app


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def make_celery(app):
    # create context tasks in celery
    celery = Celery(
        app.import_name,
        broker=app.config['BROKER_URL']
    )
    celery.conf.update(app.config)
    celery.config_from_object(celeryconfig)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

    return celery
