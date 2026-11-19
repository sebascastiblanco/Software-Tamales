import datos
import ventas
import config


# Extract Method: la busqueda de insumos bajos estaba repetida en rep y rep2
def insumos_bajos():
    bajos = []
    for nombre in datos.nombres():
        if datos.obtener(nombre) < config.sede().umbral_alerta:
            bajos.append(nombre)
    return bajos


# Rename Method: rep() (norte) y reporte() (sur) -> un solo nombre claro
def reporte_del_dia():
    datos.cargar()
    print("=== REPORTE ===")
    for nombre in insumos_bajos():
        print("poco", nombre)
    print("ventas del dia:", ventas.total_dia())


def reporte_del_dia_alterno():
    # igual que reporte_del_dia pero con otro formato
    datos.cargar()
    for nombre in insumos_bajos():
        print("*** poco ***", nombre)
    print("TOTAL VENTAS:", ventas.total_dia())
