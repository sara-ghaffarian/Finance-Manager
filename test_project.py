from project import FinanceManager
from project import validate_amount
from project import validate_transaction_type

def test_add_transaction_income():
    manager = FinanceManager()
    manager.add_transaction(1000, "salary", "income")

    assert len(manager.transactions) == 1
    assert manager.transactions[0].amount == 1000
    assert manager.transactions[0].category == "salary"
    assert manager.transactions[0].transaction_type == "income"


def test_add_transaction_expense():
    manager = FinanceManager()
    manager.add_transaction(500, "food", "expense")

    assert len(manager.transactions) == 1
    assert manager.transactions[0].transaction_type == "expense"


def test_calculate_balance_basic():
    manager = FinanceManager()
    manager.add_transaction(1000, "salary", "income")
    manager.add_transaction(300, "food", "expense")
    manager.add_transaction(200, "rent", "expense")

    assert manager.calculate_balance() == 500


def test_get_total_income():
    manager = FinanceManager()
    manager.add_transaction(1000, "salary", "income")
    manager.add_transaction(500, "bonus", "income")

    assert manager.get_total_income() == 1500


def test_get_total_expense():
    manager = FinanceManager()
    manager.add_transaction(300, "food", "expense")
    manager.add_transaction(200, "rent", "expense")

    assert manager.get_total_expense() == 500


def test_get_top_category():
    manager = FinanceManager()
    manager.add_transaction(300, "food", "expense")
    manager.add_transaction(500, "rent", "expense")
    manager.add_transaction(200, "food", "expense")

    # food = 500, rent = 500 → یکی از این دو قابل قبوله
    result = manager.get_top_category()
    assert result in ["food", "rent"]


def test_delete_transaction():
    manager = FinanceManager()
    manager.add_transaction(100, "test", "expense")

    assert len(manager.transactions) == 1

    manager.delete_transaction(0)

    assert len(manager.transactions) == 0


def test_balance_empty():
    manager = FinanceManager()

    assert manager.calculate_balance() == 0


def test_top_category_empty():
    manager = FinanceManager()

    assert manager.get_top_category() is None


def test_validate_amount():

    assert validate_amount(100) == True
    assert validate_amount(1) == True
    assert validate_amount(0) == False
    assert validate_amount(-10) == False


def test_validate_transaction_type():

    assert validate_transaction_type("income") == True
    assert validate_transaction_type("expense") == True
    assert validate_transaction_type("food") == False


def test_search_by_category():

    manager = FinanceManager()
    manager.add_transaction(100, "food", "expense")
    manager.add_transaction(200, "food", "expense")
    result = manager.search_by_category("food")

    assert len(result) == 2

