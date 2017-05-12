from . import config
from flask import Flask, session
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
auth = HTTPTokenAuth('Token ')

from models import models
from views import views
