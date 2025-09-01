import sqlite3
import click
from flask import current_app, g
from requests import get

def select_candlestick_by_date(date):
    return get_db().execute(f'SELECT * FROM candlestick WHERE date = {date}').fetchall()

def insert_candlestick(candlestick_sign):
    get_db().executemany('INSERT INTO candlestick (symbol, date, candlestick_sign) VALUES (?, ?, ?)', candlestick_sign)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'],
                                detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    init_db()
    print('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)