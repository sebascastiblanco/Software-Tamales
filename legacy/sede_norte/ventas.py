import datos, time

def vender_tamal(t, c):
    # t = clasico / tradicional / especial
    p = 0
    if t == "clasico":
        p = 8000
    elif t == "tradicional":
        p = 10000
    elif t == "especial":
        p = 13000
    elif t == "Clasico ":
        p = 8000
    else:
        print("no existe")
        return
    total = p * c
    datos.ventas.append(["tamal " + t, c, total, time.time()])
    f = open("ventas.txt", "a")
    f.write("tamal " + t + "," + str(c) + "," + str(total) + "\n")
    print("total", total)
    # TODO: descontar insumos (se hace a mano al final del dia)

def vender_lechona(g, c):
    # g = gramos (200, 250 o 350)
    p = 0
    if g == 200:
        p = 15000
    elif g == 250:
        p = 19000
    elif g == 350:
        p = 26000
    else:
        print("no existe")
        return
    total = p * c
    datos.ventas.append(["lechona " + str(g), c, total, time.time()])
    f = open("ventas.txt", "a")
    f.write("lechona " + str(g) + "," + str(c) + "," + str(total) + "\n")
    print("total", total)

def vender_voltiado(t, c):
    # copia de vender_tamal() pero con lechona
    p = 0
    if t == "clasico":
        p = 15500
    elif t == "tradicional":
        p = 21500
    elif t == "especial":
        p = 28000
    else:
        print("no existe")
        return
    total = p * c
    datos.ventas.append(["voltiado " + t, c, total, time.time()])
    f = open("ventas.txt", "a")
    f.write("voltiado " + t + "," + str(c) + "," + str(total) + "\n")
    print("total", total)

def vender_bebida(b, c):
    p = 0
    if b == "jugo natural":
        p = 7000
    elif b == "jugo de naranja":
        p = 7000
    elif b == "limonada":
        p = 7000
    elif b == "gaseosa":
        p = 4900
    else:
        print("no existe")
        return
    total = p * c
    datos.ventas.append([b, c, total, time.time()])
    f = open("ventas.txt", "a")
    f.write(b + "," + str(c) + "," + str(total) + "\n")
    print("total", total)

def vender_migao(c):
    total = 25000 * c
    datos.ventas.append(["migao", c, total, time.time()])
    f = open("ventas.txt", "a")
    f.write("migao," + str(c) + "," + str(total) + "\n")
    print("total", total)

def total_dia():
    s = 0
    for v in datos.ventas:
        s = s + v[2]
    return s
