import os
import json
from ..models.models import Session
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
                    parsed_dict = json.loads(line)
                    session = Session(session_id=0,
                                      user_id=parsed_dict['user_id'],
                                      key_id=parsed_dict['key_id'],
                                      started_on=parsed_dict['started_on'],
                                      closed_on=parsed_dict['closed_on'])
                    sessions.append(session)
                return sessions
        return None
