import unittest

def soma(a, b):
    return a + b

class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        resultado = soma(2, 3)
        self.assertEqual(resultado, 5)

    def test_soma_negativos(self):
        resultado = soma(-2, -3)
        self.assertEqual(resultado, -5)

    def test_soma_positivo_negativo(self):
        resultado = soma(2, -3)
        self.assertEqual(resultado, -1)

if __name__ == '__main__':
    unittest.main()
