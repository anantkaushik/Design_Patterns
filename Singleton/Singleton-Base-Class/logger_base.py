import datetime
from singleton_base import Singleton

class Logger(Singleton):
    log_file = None

    def __init__(self, path):
        if not self.log_file:
            self.log_file = open(path, mode='w')

    def write_log(self, log_record):
        now = str(datetime.datetime.now())
        record = f"{now}: {log_record}\n"
        self.log_file.writelines(record)

    def close_log(self):
        self.log_file.close()
