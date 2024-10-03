'''My Calculator Test'''
import sys
from decimal import Decimal
from typing import List
sys.path.append('/Users/liviali/Documents/'+
                'NJIT/Fall_2024/WebSystemDev_IS601853/'+
                'GitHubHomework/Projects3/calculator_3_levels')
# Fix wrong import order by placing standard imports before third-party imports
import pytest
# Removed redundant import of Calculation and Calculations; assuming correct import paths
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

# If you need custom behavior, rename this function and adjust its usage

history: List[Calculation] = Calculations.get_history()

@pytest.fixture
def setup_calculations():
    """Clear history and add sample calculations for tests."""
    Calculations.clear_history()  # Ensure a clean state before each test
    # Adding sample calculations to the history for tests
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

def test_add_calculation():
    """Test adding a calculation."""
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history"

def test_get_history():
    """Test retrieving calculation history."""
    calc1 = Calculation(Decimal('2'), Decimal('2'), add)
    calc2 = Calculation(Decimal('3'), Decimal('1'), subtract)
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)
    assert len(history) == 3, "History does not contain the expected number of calculations"

def test_clear_history():
    """Test clearing the calculation history."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared"

def test_get_latest():
    """Test getting the latest calculation."""
    calc = Calculation(Decimal('20'), Decimal('3'), add)  # Create a Calculation object
    Calculations.add_calculation(calc)

    print("Current history:", Calculations.get_history())

    latest = Calculations.get_latest()
    print("Latest calculation:", latest)

    assert latest is not None, "Latest calculation should not be None"
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Did not get the correct latest calculation"

def test_find_by_operation():
    """Test finding calculations by operation type."""
    calc_add = Calculation(Decimal('5'), Decimal('3'), add)
    Calculations.add_calculation(calc_add)
    calc_subtract = Calculation(Decimal('10'), Decimal('4'), subtract)
    Calculations.add_calculation(calc_subtract)
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 2, "Did not find the correct number of calculations with add operation"
    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 1, "Did not find the correct number of calculations with subtract operation"

def test_get_latest_with_empty_history():
    """Test getting the latest calculation when history is empty."""
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected None for latest calculation with empty history"