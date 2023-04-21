class Account:

    def __init__(self, name: str) -> None:
        """Initialize a new Account object with the specified name and a balance of 0.
            :param name: The name associated with the account.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Add the specified amount to the account balance.
        :param amount: The amount to deposit.
        :return: True if the deposit transaction is successful, False otherwise.
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Subtract the specified amount from the account balance.
        :param amount: The amount to withdraw.
        :return: True if the withdrawal transaction is successful, False otherwise.
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """Return the current balance of the account.
            :return: The current balance of the account.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """Return the name associated with the account.
            :return: The name associated with the account.
        """
        return self.__account_name
