import unittest

# from src.exceptions import (
   # ingrese_numero,
   # NumeroDebeSerPositivo,
# )

from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):

    @patch(  
        'builtins.input',
        return_value='200'
    )
    def test_ingreso_feliz(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 200)

if __name__ == "__main__":
    unittest.main()