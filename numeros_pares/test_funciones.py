"""Tests unitarios de la función `parimpar` del módulo `funciones`.

Se ejecutan con:
    python test_funciones.py
    python -m unittest test_funciones
"""
import unittest

from funciones import parimpar


class TestParImpar(unittest.TestCase):
    """Casos de prueba de `parimpar`: cero, pares, impares, negativos y decimales."""

    def test_cero(self):
        """El 0 devuelve "Cero"."""
        self.assertEqual(parimpar(0), "Cero")

    def test_par(self):
        """Un número par positivo devuelve "Par"."""
        self.assertEqual(parimpar(4), "Par")

    def test_impar(self):
        """Un número impar positivo devuelve "Impar"."""
        self.assertEqual(parimpar(3), "Impar")

    def test_uno(self):
        """El 1, el impar más chico, devuelve "Impar"."""
        self.assertEqual(parimpar(1), "Impar")

    def test_impar_no_multiplo_de_3(self):
        """Impares que no son múltiplos de 3 también devuelven "Impar"."""
        self.assertEqual(parimpar(5), "Impar")
        self.assertEqual(parimpar(7), "Impar")

    def test_par_negativo(self):
        """Un par negativo devuelve "Par"."""
        self.assertEqual(parimpar(-4), "Par")

    def test_impar_negativo(self):
        """Un impar negativo devuelve "Impar"."""
        self.assertEqual(parimpar(-3), "Impar")
        self.assertEqual(parimpar(-1), "Impar")

    def test_decimal(self):
        """Un número con parte decimal devuelve "Decimal"."""
        self.assertEqual(parimpar(5.5), "Decimal")

    def test_decimal_negativo(self):
        """Un decimal negativo también devuelve "Decimal"."""
        self.assertEqual(parimpar(-2.5), "Decimal")


if __name__ == "__main__":
    unittest.main()