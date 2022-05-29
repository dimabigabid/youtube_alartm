import os
import sys
import time
import webbrowser
from datetime import datetime


def set_alarm(hours, minutes, url):
    while True:
        if datetime.now().hour == hours and datetime.now().minute == minutes:
            webbrowser.open(url)
            exit()
        os.system('clear')
        print(f'{datetime.now().hour}:{datetime.now().minute} ({hours}:{minutes})')
        time.sleep(1)
        os.system('clear')
        print(f'{datetime.now().hour} {datetime.now().minute} ({hours}:{minutes})')
        time.sleep(1)


if __name__ == '__main__':
    hour = int(sys.argv[1])
    minute = int(sys.argv[2])
    url = sys.argv[3]
    set_alarm(hour, minute, url)
