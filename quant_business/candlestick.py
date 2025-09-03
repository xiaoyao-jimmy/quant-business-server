import json

from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from . import db

cdbp = Blueprint('candlestick', __name__)

@jwt_required()
@cdbp.route('/report_candlestick_sign', methods=['POST'])
def report_candlestick_sign():
    # request.authorization().token
    # request.authorization.token
    rows = [tuple(sign_dict.values()) for sign_dict in request.json]
    db.insert_candlestick(rows)
    return {"status": "ok"}

@jwt_required()
@cdbp.route('/get_candlestick_sign', methods=['GET'])
def get_candlestick_sign():
    rows = db.select_candlestick_by_date(request.args.get("date"))
    return {"status": "ok"}
