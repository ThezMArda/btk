class Logger:
    _instance = None
    def __new__(cls):
        if cls._instance in None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def log(self,msg :str):
        print("[log]" ,msg)