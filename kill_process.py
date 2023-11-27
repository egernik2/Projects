import subprocess
from time import sleep
print ('Loop started!')
while True:
    print ('New try started')
    result = subprocess.Popen('tasklist | find "chrome.exe"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = result.communicate()
    if out:
        print ('Game process founded!')
        next_result = subprocess.Popen('taskkill /IM "chrome.exe" /f', shell=True)
        next_result.communicate()
        print ('Killing command status code: {}'.format(next_result.poll()))
    else:
        print ('Game process not found')
    sleep(10)