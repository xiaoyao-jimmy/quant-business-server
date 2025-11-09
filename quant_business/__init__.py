import os

from flask import Flask
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = '731314806@qq.com'
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'quant.sqlite'),
        JWT_SECRET_KEY='731314806@qq.com',
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    JWTManager(app)

    from . import candlestick
    app.register_blueprint(candlestick.cdbp, url_prefix='/candlestick')
    from . import fundamental
    app.register_blueprint(fundamental.cdbp, url_prefix='/fundamental')

    from . import db
    db.init_app(app)
    return app
