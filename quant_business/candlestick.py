import json

from flask import Blueprint, request
from . import db

cdbp = Blueprint('candlestick', __name__)


@cdbp.route('/report_candlestick_sign', methods=['POST'])
def report_candlestick_sign():
    # request.authorization().token
    # request.authorization.token
    rows = [tuple(sign_dict.values()) for sign_dict in request.json]
    db.insert_candlestick(rows)
    return {"status": "ok"}


@cdbp.route('/get_candlestick_sign', methods=['GET'])
def get_candlestick_sign():
    rows = db.select_candlestick_by_date(request.args.get("date"))
    return {"status": "ok"}
