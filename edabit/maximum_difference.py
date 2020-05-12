"""
Given a list of integers, return the difference between the largest and smallest integers in the list.
Examples

difference([10, 15, 20, 2, 10, 6]) ➞ 18
# 20 - 2 = 18
difference([-3, 4, -9, -1, -2, 15]) ➞ 24
# 15 - (-9) = 24
difference([4, 17, 12, 2, 10, 2]) ➞ 15
17 - 2 = 15
"""
import unittest


def difference(nums):
    return max(nums) - min(nums)


class DifferenceTest(unittest.TestCase):

    def test_difference_return_integer(self):
        assert isinstance(difference([1]), int)

    def test_difference_list_of_one(self):
        expected = difference([1])
        self.assertEqual(expected, 0)

    def test_difference_list_two_n1(self):
        expected = difference([1, 2])
        self.assertEqual(expected, 1)

    def test_difference_list_two_n2(self):
        expected = difference([1, 1])
        self.assertEqual(expected, 0)

    def test_difference_list_two_n3(self):
        expected = difference([1, 5])
        self.assertEqual(expected, 4)

    def test_difference_list_three_n1(self):
        expected = difference([1, 2, 3])
        self.assertEqual(expected, 2)

    def test_difference_list_three_n2(self):
        expected = difference([2, 2, 2])
        self.assertEqual(expected, 0)

    def test_difference_list_three_n3(self):
        expected = difference([1, 2, 7])
        self.assertEqual(expected, 6)
