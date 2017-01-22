from ..models.adapters import UserProfile
from ..db import SqliteManager
from .db_seed import DbInitializer
import key_factory
import user_factory
import session_factory
import user_session_factory
import images_service
from ..embedded.mfrc_service import ServiceMFRC
from ..io_sockets import reader_output, send_message


class ServiceManager(object):
    @staticmethod
    def start_db(drop_create=False, seed_data=False):
        db = SqliteManager(drop_create)
        if seed_data:
            seed = DbInitializer()
            for session in seed.get_sessions():
                user_factory.create_user(tag_id=session.user_id)
                user = user_factory.search_user(tag_id=session.user_id)
                if None is user:
                    pass
                key_factory.create_key(tag_id=session.key_id, room_id=session.key_id)
                key = key_factory.search_key(tag_id=session.key_id)
                if None is key:
                    pass
                session_factory.create_session(user_id=user.id, key_id=key.id, started_on=session.started_on)

    # api for keys
    @staticmethod
    def get_keys():
        return key_factory.get_keys()

    @staticmethod
    def search_key(key_id=None, tag_id=None, room_id=None, limit=1, exclusive=False):
        return key_factory.search_key(key_id, tag_id, room_id, limit, exclusive)

    @staticmethod
    def create_key(tag_id, room_id):
        return key_factory.create_key(tag_id, room_id)

    @staticmethod
    def delete_key(key_id=None, tag_id=None, room_id=None, delete_history=False):
        return key_factory.delete_key(key_id, tag_id, room_id, delete_history)

    @staticmethod
    def update_key(key_id, tag_id=None, room_id=None):
        return key_factory.delete_key(key_id, tag_id, room_id)

    # api for users
    @staticmethod
    def get_users():
        return user_factory.get_users()

    @staticmethod
    def search_user(user_id=None, tag_id=None, first_name=None, last_name=None, pic_url=None, limit=1, exclusive=False):
        return user_factory.search_user(user_id, tag_id, first_name, last_name, pic_url, limit, exclusive)

    @staticmethod
    def create_user(tag_id, first_name=None, last_name=None, pic_id=None):
        return user_factory.create_user(tag_id, first_name, last_name, pic_url)

    @staticmethod
    def delete_user(user_id, delete_history=False):
        return user_factory.delete_user(user_id, delete_history)

    @staticmethod
    def update_user(user_id, tag_id=None, first_name=None, last_name=None, pic_url=None):
        return user_factory.update_user(user_id, tag_id, first_name, last_name, pic_url)

    @staticmethod
    def create_user_json(user):
        pic_id = images_service.get_img_id(user['pic_url'])
        return {
            'id': -1,
            'tag_id': user['tag_id'],
            'first_name': user['first_name'],
            'last_name': user['last_name'],
            'email': user['email'],
            'role_id': user['role_id'],
            'pic_id': pic_id
        }

    @staticmethod
    def get_user_ui_model(user):
        pic_url = images_service.get_img_url(user.pic_id)
        return UserProfile(user.id, user.tag_id, user.first_name, user.last_name, user.email, user.role_id, pic_url)

    # api for sessions
    @staticmethod
    def get_sessions():
        return session_factory.get_sessions()

    @staticmethod
    def search_session(session_id=None, user_id=None, key_id=None, started_on=None, closed_on=None, limit=1,
                       exclusive=False):
        return session_factory.search_session(session_id, user_id, key_id, started_on, closed_on, limit, exclusive)

    @staticmethod
    def create_session(user_id=None, key_id=None, started_on=None):
        return session_factory.create_session(user_id, key_id, started_on)

    @staticmethod
    def delete_session(session_id=None, user_id=None, key_id=None, started_on=None, closed_on=None):
        return session_factory.delete_session(session_id, user_id, key_id, started_on, closed_on)

    @staticmethod
    def update_session(session_id, user_id=None, key_id=None, started_on=None, closed_on=None):
        return session_factory.update_session(session_id, user_id, key_id, started_on, closed_on)

    @staticmethod
    def create_user_session(user_id, timestamp):
        return user_session_factory.create_user_session(user_id=user_id, timestamp=timestamp)

    @staticmethod
    def get_user_sessions(user_id, limit=0):
        return user_session_factory.get_user_sessions(user_id=user_id, limit=limit)

    # api for matching
    @staticmethod
    def init_reader():
        reader = ServiceMFRC()
        print('From server - service manager - reader activated')
        data = reader.do_read()
        print('From server - service manager - reader message is %s' % data['message'])
        print('From server - service manager - tag data is %s' % data['data'])
        return data

    @staticmethod
    def upload_image(image):
        return images_service.save_img(image)
