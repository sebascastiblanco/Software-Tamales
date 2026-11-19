import inventario, ventas, reportes, parches, datos

def menu():
    print("--- TAMALES EL MANA ---")
    print("1 entrada 2 salida 3 ver 4 contar")
    print("5 tamal 6 lechona 7 voltiado 8 bebida 9 migao")
    print("10 reporte 11 parche 12 salir")

datos.cargar()
while True:
    menu()
    o = input("> ")
    if o == "1":
        n = input("nombre: ")
        c = float(input("cantidad: "))
        inventario.entrada(n, c)
    elif o == "2":
        n = input("nombre: ")
        c = float(input("cantidad: "))
        inventario.salida(n, c)
    elif o == "3":
        inventario.ver()
    elif o == "4":
        inventario.contar()
    elif o == "5":
        t = input("clasico / tradicional / especial: ")
        c = int(input("cuantos: "))
        ventas.vender_tamal(t, c)
    elif o == "6":
        g = int(input("gramos (200/250/350): "))
        c = int(input("cuantos: "))
        ventas.vender_lechona(g, c)
    elif o == "7":
        t = input("clasico / tradicional / especial: ")
        c = int(input("cuantos: "))
        ventas.vender_voltiado(t, c)
    elif o == "8":
        b = input("jugo natural / jugo de naranja / limonada / gaseosa: ")
        c = int(input("cuantos: "))
        ventas.vender_bebida(b, c)
    elif o == "9":
        c = int(input("cuantos: "))
        ventas.vender_migao(c)
    elif o == "10":
        reportes.reporte()
    elif o == "11":
        parches.parche_inicial()
        parches.parche1()
        parches.parche_urgente()
    elif o == "12":
        break
    else:
        print("???")
