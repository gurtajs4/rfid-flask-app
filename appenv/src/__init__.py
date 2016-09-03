import os
from models.sessionInfo import SessionInfo
from services.sessionRepository import SessionRepository
from flask import Flask, url_for
from flask import jsonify
from flask import Response


data_root_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "data")


_service = SessionRepository(data_storage_path=data_root_path)
app = Flask(__name__)


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
    return jsonify(_tag)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
