'''
Python has a logical operator and, which can also be written as &. The and operator takes two boolean values, and returns true if both values are true.

Consider a and b:

  - `a` is checked if it is `True` or `False`.
  - If `a` is `False`,  `False` is returned
  - `b` is checked if it is `True` or `False`.
  - If `b` is `False`, `False` is returned
  - Otherwise, `True` is returned (as both `a` and `b` are therefore `True` )

The and operator will only return True for True and True.
Make a function using the and operator.
Examples

And(True, False) ➞ False
And(True, True) ➞ True
And(False, True) ➞ False
And(False, False) ➞ False
'''


def and_operator(a, b):
    return a and b


def test_and_operator_1():
    return_value = and_operator(True, False)
    assert return_value is False


def test_and_operator_2():
    return_value = and_operator(True, True)
    assert return_value is True


def test_and_operator_3():
    return_value = and_operator(False, False)
    assert return_value is False
