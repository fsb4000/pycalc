import unittest
import calculator
 
class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(5, 2), 7)

if __name__ == '__main__':
    unittest.main()
