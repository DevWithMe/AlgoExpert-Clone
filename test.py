import unittest
from solution import *

class TestCase(unittest.TestCase):
	def test_1(self):
		assert "hello" == hello()
	def test_2(self):
		assert "hello" != hello()
	def test_3(self):
		assert "hello" != hello()

if __name__ == "__main__":
	unittest.main()