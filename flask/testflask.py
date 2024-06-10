#!/bin/python

from flask import Flask, render_template
import requests
import json
app = Flask(_name_)

@app.route('/')
def index():
    return "D"

app.run(host="0.0.0.0", port=80)
