import unittest
import Python.test.calc as calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(22, 20), 42)
