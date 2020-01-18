import sqlite3

from flask import current_app, g
from api import routes

DATABASE = 'trails.db'
_app = None

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


def init_db(app):
    _app = app
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    db.row_factory = make_dicts


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            DATABASE
        )
        g.db.row_factory = make_dicts
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv
