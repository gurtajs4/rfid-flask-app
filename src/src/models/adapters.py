import models


class UserProfile:
    def __init__(self, user_id, tag_id, first_name, last_name, email, role_id, pic_url):
        self.user_id = user_id
        self.tag_id = tag_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.role_id = role_id
        self.role_title = 'Professor' if role_id == 1 else 'Student'
        self.pic_url = pic_url

# class SessionInfo:
#     def __init__(self, session_id, user_id, key_id, started_on, closed_on, room_repr):
#         self.id = session_id
#         self.user_id = user_id
#         self.key_id = key_id
#         self.started_on = started_on
#         self.closed_on = closed_on
#         self.room_repr = room_repr
