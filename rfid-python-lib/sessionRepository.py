import json
from sessionInfo import SessionInfo

# method for hooking parsed json object into SessionInfo for usage in SessionRepository
def session_hook_handler(parsed_dict):
    return SessionInfo(sessionId=parsed_dict['sessionId'],
                       userId=parsed_dict['userId'],
                       timeStamp=parsed_dict['timeStamp'],
                       keyId=parsed_dict['keyId'])

# class that encapsulates session storage logic
class SessionRepository:

    # initialize SessionRepository object for managing session storage
    def __init__(self, dataStoragePath):
        self.dataStoragePath = dataStoragePath

    # methed for getting session from storage by sessionId
    def getSession(self, sessionId):
        with open(self.dataStoragePath, 'r') as jsonStorage:
            sessions = json.loads(jsonStorage.read())
            session = [value for key, value in sessions.iteritems() if value['sessionId'] == sessionId]
            return session_hook_handler(session)

    # method for getting all sessions from storage
    def getSessions(self):
        with open(self.dataStoragePath, 'r') as jsonStorage:
            sessionsRaw = json.loads(jsonStorage.read())
            sessions = []
            for key, value in sessionsRaw.iteritems():
                sessions.append(session_hook_handler(value))
            return sessions

    # method for storing a session into storage file
    def storeSession(self, session):
        with open(self.dataStoragePath, 'a') as jsonStorage:
            jsonStorage.write(json.dumps(session))
