import datetime
import os

log_directory = os.path.dirname(__file__)
log_file = None


def initialize_log(log_d=log_directory):
    global log_file
    log_d += "\\logs"
    now = datetime.datetime.now()
    name = f"\\log_{now.month}-{now.day}-{now.year}_{now.hour}.{now.minute}.{now.second}.txt"
    if not os.path.isdir(log_d):
        os.mkdir(log_d)

    log_file = open(log_d + name, 'w')


def log(message, broadcast=True):
    message = f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {message}"
    if broadcast:
        print(message)
    log_file.write(message + "\n")
    log_file.flush()
