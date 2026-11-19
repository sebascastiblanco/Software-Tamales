import datos

# carga inicial "de prueba" (nombres escritos como cada quien quiso)
def parche_inicial():
    datos.cargar()
    datos.inv["masa de maiz"] = 30
    datos.inv["Masa"] = 12
    datos.inv["cerdo"] = 25
    datos.inv["pollo"] = 15
    datos.inv["arroz"] = 10
    datos.inv["arveja"] = 6
    datos.inv["hoja de platano"] = 200
    datos.inv["huevo"] = 60
    datos.inv["pan"] = 8
    datos.inv["naranja"] = 40
    datos.inv["limon"] = 30
    datos.inv["gaseosa 400"] = 48
    datos.guardar()

# parche del 12 marzo (se rompio el conteo)
def parche1():
    datos.cargar()
    for k in list(datos.inv):
        if datos.inv[k] < 0:
            datos.inv[k] = 0
    datos.guardar()

# parche urgente (no se sabe por que funciona)
def parche_urgente():
    try:
        datos.inv["hoja de platano"] = datos.inv["hoja de platano"] + 50
    except:
        pass

# parche2_final_FINAL
def parche2():
    datos.cargar()
    datos.inv["Masa"] = datos.inv.get("Masa", 0)
    datos.inv["masa"] = datos.inv.get("masa", 0)
    datos.inv["masa maiz"] = datos.inv.get("masa maiz", 0)
    datos.guardar()
