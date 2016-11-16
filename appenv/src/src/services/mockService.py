import os
import random
import json


class MockService(object):
    def __init__(self, data_storage_path):
        self.data_storage_path = data_storage_path

    def get_id(self):
        size = os.stat(self.data_storage_path).st_size
        if size > 0:
            with open(self.data_storage_path, 'r') as mockData:
                i = 0
                chosen = random.randint(1, size)
                for line in mockData:
                    i += 1
                    if i == chosen:
                        return line
        return None

    def lookup_id(self, chosen):
        size = os.stat(self.data_storage_path).st_size
        if size > 0:
            with open(self.data_storage_path, 'r') as mockData:
                i = 0
                for line in mockData:
                    i += 1
                    if i == chosen:
                        return line
        return None


class KeyService(MockService):
    def get_kid(self):
        return super(KeyService, self).get_id()

    def lookup_key(self, chosen):
        return super(KeyService, self).lookup_id(chosen)


class UserService(MockService):
    def get_uid(self):
        return super(UserService, self).get_id()

    def lookup_user(self, chosen):
        return super(UserService, self).lookup_id(chosen)
