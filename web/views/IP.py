import socket

class ip():

    def __init__(self):
        self.__ip = socket.gethostbyname(socket.gethostname())

    def getIP(self):
        return self.__ip

    def toString(self):
        return "IP: {}".format(self.getIP())

a = ip()
print  a.getIP()