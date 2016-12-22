from flask import Flask
app = Flask(__name__)

# app.config.from_object('src.settings')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////rfid-flask-app/data/rfiddb.sqlite'
# app.url_map.strict_slashes = False


from . import core
from models import models
from views import views
