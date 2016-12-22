from .. import app
from ..services.service_manager import ServiceManager
from ..services.sqlite_manager import SqliteApiManager
from flask import jsonify, request, Response
from ..core import api_manager


# for model_name in app.config['API_MODELS']:
#     model_class = app.config['API_MODELS'][model_name]
#     api_manager.create_api(model_class, methods=['GET', 'POST'])

# api_session = api_manager.session
service_manager = ServiceManager()
sqlite_manager = SqliteApiManager()
# crud_url_models = app.config['CRUD_URL_MODELS']


@app.route('/', methods=['GET'])
def api_root():
    return app.send_static_file('index.html')


@app.route('/api/sessions', methods=['GET'])
def api_get_sessions():
    # data = service_manager.session_service.get_sessions()
    data = sqlite_manager.get_models('session')
    # data = crud_url_models['session']
    resp = jsonify(data)
    resp.status_code = 200
    return resp


@app.route('/api/sessions/<int:session_id>', methods=['GET'])
def api_get_session(session_id):
    # session = service_manager.session_service.get_session(session_id)
    session = sqlite_manager.get_single('session', session_id)
    # models_class = crud_url_models['session']
    # session = api_session.query(model_class).filter(models_class.id==session_id).first()
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


@app.route('/api/register/user', methods=['GET', 'POST'])
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


@app.route('/api/register/key', methods=['GET', 'POST'])
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
    user = service_manager.user_service.lookup_user(int(user_id))
    if user is None:
        is_found = False
    else:
        session = service_manager.map_user_to_session(user)
        is_found = False if (session is None) else True
    if not is_found:
        message = {
            'status': 404,
            'message': 'Not Found' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        resp = Response(str(session), status=200, mimetype='application/json')
        return resp


@app.route('/api/lookup/key/<int:key_id>', methods=['GET'])
def api_lookup_key(key_id):
    key = service_manager.key_service.lookup_key(int(key_id))
    if key is None:
        is_found = False
    else:
        session = service_manager.map_key_to_session(key)
        is_found = False if (session is None) else True
    if not is_found:
        message = {
            'status': 404,
            'message': 'Not Found' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        resp = Response(str(session), status=200, mimetype='application/json')
        return resp


@app.route('/api/lookup/user', methods=['GET'])
def api_lookup_users():
    users = service_manager.user_service.get_all()
    if len(users) > 0:
        resp = jsonify(users)
        resp.status_code = 200
        return resp
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
    keys = service_manager.key_service.get_all()
    if len(keys) > 0:
        resp = jsonify(keys)
        resp.status_code = 200
        return resp
    else:
        message = {
            'status': 404,
            'message': 'Not Found' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
