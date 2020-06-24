import unittest
from solution import *
import random
import string


def correct_fib(n):
	"""correct implementation for this test"""
	if n == 2:
		return 1
	elif n == 1:
		return 0
	else:
		return correct_fib(n-1) + correct_fib(n-2)

def correct_palindrome(string):
	new_str = ""
	for i in string:
		if i.isalnum():
			new_str += (i)
	return new_str.lower()[::-1] == new_str.lower()

def random_num(n):
	return random.choice([i for i in range(n+1)])

def random_str(n):
	ans = ""
	for i in range(n):
		ans += random.choice(string.ascii_letters)
	return ans

class NthFib(unittest.TestCase):
	def test_1(self):
		"""Test for fib when n = 2"""
		assert 1 == nth_fib(2)
	def test_2(self):
		"""Test for fib when n = 6"""
		assert 5 == nth_fib(6)
	def test_3(self):
		num = random_num(15)
		"""random test 1, expected {num}, actual {nth_fib(num)}"""
		assert correct_fib(num) == nth_fib(num)
	def test_4(self):
		num = random_num(15)
		"""random test 2, expected {num}, actual {nth_fib(num)}"""
		assert correct_fib(num) == nth_fib(num)
	def test_5(self):
		num = random_num(15)
		"""random test 3, expected {num}, actual {nth_fib(num)}"""
		assert correct_fib(num) == nth_fib(num)
	def test_6(self):
		num = random_num(15)
		"""random test 4, expected {num}, actual {nth_fib(num)}"""
		assert correct_fib(num) == nth_fib(num)
	def test_7(self):
		num = random_num(15)
		"""random test 5, expected {num}, actual {nth_fib(num)}"""
		assert correct_fib(num) == nth_fib(num)

# Testcase and question description are from: https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/javascript-algorithms-and-data-structures-projects/palindrome-checker
class PalindromeChecker(unittest.TestCase):
	def test_2(self):
		"""palindrome("eye") should return true."""
		assert palindrome("eye") == True

	def test_3(self):
		"""palindrome("_eye") should return true."""
		assert palindrome("_eye") == True

	def test_4(self):
		"""palindrome("race car") should return true."""
		assert palindrome("race car") == True

	def test_5(self):
		"""palindrome("not a palindrome") should return false."""
		assert palindrome("not a palindrome") == False

	def test_6(self):
		"""palindrome("A man, a plan, a canal. Panama") should return true."""
		assert palindrome("A man, a plan, a canal. Panama") == True

	def test_7(self):
		"""palindrome("never odd or even") should return true."""
		assert palindrome("never odd or even") == True

	def test_8(self):
		"""palindrome("nope") should return false."""
		assert palindrome("nope") == False

	def test_9(self):
		"""palindrome("almostomla") should return false."""
		assert palindrome("almostomla") == False

	def test_10(self):
		"""palindrome("My age is 0, 0 si ega ym.") should return true."""
		assert palindrome("My age is 0, 0 si ega ym.") == True

"""if __name__ == "__main__":
	unittest.main()"""