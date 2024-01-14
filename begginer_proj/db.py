operator_dict = {
        '+': (1, "both", True),
        '-': (1, "both", True),
        'u-': (1, "left", True),
        '*': (2, "both", True),
        '/': (2, "both", True),
        '^': (3, "both", True),
        '@': (5, "both", True),
        '$': (5, "both", True),
        '&': (5, "both", True),
        '%': (4, "both", True),
        '~': (6, "left", True),
        '!': (6, "right", False),
        '#': (6, "right", False),

}

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
        raise ValueError


def power(x, y):
    return x**y


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
    if x < 0:
        raise ValueError
    return x * azeret(x-1)


def neg(x, y=None):
    return x*-1

def digit_sum(x, y= None):
    if x < 0:
        raise ValueError
    count = 0
    num = str(x)
    l1 = []
    for i in range(len(num)):
        if num[i] != '.':
            l1.append(num[i])
    for j in range(len(l1)):
        count += int(l1[j])
    return count


def default_operation():
    return "Invalid operator"


def calc(operator, x, y):
    operator_dict_function = {
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
        'u-': neg,
        '!': azeret,
        '#': digit_sum
    }

    # Use get() method to retrieve the function for the given operator
    operation = operator_dict_function.get(operator, lambda x, y: "Invalid operator")

    # Call the selected function
    result = operation(x, y)
    return result