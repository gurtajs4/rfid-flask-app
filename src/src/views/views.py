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


# *********** auth ***********


def get_request_auth(request):
    try:
        auth_header_value = request.headers.get('Authorization', None)
        if not auth_header_value:
            raise Exception('Invalid JWT header: No authorization headers')
        header_parts = auth_header_value.split(' ')

        if header_parts[0].lower() != 'token':
            raise Exception('Invalid JWT header: Unsupported authorization type')
        elif len(header_parts) == 1:
            raise Exception('Invalid JWT header: Token missing')
        elif len(header_parts) > 2:
            raise Exception('Invalid JWT header: Token contains spaces')

        return '1%s' % header_parts[1]
    except Exception as e:
        return '0%s' % repr(e)


def verify_token(token):
    return service_manager.validate_token(auth_token=token) is None


@app.route('/api/login', methods=['POST'])
def api_user_login():
    try:
        auth_data = request.get_json()
        email = auth_data['email']
        password = auth_data['password']
        print('Entered api login route on server side...')
        print('Email is %s' % email)
        print('Password is %s' % password)
        user_qs = service_manager.search_user(email=email, limit=1)
        if user_qs is None:
            raise Exception('User email not registered!')
        password_qs = service_manager.get_password(user_id=user_qs.id)
        if password_qs is None:
            raise Exception('User has not set the password yet!')
        user_auth = service_manager.check_password(password_qs, password)
        if user_auth is None:
            raise Exception('Incorrect password!')
        token = service_manager.generate_token(user=user_qs, password=password_qs)
        if token is None:
            raise Exception('Failed to generate a user token...')
        # TODO: generating csrf for http headers in ajax calls (during login)
        # csrf = service_manager.generate_csrf()
        # if csrf is None:
        #     raise Exception('Failed to generate a csrf token...')
        resp = jsonify(token)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return Response(e, status=404, mimetype='application/json')


# *********** users ***********


# <editor-fold desc="Users Views">


@app.route('/api/users', methods=['GET'])
def api_users_get():
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
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
        resp = jsonify(data)  # list of users - jsonify iterates over list
        resp.status_code = 200
        return resp


