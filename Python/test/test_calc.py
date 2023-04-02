import unittest
import Python.test.calc as calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calc.add(22, 20)
        self.assertEqual(result, 42)
