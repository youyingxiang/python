from flask import Flask
from apps.cms import bp as cms_bp
from apps.common import bp as common_bp
from apps.home import bp as home_bp
import config
from exts import db,mail,alidayu
from flask_wtf import CSRFProtect


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(cms_bp)
    app.register_blueprint(common_bp)
    app.register_blueprint(home_bp)

    db.init_app(app)
    mail.init_app(app)
    alidayu.init_app(app)
    CSRFProtect(app)

    return app



if __name__ == '__main__':
    app = create_app()
    app.run(port=5000)
