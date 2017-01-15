from .. import app
from ..services.service_manager import ServiceManager
from ..services.serializers import JSONSerializer as jserial
from flask import jsonify, request, Response

service_manager = ServiceManager()


@app.route('/', methods=['GET'])
def api_root():
    ServiceManager.start_db(drop_create=True, seed_data=False)
    return app.send_static_file('index.html')


@app.route('/api/reader', methods=['GET'])
def api_reader():
    print('Reader called from client')
    data = service_manager.init_reader()
    message = {
        'status': 404 if data['data'] == '00000000' else 200,
        'message': data['message'],
        'data': data['data']
    }
    resp = jsonify(message)
    resp.status_code = message['status']
    return resp


# *********** users ***********


@app.route('/api/users', methods=['GET'])
def api_users():
    users = service_manager.get_users()
    if None is users or 1 > len(users):
        message = {
            'status': 404,
            'message': 'Not Found - no users found',
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        print(users)
        # data = jserial.user_instances_serialize(user_list=users)
        # resp = Response(data, status=200, mimetype='application/json')
        resp = jsonify(users)
        resp.status_code = 200
        return resp


@app.route('/api/user/session', methods=['POST'])
def api_users_new():
    user = (request.get_json())
    print('Received user data from the reader...')
    if None is not user:
        print('User %s - timestamp %s' % (user['user_id'], user['timestamp']))
        user_session = service_manager.create_user_session(user['user_id'], user['timestamp'])
        print("User session stored as %s"%user_session)


@app.route('/api/user/sessions/<int:user_id>', methods=['GET'])
def api_user_sessions(user_id):
    sessions=service_manager.get_user_sessions(user_id=user_id)
    print('api-user-sessions count: %s' % len(sessions))
    if None is sessions:
        message = {
            'status': 404,
            'message': 'Not Found - no sessions for the selected user were found',
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        print(sessions)
        resp = jsonify(sessions)
        resp.status_code = 200
        return resp


@app.route('/api/user/register', methods=['POST'])
def api_user_register():
    user = jserial.user_instance_deserialize(request.get_json())
    print('api-user-register is post: user %s' % user)
    user = service_manager.create_user(tag_id=user.tag_id, first_name=user.first_name, last_name=user.last_name,
                                       pic_url=user.pic_id)
    print('api-user-register is post: user from db is %s' % user)
    if None is user or -1 == user.id:
        message = {
            'status': 404,
            'message': 'Not Found' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        # data = jserial.user_instance_serialize(user_instance=user)
        # resp = Response(data, status=200, mimetype='application/json')
        resp = jsonify(user)
        resp.status_code = 200
        return resp


@app.route('/api/user/search/<user_name>', methods=['GET'])
def api_user_search(user_name):
    users = service_manager.search_user(first_name=user_name, last_name=user_name, limit=0)
    if None is users or 1 > len(users):
        message = {
            'status': 404,
            'message': 'Not Found - user you are searching for is not registered'
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        data = jserial.user_instances_serialize(user_list=users)
        resp = Response(data, status=200, mimetype='application/json')
        return resp


@app.route('/api/user/tag/search/<tag_id>', methods=['GET'])
def api_user_id_search(tag_id):
    user = service_manager.search_user(tag_id=tag_id)
    if None is user:
        message = {
            'status': 404,
            'message': 'Not Found - user you are searching for is not registered'
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        data = jserial.user_instance_serialize(user_instance=user)
        resp = Response(data, status=200, mimetype='application/json')
        return resp


# *********** keys ***********


@app.route('/api/keys', methods=['GET'])
def api_keys():
    keys = service_manager.get_keys()
    print(keys)
    if None is keys or 1 > len(keys):
        message = {
            'status': 404,
            'message': 'Not Found' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        data = jserial.key_instances_serialize(key_list=keys)
        # resp = Response(data, status=200, mimetype='application/json')
        resp = jsonify(data)
        resp.status_code = 200
        return resp


@app.route('/api/key/register', methods=['POST'])
def api_key_register():
    key = jserial.key_instance_deserialize(request.get_json())
    print('api-key-register: key %s' % key)
    key = service_manager.create_key(tag_id=key.tag_id, room_id=key.room_id)
    print('api-key-register: key from db is %s' % key)
    if None is key or -1 == key.id:
        message = {
            'status': 404,
            'message': 'Not Found - unable to save the key',
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        data = jserial.key_instance_serialize(key_instance=key)
        resp = Response(data, status=200, mimetype='application/json')
        return resp


@app.route('/api/key/search/<int:key_id>', methods=['GET'])
def api_key_search(key_id):
    key = service_manager.search_key(key_id=int(key_id))
    if None is key:
        message = {
            'status': 404,
            'message': 'Not Found' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        data = jserial.key_instance_serialize(key_instance=key)
        resp = Response(data, status=200, mimetype='application/json')
        return resp


@app.route('/api/key/tag/search/<tag_id>', methods=['GET'])
def api_key_id_search(tag_id):
    key = service_manager.search_key(tag_id=int(tag_id))
    if None is key:
        message = {
            'status': 404,
            'message': 'Not Found' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        data = jserial.key_instance_serialize(key_instance=key)
        resp = Response(data, status=200, mimetype='application/json')
        return resp


# *********** sessions ***********


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
    print('Received session id: %s - parameter for session query' % session_id)
    session = jserial.session_instance_serialize(service_manager.search_session(session_id=session_id))
    print('Server retrieving session object: %s' % session)
    if None is session:
        message = {
            'status': 404,
            'message': 'Not Found' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        resp = jsonify(session)
        resp.status_code = 200
        return resp


@app.route('/api/session/key/<int:key_id>')
def api_get_key_session(key_id):
    print('Received %s from client' % key_id)
    result = service_manager.search_session(key_id=key_id)
    print('api_get_key_session - by id %s - result is %s' % key_id, result)
    send_message(result, 'key session result', session['uuid'])


@app.route('/api/sessions/new', methods=['POST'])
def api_session_new():
    data = request.get_json()
    print('Received new data from reader - session: %s' % data)
    if None is data:
        message = {
            'status': 404,
            'message': 'Not Found - incorrect request data',
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        session = service_manager.create_session(data['user_id'], data['key_id'], data['timestamp'])
        resp = jsonify(session)
        resp.status_code = 200
        return resp
