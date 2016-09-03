from .. import app
# import os
from .... import data_storage_path
from ..services.sessionRepository import SessionRepository
from flask import jsonify


# data_root_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "data")
data_store_path = data_storage_path


_service = SessionRepository(data_storage_path=data_store_path)


@app.route('/api', methods=['GET'])
def api_root():
    return 'Welcome'


@app.route('/api/sessions', methods=['GET'])
def api_get_sessions():
    resp = jsonify(_service.get_sessions())
    resp.status_code = 200
    return resp


@app.route('/api/sessions/<tagid>', methods=['GET'])
def api_get_session(tagid):
    _tag = _service.get_session(tagid)
    resp = jsonify(_tag)
    resp.status_code = 200
    return resp