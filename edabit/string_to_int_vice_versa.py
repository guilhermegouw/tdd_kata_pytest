'''
Write two functions:
    to_int() : A function to convert a string to an integer.
    to_str() : A function to convert an integer to a string.
Examples

to_int("77") ➞ 77
to_int("532") ➞ 532
to_str(77) ➞ "77"
to_str(532) ➞ "532"
'''


def to_int(txt):
    return int(txt)


def to_str(num):
    return str(num)


def test_to_int_1():
    return_value = to_int('42')
    assert return_value == 42


def test_to_int_2():
    return_value = to_int('23')
    assert return_value == 23


def test_to_int_3():
    return_value = to_int('13')
    assert return_value == 13


def test_to_str_1():
    return_value = to_str(42)
    assert return_value == '42'


def test_to_str_2():
    return_value = to_str(23)
    assert return_value == '23'


def test_to_str_3():
    return_value = to_str(13)
    assert return_value == '13'
