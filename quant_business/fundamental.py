import json

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from quant_business import db

cdbp = Blueprint('fundamental', __name__)


@cdbp.route('/report_fundamental_sign', methods=['POST'])
@jwt_required()
def report_fundamental_sign():
    rows = [tuple(sign_dict.values()) for sign_dict in request.json]
    db.insert_fundamental_sign(rows)
    return {"status": "ok"}


@cdbp.route('/get_fundamental_sign', methods=['GET'])
@jwt_required()
def get_fundamental_sign():
    rows = db.select_fundamental_sign(request.args.get('date'))
    rows_dict = [dict(row) for row in rows]
    return json.dumps(rows_dict)
