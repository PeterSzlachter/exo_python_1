from bank import Account


def test_deposit():
    account = Account(initial_balance=1000)
    account.deposit(amount=1000)
    assert account.balance == 2000


def test_withdraw():
    account = Account(initial_balance=1000)
    account.withdraw(amount=500)
    assert account.balance == 500


def test__create_identifier():
    assert False
