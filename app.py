from flask import Flask
from api.views.users import app as users_app

app = Flask(__name__)
app.register_blueprint(users_app, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(debug=True)
