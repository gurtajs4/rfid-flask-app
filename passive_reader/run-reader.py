import os
import subprocess

dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
process_name = 'sudo python ' + dir_path + '/rfid_python_lib/bkc_user_reader.py'
print(process_name)
subprocess.Popen(process_name, shell=True)
# rel_path=os.path.dirname(os.path.realpath(__file__))
# subprocess.Popen('sudo python ' + rel_path + '/bkc_user_reader.py', shell=True)
# subprocess.Popen('sudo python ' + rel_path + '/background_reader.py', shell=True)
