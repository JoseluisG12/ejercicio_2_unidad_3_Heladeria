from Clase_helado import helado
class Lista_helados:
    __helados : list

    def __init__(self):
        self.__helados = []

    def venta(self,sabores):
        gramos = int(input("ingrese la cantidad de gramos a consumir\n"))
        precio = float(input("ingrese el precio del helado\n"))
        Helado = helado(gramos,precio)
        cant = int(input("ingrese la cantidad de sabores a eleguir acorde al peso\n"))
        print("""
Sabores:
Choco Nuez
Vainilla con Fresas
Menta Chip
Caramelo Nuez
Platano Caramelo
Cookies and Cream
Tropical Mango
Cafe Mocha
Frambuelate
Mantequilla de Mani con Chocolate""")
        for i in range(cant):
            gusto = input("que gusto desea eleguir\n")
            sabor = sabores.buscarsabor(gusto)
            if sabor == None:
                print("no poseemos stock del sabor eleguido")
            else:
                Helado.addsabor(sabor)
        self.__helados.append(Helado)

    def mostrar(self):
        print("hola")
        for helado in self.__helados:
            print("""
cantidad: {} G
precio: ${}
sabores:""".format(helado.getcantidad(),helado.getprecio()))
            for sabor in helado.getsabores():
                print("""
{}""".format(sabor.getnombre()))

    def contarsabores(self,sabores):

        contadores = [0] * sabores.cantidadsabores()
        for helado in self.__helados:
            for sabor in helado.getsabores():

                contadores[sabor.getid() - 1]  = contadores[sabor.getid() - 1] + 1

        return contadores

    def contargramos(self,sabor):
        acum_gramos = 0
        for helado in self.__helados:
            contar_gustos = 0
            band = False
            for gusto in helado.getsabores():
                contar_gustos = contar_gustos + 1
                if gusto.getnombre() == sabor:
                    band = True

            if band:
                acum_gramos = acum_gramos + (helado.getcantidad()/contar_gustos)

        return acum_gramos

    def saboresporcantidad(self,sabores):
        cantidad = int(input("ingrese el tipo de helado a conocer los sabores vendidos tipos:(1000G,500G,250G)"))
        print("""
helados de {}G
sabores vendidos:""".format(cantidad))
        for helado in self.__helados:
            if helado.getcantidad() == cantidad:
                for sabor in helado.getsabores():
                    print("""

{}""".format(sabor.getnombre()))

    def importetotal(self):
        importe = [0]*5
        for helado in self.__helados:
            if helado.getcantidad() == 1000:
                importe[0]  = importe[0] + helado.getprecio()
            if helado.getcantidad() == 500:
                importe[1]  = importe[1] + helado.getprecio()
            if helado.getcantidad() == 250:
                importe[2]  = importe[2] + helado.getprecio()
            if helado.getcantidad() == 150:
                importe[3]  = importe[3] + helado.getprecio()
            if helado.getcantidad() == 100:
                importe[4]  = importe[4] + helado.getprecio()
        return importe

    def testHelados(self,Msabores):
        opc = int(input("desea probar el test 1 = datos correctos 2 = datos incorrectos 0 = salir\n"))
        while opc != 0:
            if opc == 1:
                print("_____venta_______")
                gramos = int(input("ingrese la cantidad de gramos a consumir\n"))
                precio = float(input("ingrese el precio del helado\n"))
                Helado = helado(gramos, precio)
                cant = int(input("ingrese la cantidad de sabores a eleguir acorde al peso\n"))
                print("""
                        Sabores:
                        Choco Nuez
                        Vainilla con Fresas
                        Menta Chip
                        Caramelo Nuez
                        Platano Caramelo
                        Cookies and Cream
                        Tropical Mango
                        Cafe Mocha
                        Frambuelate
                        Mantequilla de Mani con Chocolate""")
                for i in range(cant):
                    gusto = input("que gusto desea eleguir\n")
                    sabor = Msabores.buscarsabor(gusto)
                    if sabor == None:
                        print("no poseemos stock del sabor eleguido")
                    else:
                        Helado.addsabor(sabor)
                self.__helados.append(Helado)
                print("_____mostrar_______")
                self.mostrar()
                print("_____MejoresSabores_______")
                contador = self.contarsabores(Msabores)
                Msabores.mejorsabor(contador)
                print("____Cantidad_de_Gramos_por_gusto_______")
                gusto = Msabores.idsabor()
                gramos = self.contargramos(gusto)
                print("""
                        La cantidad de gramos vendidos de {} es:{}G""".format(gusto, gramos))
                print("_____importe_por_tipo_______")
                self.saboresporcantidad(Msabores)
                importe = self.importetotal()
                print("_____importetotal_______")
                print("""
                        importe total para helados de:
                         1000G = ${}
                         500G = ${}
                         250G = ${}
                         150G = ${}
                         100 = ${}
                         """.format(importe[0], importe[1], importe[2], importe[3], importe[4]))
            if opc == 2:
                print("_____venta_______")
                Helado = helado('1Kg', '$5000')
                cant = int(input("ingrese la cantidad de sabores a eleguir acorde al peso\n"))
                print("""
                                        Sabores:
                                        Choco Nuez
                                        Vainilla con Fresas
                                        Menta Chip
                                        Caramelo Nuez
                                        Platano Caramelo
                                        Cookies and Cream
                                        Tropical Mango
                                        Cafe Mocha
                                        Frambuelate
                                        Mantequilla de Mani con Chocolate""")
                for i in range(cant):
                    gusto = input("que gusto desea eleguir\n")
                    sabor = Msabores.buscarsabor(gusto)
                    if sabor == None:
                        print("no poseemos stock del sabor eleguido")
                    else:
                        Helado.addsabor(sabor)
                self.__helados.append(Helado)
                print("_____mostrar_______")
                self.mostrar()
                print("_____MejoresSabores_______")
                contador = self.contarsabores(Msabores)
                Msabores.mejorsabor(contador)
                print("____Cantidad_de_Gramos_por_gusto_______")
                gusto = Msabores.idsabor()
                gramos = self.contargramos(gusto)
                print("""
                                        La cantidad de gramos vendidos de {} es:{}G""".format(gusto, gramos))
                print("_____importe_por_tipo_______")
                self.saboresporcantidad(Msabores)
                importe = self.importetotal()
                print("_____importetotal_______")
                print("""
                                        importe total para helados de:
                                         1000G = ${}
                                         500G = ${}
                                         250G = ${}
                                         150G = ${}
                                         100 = ${}
                                         """.format(importe[0], importe[1], importe[2], importe[3], importe[4]))

            opc = int(input("desea probar el test 1 = datos correctos 2 = datos incorrectos 0 = salir\n"))









