import logging
logging.basicConfig(filename='log/application.log', encoding='utf-8', level=logging.DEBUG )

class WrapLog:

    def __init__(self):
        self.__log = logging
    
    def log(self) -> logging:
        return self.__log