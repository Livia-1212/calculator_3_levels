'''My Test'''
import sys
sys.path.append('/Users/liviali/Documents/'+
                'NJIT/Fall_2024/WebSystemDev_IS601853/'+
                'GitHubHomework/Projects3/calculator_3_levels')

from calculator._init_ import Calculator # type: ignore

from calculator.sample import add, subtract, multiply, divide
def test_addition():
    '''Test that addition function works '''    
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert Calculator.subtract(2,2) == 0

def test_multiply():
    '''Test that addition function works '''    
    assert Calculator.multiply(2,2) == 4

def test_divide():
    '''Test that addition function works '''    
    assert Calculator.divide(2,2) == 1
