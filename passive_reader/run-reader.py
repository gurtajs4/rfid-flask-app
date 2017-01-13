import os
import subprocess


rel_path=os.path.dirname(os.path.realpath(__file__))
subprocess.Popen('sudo python ' + rel_path + '/bkc_user_reader.py', shell=True)
# subprocess.Popen('sudo python ' + rel_path + '/background_reader.py', shell=True)
