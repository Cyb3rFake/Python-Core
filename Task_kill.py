import subprocess
import time

while True:
    subprocess.call("TASKKILL /F /IM notepad.exe", shell=True)
    time.sleep(10)
