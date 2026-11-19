import json, os
# copiado de la sede norte, modificado por Carlos
inv = {}
ventas = []
f = "inventario_sur.json"
x = 0

def cargar():
    global inv
    try:
        inv = json.load(open(f))
    except:
        inv = {}

def guardar():
    json.dump(inv, open(f, "w"))

# el excel se guarda aparte (a veces se olvida llamar esto)
def guardar_excel():
    a = open("inventario_excel.csv", "a")
    for k in inv:
        a.write(k + "," + str(inv[k]) + "\n")

# lo que se anota en el cuaderno de la cocina
def cuaderno(t):
    c = open("cuaderno.txt", "a")
    c.write(t + "\n")
