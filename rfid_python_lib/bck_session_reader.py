import MFRC522
import signal
import requests
import time
import datetime

continue_reading = True
MIFAREReader = MFRC522.MFRC522()


def end_read(signal, frame):
    global continue_reading
    continue_reading = False
    print("Ctrl+C captured, ending read.")
    MIFAREReader.GPIO_CLEEN()


def post_tag_data(data):
    url = 'http://0.0.0.0:80/api/sessions/new'
    requests.post(url, json=data, headers={'Content-type': 'application/json'})
    print('Tag data posted to server...')


current_userId = -1
current_keyId = -1
current_userTTL = -1

signal.signal(signal.SIGINT, end_read)

print("Reader active and awaiting input...")

while continue_reading:
    if current_userTTL <= time.time() and not current_userId == -1:
        print("2 minutes elapsed.\nPlease register your ID card again...")
        current_userId = -1
        current_keyId = -1
        current_userTTL = -1
        continue
    (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    if status == MIFAREReader.MI_OK:
        print("Tag detected")
        (status, backData) = MIFAREReader.MFRC522_Anticoll()
        tag_data = int(str(backData[0]) + str(backData[1]) + str(backData[2]) + str(backData[3]) + str(backData[4]))
        if current_userId == -1 and len(str(tag_data)) == 13:
            current_userTTL = time.time() + 120
            current_userId = tag_data
            print("User ID: %s" % current_userId)
        elif current_keyId == -1 and len(str(tag_data)) == 12:
            current_keyId = tag_data
            print("Key ID: %s" % current_keyId)
        if current_keyId == current_userId:
            current_keyId = -1
            continue
        if current_keyId != current_userId and current_keyId > -1 and current_userId > -1:
            session = {
                'user_id': str(current_userId),
                'key_id': str(current_keyId),
                'timestamp': str(datetime.datetime.now())
            }
            post_tag_data(session)
            current_userId = -1
            current_keyId = -1
            current_userTTL = -1
            time.sleep(5)
