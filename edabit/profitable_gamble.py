"""
Create a function that takes in three arguments (prob, prize, pay) and returns true if prob * prize > pay;
otherwise return false.
To illustrate, profitable_gamble(0.2, 50, 9) should yield true, since the net profit is 1 (0.2 * 50 - 9), and 1 > 0.
Examples

profitable_gamble(0.2, 50, 9) ➞ True
profitable_gamble(0.9, 1, 2) ➞ False
profitable_gamble(0.9, 3, 2) ➞ True
"""
import unittest


def profitable_gamble(prob, prize, pay):
    return prob * prize > pay


class ProfitableGambleTest(unittest.TestCase):

    def test_profitable_gamble_return_true(self):
        ret_value = profitable_gamble(0.2, 50, 9)
        self.assertEqual(True, ret_value)

    def test_profitable_gamble_return_false(self):
        ret_value = profitable_gamble(0.9, 1, 2)
        self.assertEqual(False, ret_value)


if __name__ == '__main__':
    unittest.main()
