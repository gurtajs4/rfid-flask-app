from .. import app
import os
from ..services.serviceManager import ServiceManager
# from ..services.sessionRepository import SessionRepository
# from ..services.mockService import UserService, KeyService
from flask import jsonify
from flask import request
from flask import Response


# data_storage_path = os.path.join(os.path.dirname  # /rfid-flask-app
#                                  (os.path.dirname  # /rfid-flask-app/appenv
#                                   (os.path.dirname  # /rfid-flask-app/appenv/src
#                                    (os.path.dirname  # /rfid-flask-app/appenv/src/src
#                                     (os.path.dirname  # /rfid-flask-app/appenv/src/src/views
#                                      (os.path.abspath(__file__)))))), "data/")
# sessions_path = data_storage_path + "tagReadings.txt"
# mock_users_path = data_storage_path + "mockUsers.txt"
# mock_keys_path = data_storage_path + "mockKeys.txt"
#
# session_service = SessionRepository(data_storage_path=sessions_path)
# user_service = UserService(data_storage_path=mock_users_path)
# key_service = KeyService(data_storage_path=mock_keys_path)
service_manager = ServiceManager()


@app.route('/', methods=['GET'])
def api_root():
    return app.send_static_file('index.html')


@app.route('/api/sessions', methods=['GET'])
def api_get_sessions():
    # data = session_service.get_sessions()
    data = service_manager.session_service.get_sessions()
    resp = jsonify(data)
    resp.status_code = 200
    return resp


@app.route('/api/sessions/<int:session_id>', methods=['GET'])
def api_get_session(session_id):
    # session = session_service.get_session(session_id)
    session = service_manager.session_service.get_session(session_id)
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
    user_id = "2271223943149"   # mock id --> this is where another service will be called to obtain true user id
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
    key_id = "221404673253"   # mock id --> this is where another service will be called to obtain true key id
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


@app.route('/api/lookup/user/<int:user_id>', methods=['GET'])
def api_lookup_user(user_id):
    # user = user_service.lookup_user(user_id)
    user = service_manager.user_service.lookup_user(user_id)
    if user is None:
        message = {
            'status': 404,
            'message': 'Not Found' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        return user


@app.route('/api/lookup/key/<int:key_id>', methods=['GET'])
def api_lookup_key(key_id):
    # key = key_service.lookup_key(key_id)
    key = service_manager.key_service.lookup_key(key_id)
    if key is None:
        message = {
            'status': 404,
            'message': 'Not Found' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        return key


@app.route('/api/lookup/user', methods=['GET'])
def api_lookup_users():
    # users = user_service.get_all()
    users = service_manager.user_service.get_all()
    if users.count() > 0:
        return users
    else:
        message = {
            'status': 404,
            'message': 'Not Found' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp


@app.route('/api/lookup/key', methods=['GET'])
def api_lookup_keys():
    # keys = key_service.get_all()
    keys = service_manager.key_service.get_all()
    if keys.count() > 0:
        return keys
    else:
        message = {
            'status': 404,
            'message': 'Not Found' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
