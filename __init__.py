from flask import Flask

def create_app():
    app = Flask(__name__)
    from routes.views import views
    from routes.surveys import surveys
    app.register_blueprint(views)
    app.register_blueprint(surveys, url_prefix='/init/')
    return app
