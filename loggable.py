import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list,Loggable):
    def append(self, p_object):
        list.append(self, p_object)
        self.log( p_object)

a = LoggableList()
a.append('lolo')