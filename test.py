import unittest
from solution import *
import random

def correct_fib(n):
	"""correct implementation for this test"""
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return correct_fib(n-1)+correct_fib(n-2)

def random_num(n):
	return random.choice([i for i in range(n+1)])

class TestCase(unittest.TestCase):
	def test_1(self):
		"""Test for fib when n = 2"""
		assert 1 == nth_fib(2)
	def test_2(self):
		"""Test for fib when n = 9"""
		assert 34 == nth_fib(9)
	def test_3(self):
		num = random_num(20)
		f"""random test 1, expected {num}, actual {nth_fib(num)}"""
		assert correct_fib(num) == nth_fib(num)
	def test_4(self):
		num = random_num(20)
		f"""random test 2, expected {num}, actual {nth_fib(num)}"""
		assert correct_fib(num) == nth_fib(num)
	def test_5(self):
		num = random_num(20)
		f"""random test 3, expected {num}, actual {nth_fib(num)}"""
		assert correct_fib(num) == nth_fib(num)
	def test_6(self):
		num = random_num(20)
		f"""random test 4, expected {num}, actual {nth_fib(num)}"""
		assert correct_fib(num) == nth_fib(num)
	def test_7(self):
		num = random_num(20)
		f"""random test 5, expected {num}, actual {nth_fib(num)}"""
		num = random_num(20)
		assert correct_fib(num) == nth_fib(num)

if __name__ == "__main__":
	unittest.main()