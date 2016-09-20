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
                for s in sessions:
                    if s.session_id == session_id:
                        return s
        return None

    # method for getting all sessions from storage
    def get_sessions(self):
        if os.stat(self.data_storage_path).st_size > 0:
            with open(self.data_storage_path, 'r') as jsonStorage:
                sessions = []
                for line in jsonStorage:
                    sessions.append(json.loads(line))
                return sessions
        return None

    # method for storing a session into storage file
    def store_session(self, session):
        with open(self.data_storage_path, 'a') as jsonStorage:
            jsonStorage.write(str(session))
            jsonStorage.write('\n')
            jsonStorage.flush()
            os.fsync(jsonStorage)
