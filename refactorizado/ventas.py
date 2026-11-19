import time
import datos
import config


# Extract Method: este bloque estaba copiado 5 veces (una por producto)
def registrar_venta(producto, cantidad, precio_unitario):
    total = precio_unitario * cantidad
    datos.ventas.append([producto, cantidad, total, time.time()])
    with open("ventas.txt", "a") as archivo:
        archivo.write(producto + "," + str(cantidad) + "," + str(total) + "\n")
    print("total", total)


def vender_tamal(tipo, cantidad):
    # tipo = clasico / tradicional / especial
    precios = config.sede().precios_tamal
    if tipo not in precios:
        print("no existe")
        return
    registrar_venta("tamal " + tipo, cantidad, precios[tipo])


def vender_lechona(gramos, cantidad):
    # gramos = 200, 250 o 350
    precios = config.sede().precios_lechona
    if gramos not in precios:
        print("no existe")
        return
    registrar_venta("lechona " + str(gramos), cantidad, precios[gramos])


def vender_voltiado(tipo, cantidad):
    precios = config.sede().precios_voltiado
    if tipo not in precios:
        print("no existe")
        return
    registrar_venta("voltiado " + tipo, cantidad, precios[tipo])


def vender_bebida(bebida, cantidad):
    precios = config.sede().precios_bebida
    if bebida not in precios:
        print("no existe")
        return
    registrar_venta(bebida, cantidad, precios[bebida])


def vender_migao(cantidad):
    registrar_venta("migao", cantidad, config.sede().precio_migao)


def total_dia():
    suma = 0
    for venta in datos.ventas:
        suma = suma + venta[2]
    return suma
