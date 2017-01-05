from .. import app
from ..services.service_manager import ServiceManager
from ..services.serializers import JSONSerializer as jserial
from flask import jsonify, request, Response

service_manager = ServiceManager()


@app.route('/', methods=['GET'])
def api_root():
    ServiceManager.start_db(drop_create=True, seed_data=True)
    return app.send_static_file('index.html')


@app.route('/api/sessions', methods=['GET'])
def api_sessions_get():
    data = jserial.session_instances_serialize(service_manager.get_sessions())
    if None is not data:
        resp = jsonify(data)
        resp.status_code = 200
    else:
        message = {'status': 404, 'message': 'Not Found'}
        resp = jsonify(message)
        resp.status_code = 404
    return resp


@app.route('/api/sessions/<int:session_id>', methods=['GET'])
def api_session_get(session_id):
    session = jserial.session_instance_serialize(service_manager.search_session(session_id=session_id))
    if None is not session:
        resp = jsonify(session)
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


@app.route('/api/sessions/new', methods=['POST'])
def api_session_new():
    data = request.data[0]
    if None is not session:
        session = service_manager.create_session(data['user_id'], data['key_id'], data['timestamp'])
        resp = jsonify(session)
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


@app.route('/api/reader', methods=['GET'])
def api_reader():
    print('Reader called from client')
    data = service_manager.init_reader()
    message = {
        'status': 200,
        'message': data
    }
    resp = jsonify(message)
    resp.status_code = message['status']
    return resp


@app.route('/api/user/register', methods=['POST'])
def api_user_register():
    user = jserial.user_instance_deserialize(request.data[0])
    user = service_manager.create_user(tag_id=user.tag_id, first_name=user.first_name, last_name=user.last_name,
                                       pic_url=user.pic_url)
    if None is not user and -1 < user.id:
        data = jserial.user_instance_serialize(user_instance=user)
        message = {
            'status': 200,
            'data': data
        }
        resp = jsonify(message)
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


@app.route('/api/key/register', methods=['POST'])
def api_key_register():
    key = jserial.key_instance_deserialize(request.data[0])
    key = service_manager.create_key(tag_id=key.tag_id, room_id=key.room_id)
    if None is not key and -1 < key.id:
        data = jserial.key_instance_serialize(key_instance=key)
        message = {
            'status': 200,
            'data': data
        }
        resp = jsonify(message)
        resp.status_code = 200
        return resp
    else:
        message = {
            'status': 404,
            'message': 'Not Found - unable to save the key',
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp


@app.route('/api/user/search/<user_name>', methods=['GET'])
def api_user_search(user_name):
    users = service_manager.search_user(first_name=user_name, last_name=user_name, limit=0)
    if None is user:
        message = {
            'status': 404,
            'message': 'Not Found - user you are searching for is not registered'
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        data = jserial.user_instances_serialize(user_list=users)  # .user_instance_serialize(user_instance=user)
        resp = Response(data, status=200, mimetype='application/json')
        return resp


@app.route('/api/key/search/<int:key_id>', methods=['GET'])
def api_key_search(key_id):
    key = service_manager.search_key(key_id=int(key_id))
    if None is key:
        data = jserial.key_instance_serialize(key_instance=key)
        resp = Response(data, status=200, mimetype='application/json')
        return resp
    else:
        message = {
            'status': 404,
            'message': 'Not Found' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
