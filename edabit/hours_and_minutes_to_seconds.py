'''
Write a function that takes two integers (hours, minutes) and converts them into seconds.
Examples

convert(1, 3) ➞ 3780
convert(2, 0) ➞ 7200
convert(0, 0) ➞ 0
'''


def convert(hours, minutes):
    return (hours * 3600) + (minutes * 60)


def test_convert_1():
    return_value = convert(1, 3)
    assert return_value == 3780


def test_convert_2():
    return_value = convert(2, 0)
    assert return_value == 7200


def test_convert_3():
    return_value = convert(0, 0)
    assert return_value == 0
