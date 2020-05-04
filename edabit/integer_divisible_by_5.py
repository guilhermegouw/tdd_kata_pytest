'''
Create a function that returns True if an integer is evenly divisible by 5, and False otherwise.
Examples

divisible_by_five(5) ➞ True
divisible_by_five(-55) ➞ True
divisible_by_five(37) ➞ False
'''


def divisible_by_five(n):
    return (n % 5) == 0


def test_divisible_by_five_1():
    return_value = divisible_by_five(5)
    assert return_value is True


def test_divisible_by_five_2():
    return_value = divisible_by_five(55)
    assert return_value is True


def test_divisible_by_five_3():
    return_value = divisible_by_five(37)
    assert return_value is False
