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
                sessions = []
                for line in jsonStorage:
                    sessions.append(json.loads(line))
                session = [value for key, value in sessions.iteritems() if value['session_id'] == session_id]
                return SessionHandler.session_hook_handler(session)
        return None

    # method for getting all sessions from storage
    def get_sessions(self):
        if os.stat(self.data_storage_path).st_size > 0:
            with open(self.data_storage_path, 'r') as jsonStorage:
                sessions_raw = []
                for line in jsonStorage:
                    sessions_raw.append(json.loads(line))
                sessions = []
                for key, value in sessions_raw.iteritems():
                    sessions.append(SessionHandler.session_hook_handler(value))
                return sessions
        return None

    # method for storing a session into storage file
    def store_session(self, session):
        with open(self.data_storage_path, 'a') as jsonStorage:
            json.dump(session, jsonStorage)
            jsonStorage.write('\n')
            jsonStorage.flush()
            os.fsync(jsonStorage)
