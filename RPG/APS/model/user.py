class User:
    __instance = None
    
    def __new__(cls, username=None, password=None):
        if cls.__instance is None:
            cls.__instance = super(User, cls).__new__(cls)
            cls.__instance.username = username
            cls.__instance.password = password
        return cls.__instance
    
    def __init__(self, username=None, password=None):
        if not hasattr(self, '_initialized'):
            self.username = username
            self.password = password
            self._initialized = True
