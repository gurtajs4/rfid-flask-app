import key_factory
import user_factory
import session_factory
from .db_seed import DbInitializer
from ..db import SqliteManager
from ..embedded.mfrc_service import ServiceMFRC
from ..io_sockets import reader_output, send_message


class ServiceManager(object):
    @staticmethod
    def start_db(drop_create=False):
        db = SqliteManager(drop_create)
        seed = DbInitializer()
        for session in seed.get_sessions():
            session_factory.create_session(user_id=session.user_id, key_id=session.key_id, timestamp=session.timestamp)

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
        print('Reader activated')
        data = reader.do_read()
        print('message from service manager: %s' % data['message'])
        return data
