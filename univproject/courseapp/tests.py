from django.test import TestCase
from unittest import skip

def add(a, b):
   return a + b

class SmokeTest(TestCase):

   # Checks if 1 + 1 equals 2, and it should pass
   def test_one_plus_one_is_two(self):
       self.assertEqual(1 + 1, 2)

   # Checks if 1 + 1 equals 3, and it should  pass to demonstrate a failing test
   def test_one_plus_one_is_three(self):
       self.assertEqual(1 + 1, 3)

   # Calls the add function with arguments 1 and 1 and asserts that the result is 2. This test should pass.
   def test_one_add_one(self):
       self.assertEqual(add(1, 1), 2)
   
   # # Test is marked with @skip("no time now"), it will be skipped and won't be executed.
   # @skip("no time now")
   # def test_todo(self):
       # self.fail("to do")
