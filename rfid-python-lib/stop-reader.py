import os
import MFRC522
import signal
import subprocess

p = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
out, err = p.communicate()


def find_process(out):
    for line in out.splitlines():
        if 'PID' in line:
            words = []
            for word in line.split(" "):
                if word is not " " and word is not "":
                    words.push(word)
            index = int(words.index('PID'))
            print "Index of PID is " + index
        if 'sudo python read.py' in line or 'sudo python reader.py' in line:
            words = []
            for word in line.split(" "):
                if word is not " " and word is not "":
                    word.push(word)
            print "*******************"
            pid = int(line.split(" ")[index])
            os.kill(pid, signal.SIGKILL)

find_process(out)

MIFAREReader = MFRC522.MFRC522()

MIFAREReader.GPIO_CLEEN()
