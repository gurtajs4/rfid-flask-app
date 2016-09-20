import os
import json
from sessionInfo import SessionInfo


# class that encapsulates session storage logic
class SessionRepository(object):

    # method for hooking parsed json object into SessionInfo for usage in SessionRepository
    @staticmethod
    def session_hook_handler(parsed_dict):
        return SessionInfo(session_id=parsed_dict['session_id'],
                           user_id=parsed_dict['user_id'],
                           time_stamp=parsed_dict['time_stamp'],
                           key_id=parsed_dict['key_id'])

    # initialize SessionRepository object for managing session storage
    def __init__(self, data_storage_path):
        self.data_storage_path = data_storage_path

    # method for getting session from storage by sessionId
    def get_session(self, session_id):
        if os.stat(self.data_storage_path).st_size > 0:
            with open(self.data_storage_path, 'r') as jsonStorage:
                sessions = [SessionRepository.session_hook_handler(line) for line in jsonStorage.readlines()]
                session = None
                for _session in sessions:
                    if _session.session_id == session_id:
                        session = _session
                return session
        return None

    # method for getting all sessions from storage
    def get_sessions(self):
        if os.stat(self.data_storage_path).st_size > 0:
            with open(self.data_storage_path, 'r') as jsonStorage:
                sessions = [SessionRepository.session_hook_handler(line) for line in jsonStorage.readlines()]
                return sessions
        return None

    # method for storing a session into storage file
    def store_session(self, session):
        with open(self.data_storage_path, 'a') as jsonStorage:
            json.dumps(session, jsonStorage)
            # jsonStorage.write(str(session))
            jsonStorage.write('\n')
            jsonStorage.flush()
            os.fsync(jsonStorage)
