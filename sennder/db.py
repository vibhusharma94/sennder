import click
import redis
from flask import g
from flask.cli import with_appcontext
from sennder.configs.config import REDIS_HOST, REDIS_PORT


def get_db(db_no=0):
    if 'db' not in g:
        pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=db_no)
        g.db = redis.Redis(connection_pool=pool)

    return g.db


def close_db(e=None):
    g.pop('db', None)


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    get_db()
    click.echo('Initialized the database.')
