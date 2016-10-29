import os
import MFRC522
import signal
import subprocess

p = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
out, err = p.communicate()

def findProcess(out):
    for line in out.splitlines():
        if 'sudo python read.py' or 'sudo python reader.py' in line:
            pid = int(line.split(None, 1)[0])
            os.kill(pid, signal.SIGKILL)

findProcess(out)

MIFAREReader = MFRC522.MFRC522()

MIFAREReader.GPIO_CLEEN()
