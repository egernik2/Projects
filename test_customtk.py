import subprocess
import threading
import time
import os

nodes = ["192.168.0.20", "google.com", "localhost", "example.com", '192.168.0.29']
status = {}

def pinging(node):
    result = subprocess.run(['ping', '-n', '1', node], stdout=subprocess.PIPE)
    if result.returncode == 0:
        status[node] = 'UP'
    else:
        status[node] = 'DOWN'

def main():
    while True:
        threads = []
        for node in nodes:
            thread = threading.Thread(target=pinging, args=(node, ))
            threads.append(thread)
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        os.system('cls')
        for node in nodes:
            print ('{} - {}'.format(node, status[node]))
        time.sleep(1)

if __name__ == '__main__':
    main()