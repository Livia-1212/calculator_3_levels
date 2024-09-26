'''My Test'''
import sys
sys.path.append('/Users/liviali/Documents/'+
                'NJIT/Fall_2024/WebSystemDev_IS601853/'+
                'GitHubHomework/Projects3/calculator_3_levels')

from calculator.sample import add, subtract
def test_addition():
    '''Test that addition function works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(2,2) == 0
