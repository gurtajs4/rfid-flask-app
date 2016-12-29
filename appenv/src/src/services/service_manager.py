import os
import key_factory
import user_factory
import session_factory
from ..db import SqliteManager
from ..embedded.mfrc_service import ServiceMFRC
from session_repository import SessionRepository
from mock_service import UserService, KeyService


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

    @staticmethod
    def start_db():
        db = SqliteManager(True)

    # api for keys
    @staticmethod
    def get_keys():
        return key_factory.get_keys()

    @staticmethod
    def get_key(key_id=None, tag_id=None, room_id=None):
        return key_factory.get_key(key_id, tag_id, room_id)

    @staticmethod
    def create_key(tag_id=None, room_id=None):
        return key_factory.create_key(tag_id, room_id)

    # api for users
    @staticmethod
    def get_users():
        return user_factory.get_users()

    @staticmethod
    def get_user(user_id=None, tag_id=None, first_name=None, last_name=None, pic_url=None):
        return user_factory.get_user(user_id, tag_id, first_name, last_name, pic_url)

    @staticmethod
    def create_user(tag_id=None, first_name=None, last_name=None, pic_url=None):
        user_factory.create_user(tag_id, first_name, last_name, pic_url)

    # api for sessions
    @staticmethod
    def get_sessions():
        return session_factory.get_sessions()

    @staticmethod
    def get_session(session_id=None, user_id=None, key_id=None, timestamp=None):
        return session_factory.get_session(session_id, user_id, key_id, timestamp)

    @staticmethod
    def create_session(user_id=None, key_id=None, timestamp=None):
        session_factory.create_session(user_id, key_id, timestamp)

    # api for matching
    @staticmethod
    def init_reader():
        reader = ServiceMFRC()
        data = reader.do_read()
        return {
            'message': data['message'],
            'data': data['data'],
            'optional': 'message from service manager'
        }

    @staticmethod
    def do_read(callback):
        if callable(callable):
            return callable()
        else:
            return None
