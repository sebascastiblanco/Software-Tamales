"""
Pruebas de caracterizacion: se ejecuta el programa ANTES (legacy) y DESPUES
(refactorizado) con las mismas entradas y se comparan la salida en pantalla
y los archivos que genera. Si todo es igual, el comportamiento se conservo.
"""
import os
import subprocess
import sys
import tempfile
import unittest

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCHIVOS = ["inv.json", "inventario_sur.json", "ventas.txt",
            "cuaderno.txt", "inventario_excel.csv"]

# Escenario 1: parche inicial, entradas/salidas, ventas de todo tipo, reporte
ESCENARIO_VENTAS = [
    "11", "1", "sal", "3", "3", "2", "masa", "2", "3",
    "5", "clasico", "3",
    "5", "Clasico ", "1",
    "5", "especial", "2",
    "5", "pizza", "1",
    "6", "250", "2",
    "6", "100", "1",
    "7", "especial", "1",
    "8", "gaseosa", "2",
    "8", "cafe", "1",
    "9", "2",
    "10", "99", "12",
]

# Escenario 2: conteo fisico (con una respuesta invalida) y reporte
ESCENARIO_CONTEO = ["11", "4"] + ["5"] * 3 + ["abc"] + ["7"] * 20 + ["10", "12"]


def ejecutar(comando, entradas):
    """Corre un programa en una carpeta temporal y devuelve (pantalla, archivos)."""
    with tempfile.TemporaryDirectory() as carpeta:
        resultado = subprocess.run(
            comando, input="\n".join(entradas) + "\n", cwd=carpeta,
            capture_output=True, text=True, timeout=30)
        archivos = {}
        for nombre in ARCHIVOS:
            ruta = os.path.join(carpeta, nombre)
            if os.path.exists(ruta):
                with open(ruta) as f:
                    archivos[nombre] = f.read()
        return resultado.stdout, archivos


class PruebasCaracterizacion(unittest.TestCase):
    def comparar(self, sede, entradas):
        antes = ejecutar([sys.executable,
                          os.path.join(RAIZ, "legacy", "sede_" + sede, "main.py")],
                         entradas)
        despues = ejecutar([sys.executable,
                            os.path.join(RAIZ, "refactorizado", "main.py"), sede],
                           entradas)
        self.assertEqual(antes[0], despues[0], "la pantalla cambio")
        self.assertEqual(antes[1], despues[1], "los archivos generados cambiaron")
        self.assertTrue(len(antes[0]) > 0)

    def test_ventas_sede_norte(self):
        self.comparar("norte", ESCENARIO_VENTAS)

    def test_ventas_sede_sur(self):
        self.comparar("sur", ESCENARIO_VENTAS)

    def test_conteo_sede_norte(self):
        self.comparar("norte", ESCENARIO_CONTEO)

    def test_conteo_sede_sur(self):
        self.comparar("sur", ESCENARIO_CONTEO)


if __name__ == "__main__":
    unittest.main(verbosity=2)
