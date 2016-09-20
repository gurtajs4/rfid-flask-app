from .. import app
import os
from ..services.sessionRepository import SessionRepository
from flask import json
from flask import Response
from flask import render_template

data_storage_path = os.path.join(os.path.dirname  # /rfid-flask-app
                                 (os.path.dirname  # /rfid-flask-app/appenv
                                  (os.path.dirname  # /rfid-flask-app/appenv/src
                                   (os.path.dirname  # /rfid-flask-app/appenv/src/src
                                    (os.path.dirname  # /rfid-flask-app/appenv/src/src/views
                                     (os.path.abspath(__file__)))))), "data/tagReadings.txt")

_service = SessionRepository(data_storage_path=data_storage_path)


@app.route('/', methods=['GET'])
def api_root():
    return render_template('index.html')


@app.route('/api/sessions', methods=['GET'])
def api_get_sessions():
    data = _service.get_sessions()
    session = json.dumps(data)
    resp = Response(session, status=200, mimetype='application/json')
    return resp


@app.route('/api/sessions/<tagid>', methods=['GET'])
def api_get_session(tagid):
    _tag = _service.get_session(tagid)
    resp = json.dumps(_tag)
    resp.status_code = 200
    return resp
