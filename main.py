from flask import Flask
from routes.views import views
from routes.surveys import surveys

app=Flask(__name__)
app.register_blueprint(views)
app.register_blueprint(surveys, url_prefix='/init/')

if __name__=='__main__':
    app.run(debug=True, port=9000)