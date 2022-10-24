import json


class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]




class Conversations(metaclass=SingletonMeta):
    def __init__(self, file_address):
        self.list = []
        self.file_address = file_address
