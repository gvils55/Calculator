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
    """
    :param x: a curtain operand
    :param y: a curtain operand
    :return: the addition calculation between the 2 operands
    """
    return x + y


def subtract(x, y):
    """
    :param x: a curtain operand
    :param y: a curtain operand
    :return: the subtraction calculation between the 2 operands
    """
    return x - y


def multiply(x, y):
    """
    :param x: a curtain operand
    :param y: a curtain operand
    :return: the multiplication  calculation between the 2 operands
    """
    return x * y


def divide(x, y):
    """
    :param x: a curtain operand
    :param y: a curtain operand
    :return: the division calculation between the 2 operands
    """
    if y != 0:
        return x / y
    else:
        raise ValueError


def power(x, y):
    """
    :param x: a curtain operand
    :param y: a curtain operand
    :return: Calculation of the power between the 2 operands
    """
    return x**y


def avg(x, y):
    """
    :param x: a curtain operand
    :param y: a curtain operand
    :return: Calculation of the average between the 2 operands
    """
    return (x+y)/2


def remain(x, y):
    """
    :param x: a curtain operand
    :param y: a curtain operand
    :return: the remains of the calculation of the division between the 2 operands
    """
    return x % y


def max(x, y):
    """
    :param x: a curtain operand
    :param y: a curtain operand
    :return: the bigger operand of the two
    """
    if x >= y:
        return x
    return y


def min(x, y):
    """
    :param x: a curtain operand
    :param y: a curtain operand
    :return: the smaller operand of the two
    """
    if x <= y:
        return x
    return y


def azeret(x, y= None):
    """
    :param x: a curtain operand
    :return: the factorial of the given operand
    """
    try:
        if x == 0:
            return 1
        if x < 0:
            raise ValueError
        return x * azeret(x-1)
    except RecursionError:
        raise OverflowError


def neg(x, y=None):
    """
    :param x: a curtain operand
    :return: the opposite value of the given operand
    """
    return x*-1

def digit_sum(x, y= None):
    """
    :param x: a curtain operand
    :return: the sum of the digits in the given operand
    """
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
    """
    :param operator: a curtain operator
    :param x: a curtain operand
    :param y: a curtain operand
    :return: the calculation of the two given operands with the given operator
    """
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