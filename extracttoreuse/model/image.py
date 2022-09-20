class Image:

    def __init__(self, path) -> None:
        self.__path = path

    def getPath(self) -> str:
        return self.__path