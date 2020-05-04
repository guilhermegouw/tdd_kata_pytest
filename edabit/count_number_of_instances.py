"""
Count Number of Instances

Create a class named User and create a way to check the number of users (number of instances) were created, so that the value can be accessed as a class attribute.
Examples

u1 = User("johnsmith10")
User.user_count ➞ 1
u2 = User("marysue1989")
User.user_count ➞ 2
u3 = User("milan_rodrick")
User.user_count ➞ 3

Make sure that the usernames are accessible via the instance attribute username.

u1.username ➞ "johnsmith10"
u2.username ➞ "marysue1989"
u3.username ➞ "milan_rodrick"
"""
import pytest


class User:
    number_of_users = 0

    def __init__(self, username):
        self.username = username
        User.number_of_users += 1


@pytest.fixture
def set_up():
    u1 = User('johnsmith10')
    u2 = User("marysue1989")
    u3 = User("milan_rodrick")


def test_User_1(set_up):
    u1 = User('johnsmith10')
    assert u1.number_of_users == 1


def test_User_2(set_up):
    u1 = User('johnsmith10')
    u2 = User("marysue1989")
    assert User.number_of_users == 2
