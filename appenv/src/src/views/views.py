from .. import app
import os
from ..services.sessionRepository import SessionRepository
from flask import jsonify
from flask import request
from flask import Response


data_storage_path = os.path.join(os.path.dirname  # /rfid-flask-app
                                 (os.path.dirname  # /rfid-flask-app/appenv
                                  (os.path.dirname  # /rfid-flask-app/appenv/src
                                   (os.path.dirname  # /rfid-flask-app/appenv/src/src
                                    (os.path.dirname  # /rfid-flask-app/appenv/src/src/views
                                     (os.path.abspath(__file__)))))), "data/tagReadings.txt")

_service = SessionRepository(data_storage_path=data_storage_path)


@app.route('/', methods=['GET'])
def api_root():
    return app.send_static_file('index.html')


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
        return resp
    else:
        message = {
            'status': 404,
            'message': 'Not Found' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp


@app.route('/api/register/user', methods=['GET'])
def api_register_user():
    user_id = 2271223943149   # mock id --> this is where another service will be called to obtain true user id
    if user_id is not None and user_id > -1:
        return user_id
    else:
        message = {
            'status': 404,
            'message': 'Not Found' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp


@app.route('/api/register/key', methods=['GET'])
def api_register_key():
    key_id = 221404673253   # mock id --> this is where another service will be called to obtain true key id
    if key_id is not None and key_id > -1:
        return key_id
    else:
        message = {
            'status': 404,
            'message': 'Not Found' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
