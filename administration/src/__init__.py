import os
from . import config
from flask import Flask, session

app = Flask(__name__)
app.debug = os.environ['FLASK_DEBUG']
app.secret_key = config.SECRET_KEY

from models import models
# from views import views
import views
