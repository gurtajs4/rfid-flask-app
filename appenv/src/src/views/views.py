from .. import app
from ..services.service_manager import ServiceManager
from ..services.serializers import JSONSerializer as jserial
from ..services.serializers import ImageB64Serializer as img64
from flask import jsonify, request, Response

service_manager = ServiceManager()


@app.route('/', methods=['GET'])
def api_root():
    ServiceManager.start_db(drop_create=False, seed_data=False)
    return app.send_static_file('index.html')


@app.route('/door-lock', methods=['GET'])
def api_door_lock_root():
    ServiceManager.start_db(drop_create=False, seed_data=False)
    return app.send_static_file('index2.html')


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
        print('Name of first user is %s' % users[0].first_name)
        ui_models = [service_manager.get_user_ui_model(u) for u in users]
        print('pic_url of first user in list is: %s' % ui_models[0].pic_url)
        data = jserial.user_instances_serialize(user_list=ui_models)
        resp = jsonify(data)
        resp.status_code = 200
        return resp


@app.route('/api/user/session', methods=['POST'])
def api_users_new():
    user = (request.get_json())
    print('Received user data from the reader...')
    if None is not user:
        print('User %s - timestamp %s' % (user['user_id'], user['timestamp']))
        user_session = service_manager.create_user_session(user['user_id'], user['timestamp'])
        print("User session stored as %s" % user_session)


@app.route('/api/user/sessions/<int:user_id>', methods=['GET'])
def api_user_sessions(user_id):
    sessions = service_manager.get_user_sessions(user_id=user_id)
    print('api-user-to-sessions count: %s' % len(sessions))
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
    file = None
    files = request.files
    if 'file' in files:
        file = files['file']
    pic_url, pic_id = service_manager.upload_image(file)
    # print('From server - on image upload - image id is: %s' % pic_id)
    # print('From server - on image upload - image url is: %s' % pic_url)
    # print('From server - user data is %s' % request.form['user_json'])
    user_dict = jserial.json_deserialize(request.form['user_json'])
    print('From server - on image upload - JSON data: %s' % user_dict)
    user_dict = service_manager.create_user_dict(user_dict, pic_id[0])
    print('From server - api-user-register(POST) - user json is %s' % user_dict)
    # user_json=jserial.user_instance_serialize(user_dict)
    user = jserial.user_instance_deserialize(user_dict)
    print('From server - api-user-register(POST) - user is %s' % user)
    user = service_manager.create_user(tag_id=user.tag_id,
                                       first_name=user.first_name,
                                       last_name=user.last_name,
                                       email=user.email,
                                       role_id=user.role_id,
                                       pic_id=user.pic_id)
    print('api-user-register is post: user from db is %s' % user)
    if None is user or -1 == user.id:
        message = {
            'status': 404,
            'message': 'Not Found - unable to register user',
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        data = jserial.user_instance_serialize(user_instance=user)
        resp = jsonify(data)
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
        # resp = Response(data, status=200, mimetype='application/json')
        resp = jsonify(data)
        resp.status_code = 200
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
        # resp = Response(data, status=200, mimetype='application/json')
        resp = jsonify(data)
        resp.status_code = 200
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
        print(keys)
        print('Id of first key in list is %s' % keys[0].id)
        data = jserial.key_instances_serialize(key_list=keys)
        # resp = Response(data, status=200, mimetype='application/json')
        resp = jsonify(data)
        resp.status_code = 200
        return resp


@app.route('/api/key/register', methods=['POST'])
def api_key_register():
    key = jserial.key_instance_deserialize(request.get_json())
    print('api-key-register: key tag is %s' % key.tag_id)
    key = service_manager.create_key(tag_id=key.tag_id, room_id=key.room_id)
    print('api-key-register: key from db has tag %s' % key.tag_id)
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
        resp.status_code = 200
        return resp


@app.route('/api/key/search/<int:room_id>', methods=['GET'])
def api_key_search(room_id):
    key = service_manager.search_key(room_id=int(room_id))
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
        resp = jsonify(data)
        resp.status_code = 200
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
        resp.status_code = 200
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
    print('api_get_key_session - by id %s - result is %s' % (key_id, result))
    send_message(result, 'key session result', session['uuid'])


@app.route('/api/sessions/new', methods=['POST'])
def api_session_new():
    data = request.get_json()
    print('Received new data from reader - session: %s' % data)
    if None is data:
        print('Data not received')
        message = {
            'status': 404,
            'message': 'Not Found' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        message = {
            'status': 200,
            'data': ''
        }
        print(type(data))
        user_id = -1
        key_id = -1
        # if 'user_id' in data:
        #     print(type(data['user_id']))
        #     print(data['user_id'])
        #     user_id = int(jserial.unicode_to_ascii(data['user_id']))
        # else:
        print(type(data[1]))
        print(data[1])
        user_id = int(jserial.unicode_to_ascii(data[1]))    # end of else
        print('From server - User ID is %s' % user_id)
        user = service_manager.search_user(tag_id=user_id)
        print('From server - user found %s' % user.first_name)
        # if 'key_id' in data:
        #     print(type(data['key_id']))
        #     print(data['key_id'])
        #     key_id = int(jserial.unicode_to_ascii(data['key_id']))
        # else:
        print(type(data[0]))
        print(data[0])
        key_id = int(jserial.unicode_to_ascii(data[0])) # end of else
        print('From server - Key ID is %s' % key_id)
        key = service_manager.search_key(tag_id=key_id)
        print('From server - key found with room id: %s' % key.room_id)
        session = None
        if -1 == key_id or -1 == user_id:
            print('Key ID or user ID not found so no session can be registered, retry...')
        else:
            session = service_manager.search_session(user_id=user.id, key_id=key.id, started_on=data[2])
        print('From server - is existing session? %s' % (False if session is None else True))
        if None is not session:
            session.closed_on = data[2]
            service_manager.update_session(
                session.id, session.user_id, session.key_id, session.started_on, session.closed_on
            )
            print('Session closed: %s user_id: %s key_id: %s started: %s closed: %s' % (
                session.id, session.user_id, session.key_id, session.started_on, session.closed_on
            ))
        else:
            if not (-1 == key_id or -1 == user_id):
                session = service_manager.create_session(user.id, key.id, data[2])
                print('Data stored - id: %s user_id: %s key_id: %s timestamp: %s' % (
                    session.id, session.user_id, session.key_id, session.started_on
                ))
        message['data'] = jserial.session_instance_serialize(session)
        resp = jsonify(message)
        resp.status_code = 200
        return resp


@app.route('/api/sessions/delete/<int:id>', methods=['DELETE'])
def api_delete_session(session_id):
    print('From server - delete session with id %s' % session_id)
    if service_manager.delete_session(session_id=session_id):
        message = {
            'status': 200,
            'message': 'Successfully deleted session'
        }
        resp = jsonify(message)
        resp.status_code = 200
        return resp
    else:
        message = {
            'status': 404,
            'message': 'Session not found'
        }
        resp = jsonify(message)
        resp.status_code = 200
        return resp
