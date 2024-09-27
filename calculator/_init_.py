'''Calculator class '''
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(a,b):
        # Pass the add function from calculator.operations
        calculation = Calculation(a, b, add)
        return calculation.get_result()
    @staticmethod
    def subtract(a,b):
        # Pass the add function from calculator.operations
        calculation = Calculation(a, b, subtract)
        return calculation.get_result()
    @staticmethod
    def multiply (a,b):
        # Pass the add function from calculator.operations
        calculation = Calculation(a, b, multiply)
        return calculation.get_result()
    @staticmethod
    def divide(a,b):
        # Pass the add function from calculator.operations
        calculation = Calculation(a, b, divide)
        return calculation.get_result()
