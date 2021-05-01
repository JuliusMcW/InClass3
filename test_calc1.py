import unittest
import calc


class Test(unittest.TestCase):
	def test_addition(self):
		result = calc.addition(5,4)
		self.assertEqual(result,9)

	def test_subtraction(self):
		result = calc.subtraction(5,4)
		self.assertEqual(result,1)

	def test_multiplication(self):
		result = calc.multiplication(5,4)
		self.assertEqual(result,20)

	def test_division(self):
		result = calc.division(5,4)
		self.assertEqual(result,1.25)

if __name__ =="__main__":
	unittest.main()