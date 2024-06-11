#!/bin/python

from flask import Flask
from api.views.users import app as users_app

app = Flask(__name__)

@app.route('/')
def index():
    return "D"

app.run(host="0.0.0.0", port=5000)