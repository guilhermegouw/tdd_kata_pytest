from pytest import raises


def raise_value_exception():
    raise ValueError


def test_exception():
    with raises(ValueError):
        raise_value_exception()
