import unittest

from opa.week1.assignments import divide_apples

class TestStringMethods(unittest.TestCase):

  def test_common_case(self):
      n = 3
      k = 14
      expected_result = 4
      actual_resulst = divide_apples(n, k)
      self.assertEqual(actual_resulst, expected_result)

  def test_common_case2(self):
      n = 1
      k = 14
      expected_result = k
      actual_resulst = divide_apples(n, k)
      self.assertEqual(actual_resulst, expected_result)

  def test_common_case3(self):
      n = 6
      k = 3
      expected_result = 0
      actual_resulst = divide_apples(n, k)
      self.assertEqual(actual_resulst, expected_result)
