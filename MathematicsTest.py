import unittest
from Mathematics import Mathematics
import random

class MatematicsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mIns = Mathematics()

    def setUp(self):
        self.first_num = random.randint(1, 100)
        self.second_num = random.randint(1, 100)
        self.expected_sum = self.first_num + self.second_num
        self.expected_multi = self.first_num * self.second_num

    def test_can_add(self):
        actual_sum = self.mIns.addition(self.first_num, self.second_num)
        self.assertEqual(actual_sum, self.expected_sum)

    def test_can_multiply(self):
        actual_multi = self.mIns.multiplication(self.first_num, self.second_num)
        self.assertEqual(actual_multi, self.expected_multi)

if __name__ == "__main__":
    unittest.main()
