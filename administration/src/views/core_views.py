from .. import app
from ..services.service_manager import ServiceManager
from ..services.storage_manager import StorageManager
from ..services.serializers import JSONSerializer as jserial
from flask import jsonify, request, Response, send_file

service_manager = ServiceManager()
ServiceManager.start_db(drop_create=False, seed_data=False, backup_data=False)


# *********** core app serving views ***********
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


@app.route('/door-lock', methods=['GET'])
def api_door_lock_root():
    return app.send_static_file('index2.html')


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
@app.route('/login', methods=['GET'])
@app.route('/users/register/', methods=['GET'])
@app.route('/user/search/', methods=['GET'])
@app.route('/user-details/', methods=['GET'])
@app.route('/users/edit/', methods=['GET'])
@app.route('/users', methods=['GET'])
@app.route('/keys/register/', methods=['GET'])
@app.route('/key/search/', methods=['GET'])
@app.route('/key-details/', methods=['GET'])
@app.route('/keys/edit/', methods=['GET'])
@app.route('/keys', methods=['GET'])
@app.route('/keys/seed', methods=['GET'])
@app.route('/sessions', methods=['GET'])
@app.route('/sessions/', methods=['GET'])
def api_root():
    return app.send_static_file('index.html')