@app.route('/api/users/register', methods=['POST'])
def api_user_register():
    files = request.files
    if 'file' not in files:
        file = None
    else:
        file = files['file']
    pic_url, pic_id = service_manager.upload_image(file)
    user_dict = jserial.json_deserialize(request.form['user_json'])
    raw_password = user_dict['password']
    if raw_password is None:
        return Response(
            {'message': 'No password provided!', 'status': 404}, status=404, mimetype='application/json')
    else:
        password = service_manager.secure_password(raw_password=raw_password)  # creates secure password
    print('From server - on image upload - JSON data: %s' % user_dict)
    user_dict = jserial.create_user_dict(user_dict, pic_id)
    print('From server - user register (POST) - user json is %s' % user_dict)
    user = jserial.user_instance_deserialize(user_dict)
    print('From server - user register (POST) - user email is %s' % user.email)
    user = service_manager.create_user(tag_id=user.tag_id,
                                       first_name=user.first_name,
                                       last_name=user.last_name,
                                       email=user.email,
                                       password=password,
                                       role_id=user.role_id,
                                       pic_id=user.pic_id)
    if None is user or -1 == user.id:
        message = {
            'status': 404,
            'message': 'Not found - Unable to register user',
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        print('From server - api-user-register (post) - id of stored user is %s' % user.id)
        user_ui_model = service_manager.get_user_ui_model(user)
        data = jserial.user_instance_serialize(user_instance=user_ui_model)
        # user_data = jserial.user_instance_serialize(user_instance=user_ui_model)
        # token = service_manager.generate_token(user=user, password=password)
        # data = jserial.jwt_cookie_serialize(serialized_user_data=user_data, auth_token=token)
        # resp = Response(data, status=200, mimetype='application/json')
        resp = Response(data, status=200, mimetype='application/json')
        resp.status_code = 200
        return resp


@app.route('/api/users/search/<queryset>', methods=['GET'])
def api_users_search(queryset):
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
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
        resp = jsonify(data)  # list of users - so jsonify iterates over list
        resp.status_code = 200
        return resp


@app.route('/api/users/tag/search/<tag_id>', methods=['GET'])
def api_user_tag_search(tag_id):
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
    result = service_manager.search_user(tag_id=tag_id)
    if None is result:
        message = {
            'status': 404,
            'message': 'Not found - user you are searching for is not registered'
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        user = service_manager.get_user_ui_model(result)
        data = jserial.user_instance_serialize(user_instance=user)
        # resp = jsonify(data)
        resp = Response(data, status=200, mimetype='application/json')
        resp.status_code = 200
        return resp


@app.route('/api/user/get/<int:user_id>', methods=['GET'])
def api_user_get(user_id):
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
    user_data = service_manager.search_user(user_id=user_id, exclusive=True)
    if None is user_data:
        message = {
            'status': 404,
            'message': 'Not found - user you are searching for is not registered'
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        user = service_manager.get_user_ui_model(user_data)
        data = jserial.user_instance_serialize(user)
        resp = Response(data, status=200, mimetype='application/json')
        resp.status_code = 200
        return resp


@app.route('/api/user/delete/<int:user_id>', methods=['DELETE'])
def api_user_delete(user_id):
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
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


@app.route('/api/user/edit', methods=['PUT', 'POST'])
def user_edit():
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
    files = request.files
    if 'file' not in files:
        file = None
    else:
        file = files['file']
    pic_url, pic_id = service_manager.upload_image(file)
    user_dict = jserial.json_deserialize(request.form['user_json'])
    user_dict = jserial.create_user_dict(user_dict, pic_id)
    user = jserial.user_instance_deserialize(user_dict)
    user = service_manager.update_user(user_id=user.id,
                                       tag_id=user.tag_id,
                                       first_name=user.first_name,
                                       last_name=user.last_name,
                                       email=user.email,
                                       role_id=user.role_id,
                                       pic_id=user.pic_id)
    if None is user or -1 == user.id:
        message = {
            'status': 404,
            'message': 'Not Found'
        }
        resp = jsonify(message)
        resp.status_code = message['status']
    else:
        data = jserial.user_instance_serialize(user_instance=user)
        resp = Response(data, status=200, mimetype='application/json')
        resp.status_code = 200
    return resp


# </editor-fold>


# *********** user auth requests ***********


# <editor-fold desc="User Auth Views">


@app.route('/api/user/auth-request', methods=['POST'])
def api_user_auth_request_new():
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
    user = (request.get_json())
    if None is not user:
        user_session = service_manager.create_user_auth_request(user['user_id'], user['timestamp'])
        return jsonify(user_session)
    else:
        return Response('Faild action', status=404, mimetype='application/json')


@app.route('/api/user/auth-requests/<int:user_id>', methods=['GET'])
def api_user_auth_requests(user_id):
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
    sessions = service_manager.get_user_auth_requests(user_id=user_id)
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


# </editor-fold>


# *********** keys ***********


# <editor-fold desc="Keys Views">


@app.route('/api/keys', methods=['GET'])
def api_keys_get():
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
    keys = service_manager.get_keys()
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
        resp = jsonify(data)  # list of keys - jsonify iterates over list
        resp.status_code = 200
        return resp


@app.route('/api/keys/register', methods=['POST'])
def api_key_register():
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
    key = jserial.key_instance_deserialize(request.get_json())
    key = service_manager.create_key(tag_id=key.tag_id,
                                     room_id=key.room_id,
                                     block_name=key.block_name,
                                     sector_name=key.sector_name,
                                     floor=key.floor,
                                     room_repr=key.room_repr)
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
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
    words = [word for word in queryset.split(' ')]
    keys = []
    for word in words:
        pattern = int(word) if word.isdigit() else word
        print('From server - keys search - keys count: %s' % len(keys))
        results = service_manager.search_key(room_id=pattern,
                                             room_repr=pattern,
                                             block_name=pattern,
                                             sector_name=pattern,
                                             floor=pattern, limit=0)
        if None is not results:
            for key in results:
                if None is not key:
                    if key.id not in [y.id for y in keys]:
                        keys.append(key)
                        print('From server - keys search - key found: %s' % key.room_id)
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
        resp = jsonify(data)  # list of keys - jsonfiy iterates over list
        resp.status_code = 200
        return resp


@app.route('/api/keys/tag/search/<tag_id>', methods=['GET'])
def api_key_tag_search(tag_id):
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
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
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
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
        resp = Response(data, status=200, mimetype='application/json')
        resp.status_code = 200
        return resp


@app.route('/api/key/delete/<int:key_id>', methods=['DELETE'])
def api_key_delete(key_id):
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
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


@app.route('/api/key/edit', methods=['PUT', 'POST'])
def key_edit():
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
    key = jserial.key_instance_deserialize(request.get_json())
    key = service_manager.update_key(key_id=key.id,
                                     tag_id=key.tag_id,
                                     room_id=key.room_id,
                                     block_name=key.block_name,
                                     sector_name=key.sector_name,
                                     floor=key.floor,
                                     room_repr=key.room_repr)
    if None is key or -1 == key.id:
        message = {
            'status': 404,
            'message': 'Not found - Unable to edit key data',
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        data = jserial.key_instance_serialize(key_instance=key)
        resp = Response(data, status=200, mimetype='application/json')
        resp.status_code = 200
        return resp


# </editor-fold>


# *********** sessions ***********


# <editor-fold desc="Sessions Views">


@app.route('/api/sessions', methods=['GET'])
def api_sessions_get():
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
    raw_sessions = service_manager.get_sessions()
    sessions = []
    for session in raw_sessions:
        sessions.append(service_manager.get_session_ui_model(session=session))
    data = jserial.session_instances_serialize(session_list=sessions)
    if None is not data:
        resp = jsonify(data)
        resp.status_code = 200
    else:
        message = {'status': 404, 'message': 'Not Found'}
        resp = jsonify(message)  # list of sessions - jsonify iterates over list
        resp.status_code = 404
    return resp


@app.route('/api/sessions/<int:session_id>', methods=['GET'])
def api_session_get(session_id):
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
    session_raw = service_manager.search_session(session_id=session_id)
    if None is session_raw:
        message = {
            'status': 404,
            'message': 'Not Found' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        session = service_manager.get_session_ui_model(session=session_raw)
        data = jserial.session_instance_serialize(session_instance=session)
        resp = Response(data, status=200, mimetype='application/json')
        resp.status_code = 200
        return resp


@app.route('/api/sessions/key/<int:key_id>', methods=['GET'])
def api_sessions_get_by_key(key_id):
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
    results = service_manager.search_session(key_id=key_id, limit=0)
    if None is not results:
        sessions = [service_manager.get_session_ui_model(session=session) for session in results]
        data = jserial.session_instances_serialize(session_list=sessions)
        resp = jsonify(data)
        resp.status_code = 200
    else:
        message = {'status': 404, 'message': 'Not Found'}
        resp = jsonify(message)
        resp.status_code = 404
    return resp


@app.route('/api/sessions/user/<int:user_id>', methods=['GET'])
def api_sessions_get_by_user(user_id):
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
    results = service_manager.search_session(user_id=user_id, limit=0)
    if None is not results:
        sessions = [service_manager.get_session_ui_model(session) for session in results]
        data = jserial.session_instances_serialize(session_list=sessions)
        resp = jsonify(data)  # sessions of single user - jsonify iterates over list
        resp.status_code = 200
    else:
        message = {'status': 404, 'message': 'Not Found'}
        resp = jsonify(message)
        resp.status_code = 404
    return resp


@app.route('/api/sessions/new', methods=['POST'])
def api_session_new():
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
    data = request.get_json()
    if None is data:
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
        user_id = int(data_deserialized['user_id'])
        user = service_manager.search_user(tag_id=user_id)
        key_id = int(data_deserialized['key_id'])
        key = service_manager.search_key(tag_id=key_id)
        session = None
        if None is key_id or '' == key_id or None is user_id or '' == user_id:
            return Response('Key ID or user ID not found so no session can be registered, retry...', status=404,
                            mimetype='application/json')
        elif None is user or None is key:
            session = None
        else:
            session = service_manager.search_session(key_id=key.id,
                                                     user_id=user.id,
                                                     exclusive=True,
                                                     is_active=True)
        if None is not session:
            session.closed_on = data_deserialized['timestamp']
            service_manager.update_session(
                session.id, session.key_id, session.user_id, session.started_on, session.closed_on
            )
        else:
            if not (-1 == key_id or -1 == user_id):
                session = service_manager.create_session(key.id, user.id, data_deserialized['timestamp'])
        message['data'] = jserial.session_instance_serialize(service_manager.get_session_ui_model(session))
        resp = jsonify(message)
        resp.status_code = 200
        return resp


@app.route('/api/sessions/delete/<int:session_id>', methods=['DELETE'])
def api_session_delete(session_id):
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
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


# </editor-fold>


# *********** file storage ***********


# <editor-fold desc="File storage Views">

@app.route('/api/data/template', methods=['GET'])
def api_data_template():
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
    file = ServiceManager.get_excel_template()
    return send_file(file, mimetype='text/csv', attachment_filename='data_template.xls', as_attachment=True)


@app.route('/api/data/import', methods=['POST'])
def api_data_import():
    auth_data = get_request_auth(request=request)
    if auth_data[0] == '0':
        return jsonify(auth_data[1:])
    if not verify_token(auth_data[1:]):
        return Response('Login required', status=404, mimetype='application/json')
    file = None
    files = request.files
    if 'file' in files:
        file = files['file']
    stm = StorageManager()
    file_path = stm.store_file(file=file, type=0)
    check_location = service_manager.get_excel_template(filename=file.filename)
    results = service_manager.seed_from_excel(file_location=file_path)
    if None is results:
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

# </editor-fold>
