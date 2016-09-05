import os
import stat
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
    os.stat(dataStorePath, stat.S_IRWXU)
    os.stat(dataStorePath, stat.S_IRGRP)
    os.stat(dataStorePath, stat.S_IWGRP)
    os.stat(dataStorePath, stat.S_IROTH)
    os.stat(dataStorePath, stat.S_IWOTH)


def end_read(signal, frame):
    global continue_reading
    continue_reading = False
    print "Ctrl+C captured, ending read."
    MIFAREReader.GPIO_CLEEN()


signal.signal(signal.SIGINT, end_read)

print "Reader active and awaiting input..."

while continue_reading:
    if current_userTTL == time.time():
        print "2 minutes elapsed.\nPlease register your ID card again..."
        current_userId = -1
        current_userTTL = -1
        continue
    (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    if status == MIFAREReader.MI_OK:
        print "Tag detected"
        (status, backData) = MIFAREReader.MFRC522_Anticoll()
        if not current_userId > 0:
            current_userTTL = time.time() + 120
            current_userId = int(
                str(backData[0]) + str(backData[1]) + str(backData[2]) + str(backData[3]) + str(backData[4]))
            print "User ID: " + str(current_userId)
        else:
            if backData != current_userId:
                key_id = int(
                    str(backData[0]) + str(backData[1]) + str(backData[2]) + str(backData[3]) + str(backData[4]))
                session = SessionInfo(session_id=last_sessionId,
                                      user_id=current_userId,
                                      time_stamp=datetime.datetime.now(),
                                      key_id=key_id)
                sessionService = SessionRepository(data_storage_path=dataStorePath)
                sessionService.store_session(session)
                current_userId = 0
                current_userTTL = 0
                print "Key ID: " + str(key_id)
