import os
from .serializers import JSONSerializer as jserial
from ..config import sqlite_dir_path as data_store_path


# class that encapsulates session storage logic for managing session storage
class DbInitializer(object):
    def __init__(self):
        self.data_storage_path = os.path.join(data_store_path, "tagReadings.txt")

    # method for getting all sessions from storage
    def get_sessions(self):
        if os.stat(self.data_storage_path).st_size > 0:
            with open(self.data_storage_path, 'r') as jsonStorage:
                sessions = []
                for line in jsonStorage:
                    sessions.append(json.loads(line, cls=jserial.session_instance_deserialize))
                return sessions
        return None
