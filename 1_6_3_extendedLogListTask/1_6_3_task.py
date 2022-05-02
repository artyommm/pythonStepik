import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(Loggable, list):
    def append(self, el):
        list.append(self, el)
        self.log(el)

x = LoggableList()
x.append(5)
print(x)