import datos

def entrada(n, c):
    # n = nombre, c = cantidad (kg? gramos? libras? quien sabe)
    datos.cargar()
    if n in datos.inv:
        datos.inv[n] = datos.inv[n] + c
    else:
        datos.inv[n] = c
    datos.guardar()
    datos.cuaderno("entro " + n + " " + str(c))

def salida(n, c):
    datos.cargar()
    if n in datos.inv:
        datos.inv[n] = datos.inv[n] - c   # puede quedar negativo, no importa
    datos.guardar()

def ver():
    datos.cargar()
    for k in datos.inv:
        print(k, datos.inv[k])

def contar():
    # el conteo se hace a mano cada semana y se escribe lo que dice el empleado
    datos.cargar()
    for k in datos.inv:
        r = input("cuanto hay de " + k + "? ")
        try:
            datos.inv[k] = float(r)
        except:
            pass
    datos.guardar()
    datos.guardar_excel()
