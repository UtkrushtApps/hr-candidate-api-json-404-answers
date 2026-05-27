from flask import Flask
from app.models import db


def create_app(config=None):
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "dev-secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hr.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if config:
        app.config.update(config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from app.routes import candidates_bp
    app.register_blueprint(candidates_bp)

    return app
