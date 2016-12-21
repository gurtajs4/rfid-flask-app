from flask import Flask
app = Flask(__name__)

app.config.from_object('src.settings')

# app.url_map.strict_slashes = False


from . import core
from models import models
from views import views
