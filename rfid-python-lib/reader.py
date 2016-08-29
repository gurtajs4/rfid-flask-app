import os
import time
import datetime
import MFRC522
import signal
from sessionRepository import SessionRepository
from sessionInfo import SessionInfo


continue_reading = True
MIFAREReader = MFRC522.MFRC522()
last_sessionId = 0
current_userId = 0
current_userTTL = 0


dataStorePath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data/tagReadings.txt")
if not os.path.isfile(dataStorePath):
    with open(dataStorePath, 'w') as dataStore:
        dataStore.write('')


def end_read(signal, frame):
    global continue_reading
    continue_reading = False
    print "Ctrl+C captured, ending read."
    MIFAREReader.GPIO_CLEEN()

signal.signal(signal.SIGINT, end_read)

while continue_reading:
    (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    if status == MIFAREReader.MI_OK:
        print "Tag detected"
        (status, backData) = MIFAREReader.MFRC522_Anticoll()
        if current_userId > 0:
            if backData != current_userId:
                session = SessionInfo(last_sessionId, current_userId, datetime.datetime.now(), int(backData))
                sessionService = SessionRepository(data_storage_path=dataStorePath)
                sessionService.store_session(session)
                current_userId = 0
                current_userTTL = 0
        else:
            current_userTTL = time.time() + 120
            current_userId = int(backData)
    if current_userTTL == time.time():
        print "2 minutes elapsed.\nPlease register your ID card again..."
        current_userId = 0
        current_userTTL = 0

