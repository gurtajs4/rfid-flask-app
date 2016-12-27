import json
import datetime
import base64
from ..models.models import Session, User, Key


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if type(o) is datetime.datetime:
            return str(o)
        elif type(o) is str and len(o) > 100:
            return base64.b64decode(o)
        return o.__dict__


class ApiJSONEncoder(object):
    @staticmethod
    def session_json_decode(parsed_dict):
        return Session(id=parsed_dict['id'],
                       user_id=parsed_dict['user_id'],
                       key_id=parsed_dict['key_id'],
                       timestamp=parsed_dict['timestamp'])

    @staticmethod
    def session_json_encode(model_class):
        return json.dumps(model_class, cls=CustomJSONEncoder)

    @staticmethod
    def user_json_decode(parsed_dict):
        return User(id=parsed_dict['id'],
                    tag_id=parsed_dict['tag_id'],
                    first_name=parsed_dict['first_name'],
                    last_name=parsed_dict['last_name'],
                    profile_pic=parsed_dict['profile_pic'])

    @staticmethod
    def user_json_encode(model_class):
        return json.dumps(model_class, cls=CustomJSONEncoder)

    @staticmethod
    def key_json_decode(parsed_dict):
        return Key(id=parsed_dict['id'],
                   tag_id=parsed_dict['tag_id'],
                   room_id=parsed_dict['room_id'])

    @staticmethod
    def key_json_encode(model_class):
        return json.dumps(model_class, cls=CustomJSONEncoder)
