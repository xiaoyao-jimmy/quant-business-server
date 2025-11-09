import sqlite3

import click
from flask import current_app, g


def select_candlestick_by_date(date):
    rows = get_db().execute(f"SELECT symbol, date, candlestick_sign, candlestick_bullish_sign, candlestick_bearish_sign FROM candlestick WHERE date = '{date}'").fetchall()
    return rows


def insert_candlestick(candlestick_sign):
    get_db().executemany('INSERT INTO candlestick (symbol, date, candlestick_sign) VALUES (?, ?, ?) ON CONFLICT(symbol, date) DO UPDATE SET candlestick_sign = excluded.candlestick_sign', candlestick_sign)
    get_db().commit()


def insert_bullish_candlestick(candlestick_bullish_sign):
    get_db().executemany('INSERT INTO candlestick (symbol, date, candlestick_bullish_sign) VALUES (?, ?, ?) ON CONFLICT(symbol, date) DO UPDATE SET candlestick_bullish_sign = excluded.candlestick_bullish_sign', candlestick_bullish_sign)
    get_db().commit()


def insert_bearish_candlestick(candlestick_bearish_sign):
    get_db().executemany('INSERT INTO candlestick (symbol, date, candlestick_bearish_sign) VALUES (?, ?, ?) ON CONFLICT(symbol, date) DO UPDATE SET candlestick_bearish_sign = excluded.candlestick_bearish_sign', candlestick_bearish_sign)
    get_db().commit()


def insert_fundamental_sign(fundamental_sign):
    get_db().executemany('INSERT INTO fundamental (symbol, date, fundamental_sign) VALUES (?, ?, ?) ON CONFLICT(symbol, date) DO UPDATE SET fundamental_sign = excluded.fundamental_sign', fundamental_sign)
    get_db().commit()


def select_fundamental_sign(date):
    rows = get_db().execute(f'SELECT symbol, date, fundamental_sign FROM fundamental WHERE date = "{date}"').fetchall()
    return rows


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
    with current_app.open_resource('json.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    init_db()
    print('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
