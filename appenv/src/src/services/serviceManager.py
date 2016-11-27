import os
import json
from sessionRepository import SessionRepository
# from personRepository import PersonRepository
from mockService import UserService, KeyService


class ServiceManager(object):
    def __init__(self):
        data_storage_path = os.path.join(os.path.dirname  # /rfid-flask-app
                                         (os.path.dirname  # /rfid-flask-app/appenv
                                          (os.path.dirname  # /rfid-flask-app/appenv/src
                                           (os.path.dirname  # /rfid-flask-app/appenv/src/src
                                            (os.path.dirname  # /rfid-flask-app/appenv/src/src/services
                                             (os.path.abspath(__file__)))))), "data/")
        sessions_path = data_storage_path + "tagReadings.txt"
        users_path = data_storage_path + "people.txt"
        keys_path = data_storage_path + "keys.txt"
        mock_users_path = data_storage_path + "mockUsers.txt"
        mock_keys_path = data_storage_path + "mockKeys.txt"

        self.session_service = SessionRepository(data_storage_path=sessions_path)
        self.user_service = UserService(data_storage_path=mock_users_path)
        self.key_service = KeyService(data_storage_path=mock_keys_path)
