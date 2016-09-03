# class for encapsulating RFID reader stored data logic
class SessionInfo(object):

    # initialize SessionInfo object
    def __init__(self, session_id, user_id, time_stamp, key_id=None):
        self._session_id = session_id
        self._user_id = user_id
        self._time_stamp = time_stamp
        if key_id is not None:
            self._key_id = key_id

    # unique identifier for reader session data
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        self._session_id = session_id

    # unique identifier for detected key tag in this session
    @property
    def key_id(self):
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        self._key_id = key_id

    # unique identifier for detected user data in this session
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    # date & time for this session
    @property
    def time_stamp(self):
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        self._time_stamp = time_stamp

