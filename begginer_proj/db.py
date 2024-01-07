
import math

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"


def power(x, y):
    return math.pow(x, y)


def avg(x, y):
    return (x+y)/2


def remain(x, y):
    return x % y


def max(x, y):
    if x >= y:
        return x
    return y


def min(x, y):
    if x <= y:
        return x
    return y


def azeret(x, y= None):
    if x == 0:
        return 1
    return x * azeret(x-1)


def neg(x, y=None):
    return x*-1


def default_operation():
    return "Invalid operator"


def calc(operator, x, y):
    operator_dict = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '^': power,
        '@': avg,
        '$': max,
        '&': min,
        '%': remain,
        '~': neg,
        '!': azeret
    }

    # Use get() method to retrieve the function for the given operator
    operation = operator_dict.get(operator, lambda x, y: "Invalid operator")

    # Call the selected function
    result = operation(x, y)
    return result
