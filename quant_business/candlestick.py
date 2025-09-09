import functools
import json

import yfinance as yf
from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from . import db

cdbp = Blueprint('candlestick', __name__)


@cdbp.route('/report_candlestick_sign', methods=['POST'])
@jwt_required()
def report_candlestick_sign():
    rows = [tuple(sign_dict.values()) for sign_dict in request.json]
    db.insert_candlestick(rows)
    return {"status": "ok"}


@cdbp.route('/get_candlestick_sign', methods=['GET'])
@jwt_required()
def get_candlestick_sign():
    return get_candlestick_sign_date(request.args.get("date"))


@functools.cache
def get_candlestick_sign_date(date):
    rows = db.select_candlestick_by_date(date)
    rows_dict = [dict(row) for row in rows]
    yf.set_config(proxy='http://127.0.0.1:7890')
    symbols = [row_dict['symbol'] for row_dict in rows_dict]
    tickers = yf.Tickers(' '.join(symbols))
    for row_dict in rows_dict:
        row_dict['candlestick_draw'] = []
        history = tickers.tickers[row_dict['symbol']].history(period='90d').to_dict(orient='index')
        for key, value in history.items():
            date_str = key.date().strftime('%Y-%m-%d')
            value['Time'] = date_str
            value['Open'] = round(value['Open'], 2)
            value['Close'] = round(value['Close'], 2)
            value['High'] = round(value['High'], 2)
            value['Low'] = round(value['Low'], 2)
            row_dict['candlestick_draw'].append(value)

    return json.dumps(rows_dict)