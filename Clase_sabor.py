
class sabor:
    __id : int
    __ingredientes : str
    __nombre : str
    def __init__(self,id,ingredientes,nombre):
        self.__id = int(id)
        self.__ingredientes = ingredientes
        self.__nombre = nombre

    def getnombre(self):
        return self.__nombre

    def getid(self):
        return self.__id
