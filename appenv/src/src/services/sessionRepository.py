import os
import json
from sessionHandler import SessionHandler


# class that encapsulates session storage logic
class SessionRepository(object):
    # initialize SessionRepository object for managing session storage
    def __init__(self, data_storage_path):
        self.data_storage_path = data_storage_path

    # method for getting session from storage by sessionId
    def get_session(self, session_id):
        if os.stat(self.data_storage_path).st_size > 0:
            with open(self.data_storage_path, 'r') as jsonStorage:
                sessions = json.loads(jsonStorage.read())
                session = [value for key, value in sessions.iteritems() if value['session_id'] == session_id]
                return SessionHandler.session_hook_handler(session)
        return None

    # method for getting all sessions from storage
    def get_sessions(self):
        if os.stat(self.data_storage_path).st_size > 0:
            with open(self.data_storage_path, 'r') as jsonStorage:
                sessions_raw = json.loads(jsonStorage.read())
                sessions = []
                for key, value in sessions_raw.iteritems():
                    sessions.append(SessionHandler.session_hook_handler(value))
                return sessions
        return None

    # method for storing a session into storage file
    def store_session(self, session):
        sessions_raw = self.get_sessions()
        sessions = [] if sessions_raw is None else sessions_raw
        with open(self.data_storage_path, 'w') as jsonStorage:
            json.dumps(sessions, jsonStorage)
            jsonStorage.flush()
            os.fsync(jsonStorage)
