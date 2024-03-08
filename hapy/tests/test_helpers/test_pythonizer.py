import unittest

import hapy.helpers as helpers


class TestPythonizer(unittest.TestCase):

    def test_weird_symbols(self):
        func_name = r'has_new_\€€'
        pythonized = helpers.Pythonize.method_name(func_name)
        self.assertTrue(pythonized.isidentifier())

    def test_more_weird_symbols(self):
        func_name = 'has_new_\€€|@##|¢∞#¢@∞∞¢¬¢@¢@®¢#®€æƒ¥†™®¥'
        pythonized = helpers.Pythonize.method_name(func_name)
        self.assertTrue(pythonized.isidentifier())
º