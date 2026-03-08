class Client:
    def __init__(self, IP, PORT):
        self.IP = IP
         = PORT

    def __str__(self):
        return self.IP,self.PORT

    def ping(self):
        print("ok")

