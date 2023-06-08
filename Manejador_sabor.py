import  csv
from Clase_sabor import sabor
class Lista_sabores:
    __sabores : list

    def __init__(self):
        self.__sabores = []


    def cargadatos(self):
        archivo = open('sabores.csv')
        reader = csv.reader(archivo,delimiter= (';'))
        next(reader)
        for fila in reader:
            Sabor = sabor(fila[0],fila[1],fila[2])
            self.__sabores.append(Sabor)
        archivo.close()

    def buscarsabor(self,gusto):
        band = True
        i = 0
        while band and i < len(self.__sabores):
            if self.__sabores[i].getnombre() == gusto:
                band = False
            else:
                i = i + 1
        if band:
            return None
        else:
            return self.__sabores[i]

    def cantidadsabores(self):
        return len(self.__sabores)

    def mejorsabor(self,contadores):
        print("Top 5 gustos mas pedidos")
        b = 1
        while b < 6:
            max = 0
            maxi = 0
            for i in range(len(contadores)):
                if contadores[i] > max:
                    max = contadores[i]
                    maxi = i
            if contadores[maxi]!= 0:
                print("""
{}-{}""".format(b,self.__sabores[maxi].getnombre()))
            contadores[maxi] = 0
            b = b + 1

    def idsabor(self):
        id = int(input("ingrese el codigo de sabor a evaluar\n"))
        band = True
        i = 0
        while band and i < len(self.__sabores):
            if self.__sabores[i].getid() == id:
                band = False
            else:
                i = i + 1
        if band:
            print("Error id incorrecto")
        else:
            return self.__sabores[i].getnombre()

    def testsabores(self):
        archivo = open('sabores.csv')
        reader = csv.reader(archivo, delimiter=(';'))
        next(reader)
        for fila in reader:
            Sabor = sabor(fila[0], fila[1], fila[2])
            self.__sabores.append(Sabor)
        archivo.close()
        return self.__sabores
