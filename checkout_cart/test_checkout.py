"""
Can create an instance of the Checkout Class -ok
Can add an item price -ok
Can add an item -ok
Can calculate the current total -ok
Can add multiple items and get correct total -ok
Can add discount rules
Can apply discount rules to the total
Exception is thrown for item added without a price
"""
import pytest

from checkout_cart.checkout import Checkout


@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.add_item_price("a", 1)
    checkout.add_item_price("b", 2)
    return checkout


def test_can_calculate_total(checkout):
    checkout.add_item("a")
    assert checkout.calculate_total() == 1


def test_get_correct_total_multiple_items(checkout):
    checkout.add_item("a")
    checkout.add_item("b")
    assert checkout.calculate_total() == 3


def test_can_add_discount_rule(checkout):
    checkout.add_discount("a", 3, 2)


def test_can_apply_discount_rule(checkout):
    checkout.add_discount("a", 3, 2)
    checkout.add_item("a")
    checkout.add_item("a")
    checkout.add_item("a")
    assert checkout.calculate_total() == 2

