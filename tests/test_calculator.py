<<<<<<< HEAD
'''My Calculator Test'''
from calculator._init_ import Calculator
=======
'''My Test'''
import sys
sys.path.append('/Users/liviali/Documents/'+
                'NJIT/Fall_2024/WebSystemDev_IS601853/'+
                'GitHubHomework/Projects3/calculator_3_levels')
>>>>>>> f511910b9e5e1e76d6ee3d7cf65d6edfabdd7f48

from calculator.sample import add, subtract
def test_addition():
    '''Test that addition function works '''    
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
<<<<<<< HEAD
    assert Calculator.subtract(2,2) == 0

def test_divide():
    '''Test that division function works '''    
    assert Calculator.divide(2,2) == 1

def test_multiply():
    '''Test that multiply function works '''    
    assert Calculator.multiply(2,2) == 4
=======
    assert subtract(2,2) == 0
>>>>>>> f511910b9e5e1e76d6ee3d7cf65d6edfabdd7f48
