"""
Create a function that takes two strings as arguments and return either True or False depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.
Examples

comp("AB", "CD") ➞ True
comp("ABC", "DE") ➞ False
comp("hello", "edabit") ➞ False
"""
import unittest


def comp(txt1, txt2):
    return len(txt1) == len(txt2)


class CompTest(unittest.TestCase):

    def test_comp_return_true(self):
        ret_value = comp('txt1', 'txt2')
        self.assertEqual(True, ret_value)

    def test_comp_return_false(self):
        ret_value = comp('txt', 'txt2')
        self.assertEqual(False, ret_value)

    def test_edabit_test_cases(self):
        self.assertEqual(comp("AB", "CD"), True)
        self.assertEqual(comp("ABC", "DE"), False)
        self.assertEqual(comp("hello", "edabit"), False)


if __name__ == '__main__':
    unittest.main()
