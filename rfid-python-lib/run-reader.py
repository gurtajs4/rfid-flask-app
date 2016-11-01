import os
import subprocess


rel_path=os.path.dirname(os.path.realpath(__file__))
subprocess.Popen('sudo python ' + rel_path + 'reader.py', shell=True)
