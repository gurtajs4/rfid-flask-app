from .. import app
from ..services.service_manager import ServiceManager
from ..services.storage_manager import StorageManager
from ..services.serializers import JSONSerializer as jserial
from ..services.serializers import ImageB64Serializer as img64
from flask import jsonify, request, Response, send_file

service_manager = ServiceManager()


@app.route('/', methods=['GET'])
def api_root():
    ServiceManager.start_db(drop_create=False, seed_data=False, backup_data=False)
    return app.send_static_file('index.html')


@app.route('/door-lock', methods=['GET'])
def api_door_lock_root():
    ServiceManager.start_db(drop_create=False, seed_data=False, backup_data=False)
    return app.send_static_file('index2.html')


@app.route('/api/reader', methods=['GET'])
def api_reader():
    print('From server - reader init - reader called from client')
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
def api_users_get():
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
        print('From server - users - %s' % users)
        ui_models = [service_manager.get_user_ui_model(u) for u in users]
        print('From server - users - pic_url of first user is: %s' % ui_models[0].pic_url)
        data = jserial.user_instances_serialize(user_list=ui_models)
        resp = jsonify(data)
        resp.status_code = 200
        return resp


@app.route('/api/users/register', methods=['POST'])
def api_user_register():
    file = None
    files = request.files
    if 'file' in files:
        file = files['file']
    pic_url, pic_id = service_manager.upload_image(file)
    user_dict = jserial.json_deserialize(request.form['user_json'])
    print('From server - on image upload - JSON data: %s' % user_dict)
    user_dict = service_manager.create_user_dict(user_dict, pic_id[0])
    print('From server - user register (POST) - user json is %s' % user_dict)
    user = jserial.user_instance_deserialize(user_dict)
    print('From server - user register (POST) - user is %s' % user)
    user = service_manager.create_user(tag_id=user.tag_id,
                                       first_name=user.first_name,
                                       last_name=user.last_name,
                                       email=user.email,
                                       role_id=user.role_id,
                                       pic_id=user.pic_id)
    print('From server - api-user-register (post) - user from db is %s' % user)
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


