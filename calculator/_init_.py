class calculator:
    @staticmethod
    def add (a,b):
        calculation = Calculation(a, b, add)
        return calculation.get_result()
    @staticmethod 
    def subtract (a,b):
        calculation = Calculation(a,b, subtract)
        return calculation.get_result()
    @staticmethod 
    def multiply (a,b):
        calculation = Calculation(a,b, multiply)
        return calculation.get_result()
    @staticmethod 
    def divide(a,b):
        calculation = Calculation(a,b, divide)
        return calculation.get_result()
    