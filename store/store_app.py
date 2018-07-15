from flask import Flask
from flask_cors import CORS
from config import Config


config = Config()
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": [config.allowed_url]}})