@app.route('/api/users/search/<queryset>', methods=['GET'])
def api_users_search(queryset):
    words = [word for word in queryset.split(' ')]
    users = []
    for word in words:
        results = service_manager.search_user(first_name=word, last_name=word, limit=0)
        if None is not results:
            map(lambda x: users.append(x) if x.id not in [y.id for y in users] else False, results)
            users = sorted(users, key=lambda x: x.id)
    if None is users or 1 > len(users):
        message = {
            'status': 404,
            'message': 'Not Found - user you are searching for is not registered'
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        ui_models = [service_manager.get_user_ui_model(u) for u in users]
        data = jserial.user_instances_serialize(user_list=ui_models)
        print('From server - users search - users returned: %s' % data)
        resp = jsonify(data)
        resp.status_code = 200
        return resp


@app.route('/api/users/tag/search/<tag_id>', methods=['GET'])
def api_user_tag_search(tag_id):
    result = service_manager.search_user(tag_id=tag_id)
    if None is result:
        message = {
            'status': 404,
            'message': 'Not Found - user you are searching for is not registered'
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        user = service_manager.get_user_ui_model(result)
        data = jserial.user_instance_serialize(user_instance=user)
        resp = jsonify(data)
        resp.status_code = 200
        return resp


@app.route('/api/user/get/<int:user_id>', methods=['GET'])
def api_user_get(user_id):
    print('From server - user get - user id: %s' % user_id)
    user_data = service_manager.search_user(user_id=user_id, exclusive=True)
    if None is user_data:
        message = {
            'status': 404,
            'message': 'Not Found - user you are searching for is not registered'
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        user = service_manager.get_user_ui_model(user_data)
        data = jserial.user_instance_serialize(user)
        resp = jsonify(data)
        resp.status_code = 200
        return resp


@app.route('/api/user/delete/<int:user_id>', methods=['DELETE'])
def api_user_delete(user_id):
    print('From server - delete user %s' % user_id)
    if service_manager.delete_user(user_id=user_id):
        message = {
            'status': 200,
            'message': 'User deleted'
        }
    else:
        message = {
            'status': 404,
            'message': 'Not found'
        }
    resp = jsonify(message)
    resp.status_code = message['status']
    return resp


# *********** user auth requests ***********


@app.route('/api/user/auth-request', methods=['POST'])
def api_user_auth_request_new():
    user = (request.get_json())
    print('From server - received from reader - auth request: %s' % user)
    if None is not user:
        print('From server - user auth request - (user: %s, timestamp %s)' % (user['user_id'], user['timestamp']))
        user_session = service_manager.create_user_auth_request(user['user_id'], user['timestamp'])
        print("From server - user auth request - stored request: %s" % user_session)


@app.route('/api/user/auth-requests/<int:user_id>', methods=['GET'])
def api_user_auth_requests(user_id):
    sessions = service_manager.get_user_auth_requests(user_id=user_id)
    print('From server - user auth requests - requests count: %s' % len(sessions))
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


# *********** keys ***********


@app.route('/api/keys', methods=['GET'])
def api_keys_get():
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
        print('From server - keys - %s' % keys)
        data = jserial.key_instances_serialize(key_list=keys)
        resp = jsonify(data)
        resp.status_code = 200
        return resp


@app.route('/api/keys/register', methods=['POST'])
def api_key_register():
    key = jserial.key_instance_deserialize(request.get_json())
    key.room_repr = block_name + sector_name + floor + '-' + str(key.room_id)
    print('From server - key register - key tag is %s' % key.tag_id)
    print('From server - key register - key repr is %s' % key.room_repr)
    key = service_manager.create_key(tag_id=key.tag_id,
                                     room_id=key.room_id,
                                     block_name=key.block_name,
                                     sector_name=key.sector_name,
                                     floor=key.floor,
                                     room_repr=key.room_repr)
    print('From server - key register - stored key id is %s' % key.id)
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


@app.route('/api/keys/search/<queryset>', methods=['GET'])
def api_keys_search(queryset):
    print('From server - keys search - queryset is %s' % queryset)
    words = [word for word in queryset.split(' ')]
    keys = []
    for word in words:
        if word.isdigit():
            print('From server - keys search - keys count: %s' % len(keys))
            room_id = int(word)
            key = service_manager.search_key(room_id=room_id)
            if None is not key:
                if key.id not in [y.id for y in keys]:
                    keys.append(key)
                    print('From server - keys search - key found: %s' % key.room_id)
            print('From server - keys search - keys count: %s' % len(keys))
        else:
            print('From server - keys search - keys count: %s' % len(keys))
            key = service_manager.search_key(room_repr=word)
            if None is not key:
                if key.id not in [y.id for y in keys]:
                    keys.append(key)
                    print('From server - keys search - key found: %s' % key.room_id)
            print('From server - keys search - keys count: %s' % len(keys))
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
        print('From server - keys search - data is %s' % data)
        resp = jsonify(data)
        resp.status_code = 200
        return resp


@app.route('/api/keys/tag/search/<tag_id>', methods=['GET'])
def api_key_tag_search(tag_id):
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


@app.route('/api/key/get/<int:key_id>', methods=['GET'])
def api_key_get(key_id):
    key_data = service_manager.search_key(key_id=key_id, exclusive=True)
    if None is key_data:
        message = {
            'status': 404,
            'message': 'Not Found' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        data = jserial.key_instance_serialize(key_data)
        resp = jsonify(data)
        resp.status_code = 200
        return resp


@app.route('/api/key/delete/<int:key_id>', methods=['DELETE'])
def api_key_delete(key_id):
    print('From server - delete key %s' % key_id)
    if service_manager.delete_key(key_id=key_id):
        message = {
            'status': 200,
            'message': 'Key deleted'
        }
    else:
        message = {
            'status': 404,
            'message': 'Not found'
        }
    resp = jsonify(message)
    resp.status_code = message['status']
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
    session = jserial.session_instance_serialize(service_manager.search_session(session_id=session_id))
    print('From server - session get - (session_id: %s, session: %s)' % (session_id, session))
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


@app.route('/api/sessions/key/<int:key_id>', methods=['GET'])
def api_sessions_get_by_key(key_id):
    results = service_manager.search_session(key_id=key_id, limit=0)
    print('From server - sessions by key id - (key_id: %s, results: %s)' % (key_id, results))
    # send_message(results, 'key session result', session['uuid'])
    if None is not results:
        data = jserial.session_instances_serialize(session_list=results)
        resp = jsonify(data)
        resp.status_code = 200
    else:
        message = {'status': 404, 'message': 'Not Found'}
        resp = jsonify(message)
        resp.status_code = 404
    return resp


@app.route('/api/sessions/user/<int:user_id>', methods=['GET'])
def api_sessions_get_by_user(user_id):
    results = service_manager.search_session(user_id=user_id, limit=0)
    print('From server - sessions by user id - (user_id: %s, results: %s)' % (user_id, results))
    # service_manager.send
    if None is not results:
        data = jserial.session_instances_serialize(session_list=results)
        resp = jsonify(data)
        resp.status_code = 200
    else:
        message = {'status': 404, 'message': 'Not Found'}
        resp = jsonify(message)
        resp.status_code = 404
    return resp


@app.route('/api/sessions/new', methods=['POST'])
def api_session_new():
    data = request.get_json()
    print('From server - received from reader - session: %s' % data)
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
        data_deserialized = jserial.json_deserialize(data)
        print('From server - reader data deserialized: %s' % data_deserialized)
        print('From server - user id from data deserialized is %s' % data_deserialized['user_id'])
        user_id = int(data_deserialized['user_id'])
        user = service_manager.search_user(tag_id=user_id)
        print('From server - key id from data deserialized is %s' % data_deserialized['key_id'])
        key_id = int(data_deserialized['key_id'])
        key = service_manager.search_key(tag_id=key_id)
        session = None
        if None is key_id or '' == key_id or None is user_id or '' == user_id:
            print('Key ID or user ID not found so no session can be registered, retry...')
        elif None is user or None is key:
            session = None
        else:
            session = service_manager.search_session(user_id=user.id,
                                                     key_id=key.id,
                                                     exclusive=True,
                                                     is_active=True)
        print('From server - is existing session? %s' % (False if session is None else True))
        if None is not session:
            session.closed_on = data_deserialized['timestamp']
            service_manager.update_session(
                session.id, session.user_id, session.key_id, session.started_on, session.closed_on
            )
            print('From server - Session closed: %s user_id: %s key_id: %s started: %s closed: %s' % (
                session.id, session.user_id, session.key_id, session.started_on, session.closed_on
            ))
        else:
            if not (-1 == key_id or -1 == user_id):
                session = service_manager.create_session(user.id, key.id, data_deserialized['timestamp'])
                print('From server - data stored - id: %s user_id: %s key_id: %s started_on: %s' % (
                    session.id, session.user_id, session.key_id, session.started_on
                ))
        message['data'] = jserial.session_instance_serialize(session)
        resp = jsonify(message)
        resp.status_code = 200
        return resp


@app.route('/api/sessions/delete/<int:session_id>', methods=['DELETE'])
def api_session_delete(session_id):
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


# *********** file storage ***********


@app.route('/api/data/template', methods=['GET'])
def api_data_template():
    file = ServiceManager.get_excel_template()
    return send_file(file, mimetype='text/csv', attachment_filename='data_template.xls', as_attachment=True)


@app.route('/api/data/import', methods=['POST'])
def api_data_import():
    file = None
    files = request.files
    if 'file' in files:
        file = files['file']
    stm = StorageManager()
    file_path = stm.store_file(file=file, type=0)
    results = service_manager.seed_from_excel(file_location=file_path)
    if None is results or None is results[0].id:
        message = {
            'status': 404,
            'message': 'Unable to import data'
        }
    else:
        message = {
            'status': 200,
            'message': 'Successfully updated the database!'
        }
    resp = jsonify(message)
    resp.status_code = message['status']
    return resp


@app.route('/api/clean-slate', methods=['GET'])  # dev only
def api_clean_slate():
    if service_manager.start_db(drop_create=True, seed_data=True, backup_data=True):
        message = {
            'status': 200,
            'message': 'Successfully cleaned the database!'
        }
    else:
        message = {
            'status': 404,
            'message': 'Unable to backup data!'
        }
    resp = jsonify(message)
    resp.status_code = message['status']
    return resp
