import os
import sys
from flask import Flask, jsonify, request
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.user import User
from models.place import Place
from persistence.data_manager import DataManager


app = Flask(__name__)
data_manager = DataManager()

