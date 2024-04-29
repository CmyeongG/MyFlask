from pathlib import Path
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



db = SQLAlchemy()

def create_app():

  app = Flask(__name__)

  app.config.from_mapping(
    SECRET_KEY='rodlsrhkwpemrkwk',
    SQLALCHEMY_DATABASE_URI=
    f'sqlite:///{Path(__file__).parent.parent / "local.sqlite"}',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
  )

  db.init_app(app)
  Migrate(app, db)

  from apps.info import views as info_views
  app.register_blueprint(info_views.info, url_prefix="/info")

  return app