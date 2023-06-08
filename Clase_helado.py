
class helado:
    __gramos : int
    __precio : float
    __sabores : list

    def __init__(self,gramos,precio,sabor = None) -> None:
        self.__gramos = int(gramos)
        self.__precio = float(precio)
        self.__sabores = []
        if sabor != None:
            self.addsabor(sabor)

    def addsabor(self,sabor):
      self.__sabores.append(sabor)

    def getcantidad(self):
        return self.__gramos

    def getprecio(self):
        return self.__precio

    def getsabores(self):
        return self.__sabores


