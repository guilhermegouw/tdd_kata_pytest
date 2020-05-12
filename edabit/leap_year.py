def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


def check_leap_year(year, expected_result):
    ret_val = leap_year(year)
    assert ret_val == expected_result


def test_not_divisible_by_4_return_false():
    check_leap_year(1995, False)


def test_divisible_by_4_return_true():
    check_leap_year(1996, True)


def test_divisible_by_4_and_100_return_false():
    check_leap_year(2100, False)


def test_divisible_by_4_and_100_and_400_return_true():
    check_leap_year(2000, True)
