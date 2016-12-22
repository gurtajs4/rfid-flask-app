import os
import json


class MockService(object):
    def __init__(self, data_storage_path):
        self.data_storage_path = data_storage_path

    def get(self, chosen):
        size = os.stat(self.data_storage_path).st_size
        if size > 0:
            with open(self.data_storage_path, 'r') as mockData:
                for line in mockData:
                    if str(chosen) in line:
                        return line
        return None

    def get_all(self):
        size = os.stat(self.data_storage_path).st_size
        items = []
        if size > 0:
            with open(self.data_storage_path, 'r') as mockData:
                for line in mockData:
                        items.append(line)
        return items


class KeyService(MockService):
    def lookup_key(self, chosen):
        return super(KeyService, self).get(chosen)

    def get_all(self):
        return super(KeyService, self).get_all()


class UserService(MockService):
    def lookup_user(self, chosen):
        return super(UserService, self).get(chosen)

    def get_all(self):
        return super(UserService, self).get_all()
