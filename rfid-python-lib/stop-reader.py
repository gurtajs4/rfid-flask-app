import os
import MFRC522
import signal
import subprocess

p = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
out, err = p.communicate()


def find_process(out):
    for line in out.splitlines():
        if 'sudo python read.py' in line or 'sudo python reader.py' in line:
            pid = int(line.split(" ")[7])
            os.kill(pid, signal.SIGKILL)

find_process(out)

MIFAREReader = MFRC522.MFRC522()

MIFAREReader.GPIO_CLEEN()
