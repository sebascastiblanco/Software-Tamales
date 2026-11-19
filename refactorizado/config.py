# Extract Class: aqui vive TODO lo que cambia entre sedes.
# Antes estaba repartido (y copiado) en dos bases de codigo.

class Sede:
    def __init__(self, nombre, archivo_inventario, umbral_alerta,
                 precios_tamal, precios_lechona, precios_voltiado,
                 precios_bebida, precio_migao, hojas_parche_urgente):
        self.nombre = nombre
        self.archivo_inventario = archivo_inventario
        self.umbral_alerta = umbral_alerta
        self.precios_tamal = precios_tamal
        self.precios_lechona = precios_lechona
        self.precios_voltiado = precios_voltiado
        self.precios_bebida = precios_bebida
        self.precio_migao = precio_migao
        self.hojas_parche_urgente = hojas_parche_urgente


SEDES = {
    "norte": Sede(
        nombre="norte",
        archivo_inventario="inv.json",
        umbral_alerta=5,
        precios_tamal={"clasico": 8000, "tradicional": 10000,
                       "especial": 13000, "Clasico ": 8000},
        precios_lechona={200: 15000, 250: 19000, 350: 26000},
        precios_voltiado={"clasico": 15500, "tradicional": 21500,
                          "especial": 28000},
        precios_bebida={"jugo natural": 7000, "jugo de naranja": 7000,
                        "limonada": 7000, "gaseosa": 4900},
        precio_migao=25000,
        hojas_parche_urgente=50,
    ),
    "sur": Sede(
        nombre="sur",
        archivo_inventario="inventario_sur.json",
        umbral_alerta=10,
        precios_tamal={"clasico": 8000, "tradicional": 10000,
                       "especial": 12500, "Clasico ": 8000},
        precios_lechona={200: 15000, 250: 18500, 350: 26000},
        precios_voltiado={"clasico": 15500, "tradicional": 21500,
                          "especial": 27000},
        precios_bebida={"jugo natural": 7000, "jugo de naranja": 7000,
                        "limonada": 7000, "gaseosa": 5000},
        precio_migao=25000,
        hojas_parche_urgente=100,
    ),
}

_sede_actual = None


def usar_sede(nombre):
    global _sede_actual
    _sede_actual = SEDES[nombre]


def sede():
    return _sede_actual
