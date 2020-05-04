'''
Given two numbers, return True if the sum of both numbers is less than 100. Otherwise return False.
Examples

less_than_100(22, 15) ➞ True
# 22 + 15 = 37
less_than_100(83, 34) ➞ False
# 83 + 34 = 117
'''


def less_than_100(a, b):
    return a + b < 100


def test_less_than_100_1():
    return_value =less_than_100(22, 15)
    assert return_value == True


def test_less_than_100_2():
    return_value =less_than_100(83, 34)
    assert return_value == False


def test_less_than_100_3():
    return_value =less_than_100(0, 100)
    assert return_value == False