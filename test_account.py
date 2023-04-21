import pytest
from account import Account

def test_init():
    acc = Account("John")
    assert acc.get_name() == "John"
    assert acc.get_balance() == 0

def test_deposit():
    acc = Account("John")
    assert acc.deposit(-100) is False
    assert acc.deposit(0) is False
    assert acc.deposit(100) is True
    assert acc.get_balance() == 100

def test_withdraw():

    acc = Account("John")
    assert acc.deposit(100) is True

    assert acc.get_balance() == 100

    assert acc.withdraw(50) is True
    assert acc.get_balance() == 50

    assert acc.withdraw(-20) is False
    assert acc.get_balance() == 50

    assert acc.withdraw(100) is False
    assert acc.get_balance() == 50

    assert acc.withdraw(0) is False
    assert acc.get_balance() == 50
