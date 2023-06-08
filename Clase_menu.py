
class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {1:self.op1,
                           2:self.op2,
                           3:self.op3,
                           4:self.op4,
                           5:self.op5,
                           }

    def run(self,sabores,helados):
        band = True
        while band:
            b = int(input("""
Menu Principal:
1- vender Helado
2- conocer helados mas vendidos
3- ingresar el id de un sabor para saber cuantos gramos se venideron
4- saber q sabor se vendio por tamaño de helado
5- conocer el importe total por cada tipo de helado
\n"""))
            func = self.__switcher.get(b)
            if func:
                func(sabores,helados)
            else:
                print("Saliendo...")
                band = False

    def op1(self,sabores,helados):
        helados.venta(sabores)

    def op2(self,sabores,helados):
        contadores = helados.contarsabores(sabores)
        sabores.mejorsabor(contadores)

    def op3(self,sabores,helados):
        gusto = sabores.idsabor()
        gramos = helados.contargramos(gusto)
        print("""
La cantidad de gramos vendidos de {} es:{}G""".format(gusto,gramos))

    def op4(self,sabores,helados):
        helados.saboresporcantidad(sabores)

    def op5(self, sabores, helados):
        importe = helados.importetotal()
        print("""
importe total para helados de:
 1000G = ${}
 500G = ${}
 250G = ${}
 150G = ${}
 100 = ${}
 """.format(importe[0],importe[1],importe[2],importe[3],importe[4]))




