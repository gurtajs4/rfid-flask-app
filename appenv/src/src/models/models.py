class Key:
    def __init__(self, key_id, tag_id, room_id):
        self.id = key_id
        self.tag_id = tag_id
        self.room_id = room_id


class User:
    def __init__(self, user_id, tag_id, first_name, last_name, email, role_id, pic_id):
        self.id = user_id
        self.tag_id = tag_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.role_id = role_id
        self.pic_id = pic_id


class Session:
    def __init__(self, session_id, user_id, key_id, timestamp):
        self.id = session_id
        self.user_id = user_id
        self.key_id = key_id
        self.timestamp = timestamp
