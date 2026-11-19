import json
import config

# Encapsulate Field: el inventario ya no es una variable global publica.
# Solo se toca con las funciones de abajo.
_inventario = {}
ventas = []


def cargar():
    global _inventario
    try:
        with open(config.sede().archivo_inventario) as archivo:
            _inventario = json.load(archivo)
    except (OSError, ValueError):
        _inventario = {}


def guardar():
    with open(config.sede().archivo_inventario, "w") as archivo:
        json.dump(_inventario, archivo)


def existe(nombre):
    return nombre in _inventario


def obtener(nombre):
    return _inventario[nombre]


def establecer(nombre, cantidad):
    _inventario[nombre] = cantidad


def nombres():
    return list(_inventario)


# el excel se guarda aparte (a veces se olvida llamar esto)
def guardar_excel():
    with open("inventario_excel.csv", "a") as archivo:
        for nombre in _inventario:
            archivo.write(nombre + "," + str(_inventario[nombre]) + "\n")


# lo que se anota en el cuaderno de la cocina
def anotar_en_cuaderno(texto):
    with open("cuaderno.txt", "a") as archivo:
        archivo.write(texto + "\n")
