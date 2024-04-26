from flask import Flask 


def create_app():

  app = Flask(__name__)

  from apps.info import views as info_views
  app.register_blueprint(info_views.info, url_prefix="/info")

  return app