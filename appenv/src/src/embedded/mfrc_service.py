def load_src(name, fdir, fpath):
    import os, imp
    return imp.load_source(name,
                           os.path.join(os.path.dirname(
                               os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))),
                               fdir, fpath))


load_src("MFRC522", "rfid-python-lib", "MFRC522.py")
import MFRC522


class ServiceMFRC:
    def __init__(self):
        self.continue_reading = True
        self.MIFAREReader = MFRC522.MFRC522()
        self.message = ""
        self.counter = 20

    def end_read(self):
        self.continue_reading = False
        print "Ctrl+C captured, ending read."
        self.MIFAREReader.GPIO_CLEEN()

    def do_read(self):
        self.continue_reading = True
        (status, TagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL)
        if status == self.MIFAREReader.MI_OK:
            self.message += "Card detected"
        (status, backData) = self.MIFAREReader.MFRC522_Anticoll()
        if status == self.MIFAREReader.MI_OK:
            self.message += (
                "Card read UID: " + str(backData[0]) + "," + str(backData[1]) + "," + str(backData[2]) + "," + str(
                    backData[3]) + "," + str(backData[4])
            )
            self.end_read()
            return (self.message, backData)
        if self.continue_reading == True:
            self.counter -= 1
            return self.do_read()
