class Myclass:
    def __init__(self, name):
        self.name = name
        
    def myfunc(self, callback):
        callback(self.name)
        