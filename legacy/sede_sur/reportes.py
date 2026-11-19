import datos, ventas

def reporte():
    datos.cargar()
    print("=== REPORTE ===")
    for k in datos.inv:
        if datos.inv[k] < 10:
            print("poco", k)     # unica "alerta" que hay, y solo si alguien pide el reporte
    print("ventas del dia:", ventas.total_dia())

def rep2():
    # igual que rep pero con otro formato
    datos.cargar()
    for k in datos.inv:
        if datos.inv[k] < 10:
            print("*** poco ***", k)
    print("TOTAL VENTAS:", ventas.total_dia())
