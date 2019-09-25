# test_math.py
import unittest
import code.common

class TestMath(unittest.TestCase):

    # OVerriden methods
    def setUp(self):
        print('Connecting to database')

    def tearDown(self):
        print('Disconnecting to database')

    def test_add(self):
        """
        Testing add
        """
        self.assertEqual(code.common.add(1,1), 2, '1 plus 1 should equal to 2')
        self.assertEqual(code.common.add('1','1'), '11')


    # A function that changes a function
    @unittest.skip('Skipping this test') # Decorator
    def test_sub(self):
        self.fail()

if __name__ == '__main__':
    unittest.main()

