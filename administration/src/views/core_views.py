from .. import app
from ..services.service_manager import ServiceManager
from ..services.storage_manager import StorageManager
from ..services.serializers import JSONSerializer as jserial
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
            print('Invalid JWT header: No authorization headers')
            raise Exception('Invalid JWT header: No authorization headers')
        header_parts = auth_header_value.split(' ')

        if header_parts[0].lower() != 'token':
            print('Invalid JWT header: Unsupported authorization type')
            raise Exception('Invalid JWT header: Unsupported authorization type')
        elif len(header_parts) == 1:
            print('Invalid JWT header: Token missing')
            raise Exception('Invalid JWT header: Token missing')
        elif len(header_parts) > 2:
            print('Invalid JWT header: Token contains spaces')
            raise Exception('Invalid JWT header: Token contains spaces')

        return '1%s' % header_parts[1]
    except Exception as e:
        print('Exception hit on get request auth')
        return '0%s' % repr(e)


def verify_token(token):
    return service_manager.validate_token(auth_token=token)


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
        print('Printing the token from get auth...')
        print(token)
        resp = jsonify(token)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return Response(e, status=404, mimetype='application/json')


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
