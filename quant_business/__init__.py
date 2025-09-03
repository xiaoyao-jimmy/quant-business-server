import os
from flask import Flask
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'quant.sqlite'),
        JWT_SECRET_KEY=''
    )
    jwt = JWTManager(app)
    

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from . import candlestick
    app.register_blueprint(candlestick.cdbp)

    from . import db
    db.init_app(app)
    return app
