import datetime

class Logger(object):
    log_file = None

    @staticmethod
    def instance(): 
        """
        This method is used to instantiate class object.
        It'll make sure class will have only one object.
        """
        if '_instance' not in Logger.__dict__:
            Logger._instance = Logger()
        return Logger._instance
    
    def open_log(self, path):
        self.log_file = open(path, mode='w')

    def write_log(self, log_record):
        now = str(datetime.datetime.now())
        record = f"{now}: {log_record}"
        self.log_file.writelines(record)

    def close_log(self):
        self.log_file.close()

logger = Logger.instance()
logger.open_log('my.log')
logger.write_log(' Logging with classic Singleton Pattern.')
logger.close_log()

with open('my.log', 'r') as f:
    for line in f:
        print(line)

"""
What's wrong with classic Singleton?

1) Violates Single Responsibility Principle
   - As logger class is responsible for creating its object. Also, it is responsible to open and close log file and write logs.
2) Non Standard class object.
   - To get an instance you have to call instance method first.
3) Harder to test
   - As they are highly coupled with the object.
4) Carry global state.
5) Hard to sub-class
   - As they carry state.
"""