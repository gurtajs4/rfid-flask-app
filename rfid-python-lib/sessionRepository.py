import json
import datetime
from sessionInfo import SessionInfo


# method for hooking parsed json object into SessionInfo for usage in SessionRepository
def session_hook_handler(parsed_dict):
    return SessionInfo(session_id=parsed_dict['session_id'],
                       user_id=parsed_dict['user_id'],
                       time_stamp=parsed_dict['time_stamp'],
                       key_id=parsed_dict['key_id'])


# class that provides JSON serialization of SessionInfo object (transforms it into dict)
class SessionEncoder(json.JSONEncoder):
    def default(self, o):
        if type(o) is datetime.datetime:
            return {"time_span": str(o)}
        return o.__dict__


# class that encapsulates session storage logic
class SessionRepository(object):

    # initialize SessionRepository object for managing session storage
    def __init__(self, data_storage_path):
        self.data_storage_path = data_storage_path

    # method for getting session from storage by sessionId
    def get_session(self, session_id):
        with open(self.data_storage_path, 'r') as jsonStorage:
            sessions = json.loads(jsonStorage)
            session = [value for key, value in sessions.iteritems() if value['session_id'] == session_id]
            return session_hook_handler(session)

    # method for getting all sessions from storage
    def get_sessions(self):
        with open(self.data_storage_path, 'r') as jsonStorage:
            sessions_raw = json.loads(jsonStorage)
            sessions = []
            for key, value in sessions_raw.iteritems():
                sessions.append(session_hook_handler(value))
            return sessions

    # method for storing a session into storage file
    def store_session(self, session):
        with open(self.data_storage_path, 'a') as jsonStorage:
            json.dumps(session, jsonStorage, cls=SessionEncoder)