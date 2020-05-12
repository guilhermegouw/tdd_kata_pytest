"""
Write a function that counts the number of times a specific digit occurs in a range (inclusive).
The function will look like:
digit_occurrences(start, end, digit) ➞ number of times digit occurs

Examples

digit_occurrences(51, 55, 5) ➞ 6
# [51, 52, 53, 54, 55] : 5 occurs 6 times
digit_occurrences(1, 8, 9) ➞ 0
digit_occurrences(-8, -1, 8) ➞ 1
digit_occurrences(71, 77, 2) ➞ 1
"""
import unittest


def digit_occurrences(start, end, digit):
    interval = range(start, end + 1)
    count = 0
    for num in interval:
        num_string = str(abs(num))
        for letter in num_string:
            if letter == str(digit):
                count += 1
            continue
    return count


class DigitOccurrencesTest(unittest.TestCase):

    def test_digit_occurences_no_occurences(self):
        ret_value = digit_occurrences(1, 8, 9)
        self.assertEqual(ret_value, 0)

    def test_digit_occurences_single_digits(self):
        ret_value = digit_occurrences(1, 9, 9)
        self.assertEqual(ret_value, 1)

    def test_digit_occurences_single_digits_2(self):
        ret_value = digit_occurrences(-8, -1, 8)
        self.assertEqual(ret_value, 1)

    def test_digit_occurences_double_digits_1(self):
        ret_value = digit_occurrences(1, 10, 1)
        self.assertEqual(ret_value, 2)

    def test_digit_occurences_double_digits_2(self):
        ret_value = digit_occurrences(1, 11, 1)
        self.assertEqual(ret_value, 4)

    def test_digit_occurences_double_digits_3(self):
        ret_value = digit_occurrences(1, 12, 1)
        self.assertEqual(ret_value, 5)
