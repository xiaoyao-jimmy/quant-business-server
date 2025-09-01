from flask import Blueprint


cdbp = Blueprint('candlestick', __name__)

@cdbp.route('/report_candlestick_sign', methods=['POST'])
def report_candlestick_sign(candlestick_sign):
    pass

@cdbp.route('/get_candlestick_sign', methods=['GET'])
def get_candlestick_sign(date):
    pass