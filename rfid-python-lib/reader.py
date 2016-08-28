import os
import MFRC522
import signal

continue_reading = True
MIFAREReader = MFRC522.MFRC522()

dataStorePath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"data/tagReadings.txt")
if not os.path.isfile(dataStorePath):
    dataStore = open(dataStorePath, 'w')
    dataStore.close()

def end_read(signal, frame):
    global continue_reading
    continue_reading = False
    print "Ctrl+C captured, ending read."
    MIFAREReader.GPIO_CLEEN()

signal.signal(signal.SIGINT, end_read)

while continue_reading:
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    if status == MIFAREReader.MI_OK:
        print "Card detected"
    (status,backData) = MIFAREReader.MFRC522_Anticoll()
    if status == MIFAREReader.MI_OK:
        dataStore = open(dataStorePath, 'a')
        dataStore.write("Card read UID: "+str(backData[0])+","+str(backData[1])+","+str(backData[2])+","+str(backData[3])+","+str(backData[4])+"\n")
        dataStore.close()