import os
import json
import xls_service
from ..models.models import Session
from ..config import DATA_DIR_PATH as data_store_path


class DbInitializer(object):
    def __init__(self):
        if not xls_service.template_exists():
            xls_service.make_template()

    def seed_from_excel(self, file):
        if None is not file and xls_service.template_exists(file):
            return xls_service.seed(file)
        else:
            return None

    def get_excel_template(self):
        return xls_service.get_template()

    def get_sessions_from_json(self, json_storage_path):
        if os.stat(json_storage_path).st_size > 0:
            with open(json_storage_path, 'r') as jsonStorage:
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
