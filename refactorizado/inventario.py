import datos

# Unidad base unica: KG (en la sede sur algunas funciones usaban gramos)


def entrada(nombre, cantidad):
    datos.cargar()
    if datos.existe(nombre):
        datos.establecer(nombre, datos.obtener(nombre) + cantidad)
    else:
        datos.establecer(nombre, cantidad)
    datos.guardar()
    datos.anotar_en_cuaderno("entro " + nombre + " " + str(cantidad))


def salida(nombre, cantidad):
    datos.cargar()
    if datos.existe(nombre):
        # puede quedar negativo (igual que antes)
        datos.establecer(nombre, datos.obtener(nombre) - cantidad)
    datos.guardar()


def mostrar_inventario():
    datos.cargar()
    for nombre in datos.nombres():
        print(nombre, datos.obtener(nombre))


def contar():
    # el conteo se hace a mano cada semana y se escribe lo que dice el empleado
    datos.cargar()
    for nombre in datos.nombres():
        respuesta = input("cuanto hay de " + nombre + "? ")
        try:
            datos.establecer(nombre, float(respuesta))
        except ValueError:
            pass
    datos.guardar()
    datos.guardar_excel()


def merma(nombre, cantidad):
    # solo existia en la sede sur y solo imprime, no guarda nada
    print("se perdio", nombre, cantidad)


# Move Method: estas funciones estaban en ventas.py (solo sede sur).
# Descontar insumos es responsabilidad del inventario, no de las ventas.
# Todo en KG. Aun NO se llaman desde el menu (igual que antes).
def descontar_tamal(cantidad):
    salida("masa", cantidad * 0.150)
    salida("hoja de platano", cantidad * 2)


def descontar_lechona(gramos, cantidad):
    salida("cerdo", gramos * cantidad / 1000)
