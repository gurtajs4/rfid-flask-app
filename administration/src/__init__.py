from . import config
from flask import Flask, session

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

from models import models
from views import views
