from pytest import *
from account import Account

class Test:
    def setup_method(self):
        self.acc = Account('John')

    def teardown_method(self):
        del self.acc

    def test_init(self):
        assert self.acc.get_name() == "John"
        assert self.acc.get_balance() == 0


    def test_deposit(self):
        assert self.acc.deposit(-100) is False
        assert self.acc.get_balance() == 0

        assert self.acc.deposit(0) is False
        assert self.acc.get_balance() == 0

        assert self.acc.deposit(100) is True
        assert self.acc.get_balance() == 100

    def test_withdraw(self):
        assert self.acc.deposit(100) is True
        assert self.acc.get_balance() == 100

        assert self.acc.withdraw(-20) is False
        assert self.acc.get_balance() == 100

        assert self.acc.withdraw(0) is False
        assert self.acc.get_balance() == 100

        assert self.acc.withdraw(500) is False
        assert self.acc.get_balance() == 100

        assert self.acc.withdraw(50) is True
        assert self.acc.get_balance() == 50
