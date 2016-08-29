# class for encapsulating rfid reader stored data logic
class SessionInfo:

    # initialize SessionInfo object
    def __init__(self, sessionId, userId, timeStamp, keyId=None):
        self._sessionId = sessionId
        self._userId = userId
        self._timeStamp = timeStamp
        if keyId is not None:
            self._keyId = keyId

    # unique identifier for reader session data
    @property
    def sessionId(self):
        return self._sessionId

    @sessionId.setter
    def sessionId(self, sessionId):
        self._sessionId = sessionId

    # unique identifier for detected key tag in this session
    @property
    def keyId(self):
        return self._keyId

    @keyId.setter
    def tagId(self, keyId):
        self._keyId = keyId

    # unique identifier for detected user data in this session
    @property
    def userId(self):
        return self._userId

    @userId.setter
    def userId(self, userId):
        self._userId = userId

    # date & time for this session
    @property
    def timeStamp(self):
        return self._timeStamp

    @timeStamp
    def timeStamp(self, timeStamp):
        self._timeStamp = timeStamp

