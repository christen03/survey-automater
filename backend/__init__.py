from flask import Flask

def create_app():
    app = Flask(__name__)
    from .views import views
    from .surveys import surveys
    app.register_blueprint(views)
    app.register_blueprint(surveys, url_prefix='/init/')
    return app
