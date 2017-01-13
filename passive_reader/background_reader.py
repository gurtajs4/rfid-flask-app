from ..rfid_python_lib import MFRC522
import signal
import requests
import time
import datetime

continue_reading = True
MIFAREReader = MFRC522.MFRC522()


def end_read(signal, frame):
    global continue_reading
    continue_reading = False
    print "Ctrl+C captured, ending read."
    MIFAREReader.GPIO_CLEEN()


def post_tag_data(data):
    url = 'http://0.0.0.0:80/api/sessions/new'
    r = requests.post(url, data)
    if r.status_code == requests.codes.ok or r.status_code == 200:
        print('Tag data posted to server...')
        print(r.text)


current_userId = -1
current_userTTL = -1

signal.signal(signal.SIGINT, end_read)

print "Reader active and awaiting input..."

while continue_reading:
    if current_userTTL <= time.time() and not current_userId == -1:
        print "2 minutes elapsed.\nPlease register your ID card again..."
        current_userId = -1
        current_userTTL = -1
        continue
    (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    if status == MIFAREReader.MI_OK:
        print "Tag detected"
        (status, backData) = MIFAREReader.MFRC522_Anticoll()
        if current_userId == -1:
            current_userTTL = time.time() + 120
            current_userId = int(
                str(backData[0]) + str(backData[1]) + str(backData[2]) + str(backData[3]) + str(backData[4]))
            print "User ID: " + str(current_userId)
        else:
            if backData != current_userId:
                key_id = int(
                    str(backData[0]) + str(backData[1]) + str(backData[2]) + str(backData[3]) + str(backData[4]))
                if key_id != current_userId:
                    session = {
                        'user_id': str(current_userId),
                        'key_id': str(key_id),
                        'timestamp': datetime.datetime.now()
                    }
                    post_tag_data(session)
                    current_userId = -1
                    current_userTTL = -1
                    print "Key ID: " + str(key_id)
                    time.sleep(5)
