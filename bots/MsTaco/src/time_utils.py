import time
import datetime

# time variables
from src.config import RESET_HOUR

today = str(time.gmtime().tm_year) + str(time.gmtime().tm_mon).zfill(2) + str(time.gmtime().tm_mday).zfill(2)
yesterday = (datetime.date.today() - datetime.timedelta(days = 1)).strftime('%Y%m%d')
lastweek  = (datetime.date.today() - datetime.timedelta(days = datetime.date.today().weekday())).strftime('%Y%m%d')

time_left = 0

print(today, lastweek)

def update_time():

    global today, yesterday, lastweek, time_left

    now_time = time.gmtime(time.time() - 3600 * (RESET_HOUR - 1))
    now = str(now_time.tm_year) + str(now_time.tm_mon).zfill(2) + str(now_time.tm_mday).zfill(2)

    if now != today:
        today = now
        yesterday = (datetime.date.today() - datetime.timedelta(days = 1)).strftime('%Y%m%d')
        lastweek  = (datetime.date.today() - datetime.timedelta(days = datetime.date.today().weekday())).strftime('%Y%m%d')

        return True
    else:

        time_left = (RESET_HOUR - time.gmtime().tm_hour) % 24
        return False


def get_today():
    return today

def get_yesterday():
    return yesterday

def get_lastweek():
    return lastweek

def get_prevweek():
    return (datetime.date.today() - datetime.timedelta(days = datetime.date.today().weekday() + 7)).strftime('%Y%m%d')

def get_time_left():
    return time_left
