import unittest
from transferencias import(
transferir,
MONTO_INVALIDADO,
SALDO_INSUFICIENTE,
LIMITE_DIARIO,
LIMITE_EXCEDIDO,
APROBADA)

class TestTransferir(unittest.TestCase):
    def test_aprobada_por_envio_normal(self):
        self.assertEqual(transferir(50000, 40000, 100000), APROBADA)
    def test_monto_cero(self):
        self.assertEqual(transferir(50000, 0, 100000), MONTO_INVALIDADO)
    def test_limite_excedido(self):
        self.assertEqual(transferir(50000,50000,200000),LIMITE_EXCEDIDO)
if __name__ == "__main__":
    unittest.main()