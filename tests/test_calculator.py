'''My Calculator Test'''
from calculator import add, subtract, multiply, divide
from calculator import add, subtract

def test_addition():
    '''Test that addition function works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(2,2) == 0
    
def test_multiplication():
    '''Test that addition function works '''    
    assert multiply(2,2) == 4

def test_division():
    '''Test that addition function works '''    
    assert divide(2,2) == 1