import os
from models.sessionInfo import SessionInfo
from services.sessionRepository import session_hook_handler
from services.sessionRepository import SessionRepository
from flask import json
from flask import Response
from flask import Flask, url_for


data_root_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "data")


_service = SessionRepository(data_storage_path=data_root_path)
app = Flask(__name__)


@app.route('/api', methods=['GET'])
def api_root():
    return 'Welcome'


@app.route('/api/sessions', methods=['GET'])
def api_get_sessions():
    # return 'Listing all tagged info: '+str(_service.get_sessions())
    return json.dumps(_service.api_get_sessions())


@app.route('/api/sessions/<tagid>', methods=['GET'])
def api_get_session(tagid):
    _tag_raw = _service(tagid)
    _tag = session_hook_handler(_tag_raw)
    return json.dumps(_tag)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
