"""
Create a function that takes a string of words and return a string sorted alphabetically
by the last character of each word.

Examples

sort_by_last("herb camera dynamic") ➞ "camera herb dynamic"
sort_by_last("stab traction artist approach") ➞ "stab approach traction artist"
sort_by_last("sample partner autonomy swallow trend") ➞ "trend sample partner swallow autonomy"
"""
import unittest


def sort_by_last(txt):
    return ' '.join(sorted(txt.split(), key=lambda x: x[-1]))


class SortByLastTest(unittest.TestCase):

    def test_sort_by_last_one_word(self):
        ret_value = sort_by_last('luciana')
        self.assertEqual(ret_value, 'luciana')

    def test_sort_by_last_two_words(self):
        ret_value = sort_by_last('guilherme luciana')
        self.assertEqual(ret_value, 'luciana guilherme')

    def test_sort_by_last_many_words1(self):
        ret_value = sort_by_last("herb camera dynamic")
        self.assertEqual(ret_value, "camera herb dynamic")

    def test_sort_by_last_two_words2(self):
        ret_value = sort_by_last("stab traction artist approach")
        self.assertEqual(ret_value, "stab approach traction artist")

    def test_sort_by_last_two_words3(self):
        ret_value = sort_by_last("sample partner autonomy swallow trend")
        self.assertEqual(ret_value, "trend sample partner swallow autonomy")
