import datos
import config


# carga inicial "de prueba" (nombres escritos como cada quien quiso)
def parche_inicial():
    datos.cargar()
    datos.establecer("masa de maiz", 30)
    datos.establecer("Masa", 12)
    datos.establecer("cerdo", 25)
    datos.establecer("pollo", 15)
    datos.establecer("arroz", 10)
    datos.establecer("arveja", 6)
    datos.establecer("hoja de platano", 200)
    datos.establecer("huevo", 60)
    datos.establecer("pan", 8)
    datos.establecer("naranja", 40)
    datos.establecer("limon", 30)
    datos.establecer("gaseosa 400", 48)
    datos.guardar()


# parche del 12 marzo (se rompio el conteo)
def parche1():
    datos.cargar()
    for nombre in datos.nombres():
        if datos.obtener(nombre) < 0:
            datos.establecer(nombre, 0)
    datos.guardar()


# parche urgente: la cantidad extra ahora sale de la configuracion de la sede
def parche_urgente():
    if datos.existe("hoja de platano"):
        extra = config.sede().hojas_parche_urgente
        datos.establecer("hoja de platano", datos.obtener("hoja de platano") + extra)


# parche2_final_FINAL
def parche2():
    datos.cargar()
    for nombre in ["Masa", "masa", "masa maiz"]:
        if not datos.existe(nombre):
            datos.establecer(nombre, 0)
    datos.guardar()
