"""
Create a function that takes a list and returns the sum of all numbers in the list.
Examples

get_sum_of_elements([2, 7, 4]) ➞ 13
get_sum_of_elements([45, 3, 0]) ➞ 48
get_sum_of_elements([-2, 84, 23]) ➞ 105
"""
import unittest


def get_sum_of_elements(lst):
    return sum(lst)


class GetSumOfElementsTest(unittest.TestCase):

    def test_get_sum_of_elements_list_of_one1(self):
        self.assertEqual(get_sum_of_elements([1]), 1)

    def test_get_sum_of_elements_list_of_one2(self):
        self.assertEqual(get_sum_of_elements([2]), 2)

    def test_get_sum_of_elements_list_of_one3(self):
        self.assertEqual(get_sum_of_elements([9]), 9)

    def test_get_sum_of_elements_list_of_two1(self):
        self.assertEqual(get_sum_of_elements([1, 2]), 3)

    def test_get_sum_of_elements_list_of_two2(self):
        self.assertEqual(get_sum_of_elements([2, 3]), 5)

    def test_get_sum_of_elements_list_of_two3(self):
        self.assertEqual(get_sum_of_elements([9, 10]), 19)

    def test_get_sum_of_elements_list_of_three1(self):
        self.assertEqual(get_sum_of_elements([1, 2, 3]), 6)

    def test_get_sum_of_elements_list_of_three2(self):
        self.assertEqual(get_sum_of_elements([2, 3, 4]), 9)

    def test_get_sum_of_elements_list_of_three3(self):
        self.assertEqual(get_sum_of_elements([9, 10, 11]), 30)
