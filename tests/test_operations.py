import pytest
from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide


def test_operation(a, b, operation, expected):
    '''Testing various operations'''
    calculation = Calculation(a, b, operation)
    assert calculation.perform() == expected, f"{operation.__name__} operation failed"

# Keeping the divide by zero test as is since it tests a specific case
def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()