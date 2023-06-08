from Manejador_sabor import Lista_sabores
from Manejador_Helados import Lista_helados
from Clase_menu import Menu




if __name__=='__main__':
    opc = input("desea probar los metodos con la funcion test y = si n = no\n")
    if opc == 'y':
        Msabores = Lista_sabores()
        Msabores.testsabores()
        Mhelado = Lista_helados()
        Mhelado.testHelados(Msabores)
    sabores = Lista_sabores()
    sabores.cargadatos()
    helados = Lista_helados()
    menu = Menu()
    menu.run(sabores,helados)

