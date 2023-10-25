

class Calculator:
    # method to divide two numbers
    @staticmethod
    def divide(a: int, b: int) -> float:
        # raise an exception if the denominator is zero
        if b == 0:
            raise ZeroDivisionError
        return a/b
    # method to subtract two numbers
    @staticmethod
    def subtract(a: int, b: int) -> int:
        return b - a