from flask import Flask
from config import Config
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000"]}})
app.config.from_object(Config)

from store import routes
from store import utils
