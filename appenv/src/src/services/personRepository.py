import os
import json
from ..models.userInfo import UserInfo, UserEncoder


class PersonRepository(object):

    def __init__(self, data_storage_path):
        self.data_storage_path = data_storage_path

    def get_person(self, user_id):
        if os.stat(self.data_storage_path).st_size > 0:
            with open(self.data_storage_path, 'r') as jsonStorage:
                people = []
                for line in jsonStorage:
                    people.append(json.loads(line))
                for p in people:
                    person = UserInfo(p)
                    if person.user_id == user_id:
                        return person
        return None

    def get_people(self):
        if os.stat(self.data_storage_path).st_size > 0:
            with open(self.data_storage_path, 'r') as jsonStorage:
                people = []
                for line in jsonStorage:
                    people.append(json.loads(line))
                return people
        return None

    def add_person(self, person):
        with open(self.data_storage_path, 'a') as jsonStorage:
            jsonStorage.write(str(person))
            jsonStorage.write('\n')
            jsonStorage.flush()
            os.fsync(jsonStorage)
