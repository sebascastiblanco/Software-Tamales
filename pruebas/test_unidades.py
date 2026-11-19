"""Pruebas unitarias de las funciones nuevas o movidas en la refactorizacion."""
import contextlib
import io
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "refactorizado"))

import config
import datos
import inventario
import reportes
import ventas


class Base(unittest.TestCase):
    def setUp(self):
        self.carpeta = tempfile.TemporaryDirectory()
        self.anterior = os.getcwd()
        os.chdir(self.carpeta.name)
        config.usar_sede("norte")
        datos.ventas.clear()
        datos.cargar()

    def tearDown(self):
        os.chdir(self.anterior)
        self.carpeta.cleanup()

    def capturar(self, funcion, *args):
        salida = io.StringIO()
        with contextlib.redirect_stdout(salida):
            funcion(*args)
        return salida.getvalue()


class PruebasExtractMethod(Base):
    def test_registrar_venta_calcula_y_guarda(self):
        texto = self.capturar(ventas.registrar_venta, "tamal clasico", 3, 8000)
        self.assertEqual(texto, "total 24000\n")
        self.assertEqual(ventas.total_dia(), 24000)
        with open("ventas.txt") as f:
            self.assertEqual(f.read(), "tamal clasico,3,24000\n")

    def test_producto_inexistente_no_vende(self):
        texto = self.capturar(ventas.vender_tamal, "pizza", 1)
        self.assertEqual(texto, "no existe\n")
        self.assertEqual(ventas.total_dia(), 0)

    def test_insumos_bajos_usa_umbral_de_la_sede(self):
        datos.establecer("pan", 8)
        self.assertEqual(reportes.insumos_bajos(), [])       # norte: umbral 5
        config.usar_sede("sur")
        self.assertEqual(reportes.insumos_bajos(), ["pan"])  # sur: umbral 10


class PruebasConfiguracionPorSede(Base):
    def test_precio_especial_distinto_por_sede(self):
        self.capturar(ventas.vender_tamal, "especial", 1)
        self.assertEqual(ventas.total_dia(), 13000)
        datos.ventas.clear()
        config.usar_sede("sur")
        self.capturar(ventas.vender_tamal, "especial", 1)
        self.assertEqual(ventas.total_dia(), 12500)


class PruebasEncapsulate(Base):
    def test_establecer_y_obtener(self):
        datos.establecer("arroz", 10)
        self.assertTrue(datos.existe("arroz"))
        self.assertEqual(datos.obtener("arroz"), 10)
        self.assertFalse(datos.existe("sal"))

    def test_guardar_y_cargar(self):
        datos.establecer("arroz", 10)
        datos.guardar()
        datos.establecer("arroz", 99)
        datos.cargar()
        self.assertEqual(datos.obtener("arroz"), 10)


class PruebasMoveMethod(Base):
    def test_descontar_tamal_en_kg(self):
        datos.establecer("masa", 1.0)
        datos.establecer("hoja de platano", 10)
        datos.guardar()
        inventario.descontar_tamal(2)
        datos.cargar()
        self.assertAlmostEqual(datos.obtener("masa"), 0.7)
        self.assertEqual(datos.obtener("hoja de platano"), 6)

    def test_descontar_lechona_en_kg(self):
        datos.establecer("cerdo", 10)
        datos.guardar()
        inventario.descontar_lechona(250, 2)   # 500 g = 0.5 kg
        datos.cargar()
        self.assertAlmostEqual(datos.obtener("cerdo"), 9.5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
