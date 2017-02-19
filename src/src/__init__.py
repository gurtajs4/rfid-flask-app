from . import config
from flask import Flask, session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

socket_io = SocketIO(app=app)

from models import models
from views import views
from . import io_sockets