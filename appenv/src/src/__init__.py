import os
from flask import Flask
app = Flask(__name__)

# app.config.from_object('src.settings')
root_path = os.path.join(os.path.dirname  # /rfid-flask-app
                        (os.path.dirname  # /rfid-flask-app/appenv
                        (os.path.dirname  # /rfid-flask-app/appenv/src
                        (os.path.dirname  # /rfid-flask-app/appenv/src/src
                        (os.path.abspath(__file__))))), "data/")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + root_path + 'rfiddb.sqlite'
# app.url_map.strict_slashes = False


from . import core
from models import models
from views import views
