import sys
import config

if len(sys.argv) > 1:
    nombre_sede = sys.argv[1]
else:
    nombre_sede = input("sede (norte / sur): ")

if nombre_sede not in config.SEDES:
    print("sede no valida")
    sys.exit(1)
config.usar_sede(nombre_sede)

import inventario, ventas, reportes, parches, datos


def menu():
    print("--- TAMALES EL MANA ---")
    print("1 entrada 2 salida 3 ver 4 contar")
    print("5 tamal 6 lechona 7 voltiado 8 bebida 9 migao")
    print("10 reporte 11 parche 12 salir")


datos.cargar()
while True:
    menu()
    opcion = input("> ")
    if opcion == "1":
        nombre = input("nombre: ")
        cantidad = float(input("cantidad: "))
        inventario.entrada(nombre, cantidad)
    elif opcion == "2":
        nombre = input("nombre: ")
        cantidad = float(input("cantidad: "))
        inventario.salida(nombre, cantidad)
    elif opcion == "3":
        inventario.mostrar_inventario()
    elif opcion == "4":
        inventario.contar()
    elif opcion == "5":
        tipo = input("clasico / tradicional / especial: ")
        cantidad = int(input("cuantos: "))
        ventas.vender_tamal(tipo, cantidad)
    elif opcion == "6":
        gramos = int(input("gramos (200/250/350): "))
        cantidad = int(input("cuantos: "))
        ventas.vender_lechona(gramos, cantidad)
    elif opcion == "7":
        tipo = input("clasico / tradicional / especial: ")
        cantidad = int(input("cuantos: "))
        ventas.vender_voltiado(tipo, cantidad)
    elif opcion == "8":
        bebida = input("jugo natural / jugo de naranja / limonada / gaseosa: ")
        cantidad = int(input("cuantos: "))
        ventas.vender_bebida(bebida, cantidad)
    elif opcion == "9":
        cantidad = int(input("cuantos: "))
        ventas.vender_migao(cantidad)
    elif opcion == "10":
        reportes.reporte_del_dia()
    elif opcion == "11":
        parches.parche_inicial()
        parches.parche1()
        parches.parche_urgente()
    elif opcion == "12":
        break
    else:
        print("???")
