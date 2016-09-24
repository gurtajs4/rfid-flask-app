from .. import app
import os
from ..services.sessionRepository import SessionRepository
from flask import jsonify
from flask import request
from flask import render_template
from flask import Response
from flask import Markup


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
    resp = jsonify(data)
    resp.status_code = 200
    return resp


@app.route('/api/sessions/<int:session_id>', methods=['GET'])
def api_get_session(session_id):
    session = _service.get_session(session_id)
    if session is not None:
        resp = Response(str(session), status=200, mimetype='application/json')
        # resp = jsonify(session)
        # resp.status_code = 200
        return resp
    else:
        message = {
            'status': 404,
            'message': 'Not Found' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp


@app.route('/api/testing', methods=['GET'])
def api_testing():
    data = _service.get_sessions()
    resp = None
    for d in data:
        if d['session_id'] == 2:
            resp = Response(str(d), status=200, mimetype='application/json')
            # resp = jsonify(d)
            # resp.status_code = 200
    if resp is None:
        message = {
            'status': 404,
            'message': 'Not Found ' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
    return resp


@app.route('/api/test', methods=['GET'])
def api_test():
    return '<h1>Hello from Flask...</h1>'
