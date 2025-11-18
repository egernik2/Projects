import signal
import time

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    print('Now exiting...')
    exit(0)

signal.signal(signal.SIGTERM, signal_handler)

while True:
    print('Program is running...')
    time.sleep(1)