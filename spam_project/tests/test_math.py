# test_math.py
import unittest
from code.common import add

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,1), 2)
        self.assertEqual(add('1','1'), '11')

if __name__ == '__main__':
    unittest.main()

