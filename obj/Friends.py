import json


class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]




class Friends(metaclass=SingletonMeta):
    def __init__(self, file_address):
        self.list = []
        self.file_address = file_address

    def getAll(self):
        return self.list
    
    def get(self, username):
        return self.list[username]
        
    def load(self):
        with open(self.file_address, "r") as f:
            self.list = json.load(f)
            f.close()
        
    def add(self, username, PUK):
        self.list[username] = PUK

    def delete(self, username):
        del self.list[username]

    def save(self):
        with open(self.file_address, "w") as f:
            json.dump(self.list, f)