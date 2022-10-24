class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Profile(metaclass=SingletonMeta):
    def __init__(self):
        self.PUK_srting = ""
        self.PRK_srting = ""

    def load(self):
        with open("data/keys/PUK.txt", "r") as f:
            self.PUK_srting = f.read()
        with open("data/keys/PRK.txt", "r") as f:
            self.PRK_srting = f.read()

    def show_keys(self):
        print('----Private Key----')
        print(self.PRK_srting)
        print('----Public Key----')
        print(self.PUK_srting)
    
    def generate_key():
        

