from .. import app
from ..services.service_manager import ServiceManager
from ..services.serializers import JSONSerializer as jserial
from flask import jsonify, request, Response

service_manager = ServiceManager()


@app.route('/', methods=['GET'])
def api_root():
    ServiceManager.start_db(True)
    for session in service_manager.session_service.get_sessions():
        service_manager.create_session(user_id=session['_user_id'], key_id=session['_key_id'],
                                       timestamp=session['_time_stamp'])
    return app.send_static_file('index.html')


@app.route('/api/sessions', methods=['GET'])
def api_sessions_get():
    print('Hello from api-views')
    data = jserial.session_instances_serialize(service_manager.get_sessions())
    resp = jsonify(data)
    resp.status_code = 200
    return resp


@app.route('/api/sessions/<int:session_id>', methods=['GET'])
def api_session_get(session_id):
    session = jserial.session_instance_serialize(service_manager.get_session(session_id=session_id))
    if session is not None:
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
    if user.id > -1:
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
    if key.id > 0:
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
            'message': 'Not Found' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp


@app.route('/api/user/search/<int:user_id>', methods=['GET'])
def api_user_search(user_id):
    user = service_manager.get_user(user_id=user_id)
    if user is None:
        message = {
            'status': 404,
            'message': 'Not Found' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    else:
        data = jserial.user_instance_serialize(user_instance=user)
        resp = Response(data, status=200, mimetype='application/json')
        return resp


@app.route('/api/key/search/<int:key_id>', methods=['GET'])
def api_key_search(key_id):
    key = service_manager.get_key(key_id=int(key_id))
    if key is None:
        data=jserial.key_instance_serialize(key_instance=key)
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


# @app.route('/api/users/search', methods=['GET'])
# def api_users_search():
#     users = service_manager.user_service.get_all()
#     if len(users) > 0:
#         resp = jsonify(users)
#         resp.status_code = 200
#         return resp
#     else:
#         message = {
#             'status': 404,
#             'message': 'Not Found' + request.url,
#         }
#         resp = jsonify(message)
#         resp.status_code = 404
#         return resp
#
#
# @app.route('/api/key/search', methods=['GET'])
# def api_keys_search():
#     keys = service_manager.key_service.get_all()
#     if len(keys) > 0:
#         resp = jsonify(keys)
#         resp.status_code = 200
#         return resp
#     else:
#         message = {
#             'status': 404,
#             'message': 'Not Found' + request.url,
#         }
#         resp = jsonify(message)
#         resp.status_code = 404
#         return resp
