from db import *

operator_dict = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,
        '@': 5,
        '$': 5,
        '&': 5,
        '%': 4,
        '~': 6,
        '!': 6,
    }
def get_expression():
    while True:
        math_expr = input("enter a math expression:")
        try:
            stc = expr_list(math_expr)
            if has_invalid_spaces(stc):
                stc = remove_spaces(stc)
                if has_valid_symbols(stc) and has_wrong_symbol_placements(stc):
                    new_s = change_minuses(stc)
                    return new_s
                else:
                    print("invalid chars for the the math expression")
            else:
                print("invalid spaces, there are some operands that are not separated by an operator")

        except ValueError as ae:
            print("invalid input")


def expr_list(math_expr: str):
    stack = []
    i = 0

    while i < (len(math_expr)):
        num = ''
        j = i
        is_num = False
        while j < len(math_expr) and (math_expr[j].isnumeric() or math_expr[j] == '.'):
            is_num = True
            num = num + math_expr[j]
            j = j + 1
        i = j
        if is_num:
            stack.append(float(num))
        else:
            stack.append(math_expr[i])
            i = i + 1

    return stack


def has_wrong_symbol_placements(exp_list:list):
    if len(exp_list) == 1 and exp_list[0] in operator_dict:
        return False

    elif exp_list[0] in operator_dict:
        if exp_list[0] != '~' and exp_list[0] != '-':
            return False

    for i in range(len(exp_list)-1):
        if exp_list[i] == '!' and isinstance(exp_list[i+1], float) or exp_list[i+1] == '~' and isinstance(exp_list[i], float):
            return False
    return True


def remove_spaces(exp_list:list):
    new_list = []
    for i in range(len(exp_list)):
        if exp_list[i] != ' ':
            new_list.append(exp_list[i])
    return new_list


def has_valid_symbols(exp_list:str):
    for i in range(len(exp_list)):
        if (not isinstance(exp_list[i], float)) and exp_list[i] not in operator_dict:
            if exp_list[i] != '(' and exp_list[i] != ')':
                return False
    return True


def has_invalid_spaces(exp_list:list):
    for i in range(len(exp_list)-1):
        if isinstance(exp_list[i], float) and exp_list[i+1] == ' ':
            j = i
            while j+1 < len(exp_list) and exp_list[j+1] == ' ':
                 j = j +1
            if exp_list[j+1] not in operator_dict:
                return False
    return True


def change_minuses(exp_list:list):
    new_list = []
    i = 0
    count = 0
    if exp_list[0] == '-':

        while i < len(exp_list) and exp_list[i] == '-':
            count = count + 1
            i = i + 1
        if isinstance(exp_list[i], float):
            if count % 2 == 0:
                exp_list[i] = exp_list[i] * -1
            new_list.append(exp_list[i])
            i=i+1
        else:
            raise ValueError

    while i < len(exp_list):
        new_list.append(exp_list[i])

        if (exp_list[i] in operator_dict or exp_list[i] == '(') and (exp_list[i] != '!'):

            if i + 1 == len(exp_list):
                if exp_list[i] != '!':
                    raise ValueError

            elif exp_list[i + 1] == '-':
                j = i + 1
                count = 0
                while j < len(exp_list) - 1 and exp_list[j + 1] == '-':
                    count = count + 1
                    j = j + 1
                i = j + 1
                if isinstance(exp_list[i], float):
                    if count % 2 == 0:
                        exp_list[i] = exp_list[i] * -1
                    new_list.append(exp_list[i])


                else:
                    raise ValueError
        i = i + 1

    return new_list



def hasHigherPrecedence(operator1, operator2):
    return operator_dict[operator1] >= operator_dict[operator2]


def to_postfix(exp_list:list):


    post_list = []
    operator_stack = []

    for obj in exp_list:

        if obj in operator_dict:

            while operator_stack and operator_stack[-1] != '(' and hasHigherPrecedence(operator_stack[-1], obj):
                op1 = operator_stack.pop()
                post_list.append(op1)
            operator_stack.append(obj)


        elif obj not in operator_dict and obj not in ['(', ')']:
            post_list.append(obj)


        elif obj == '(':
            operator_stack.append(obj)


        elif obj == ')':

            while operator_stack and operator_stack[-1] != '(':
                op1 = operator_stack.pop()
                post_list.append(op1)

            operator_stack.pop();

    while operator_stack:
        op1 = operator_stack.pop()
        post_list.append(op1)

    return post_list



def calculate_postfix(exp_list:list):

    try:
        result = exp_list[0]
        i = 0
        while i < len(exp_list):
            if exp_list[i] in operator_dict:
                if exp_list[i] == '!' or exp_list[i] == '~':
                    result = calc(exp_list[i], exp_list[i-1], None)
                    exp_list[i-1] = result
                    exp_list.pop(i)

                else:
                    result = calc(exp_list[i], exp_list[i - 2], exp_list[i - 1])
                    exp_list[i-2] = result
                    exp_list.pop(i)
                    exp_list.pop(i-1)

                i = 0
            i = i+1
        return result
    except Exception as ae:
        raise ArithmeticError


def main():

    while True:
        try:
            math_expr = get_expression()
            post_list = to_postfix(math_expr)
            print(post_list)
            result = calculate_postfix(post_list)
            print(result)
        except KeyboardInterrupt as ae:
            print("\nlogged out of console")
            break
        except ArithmeticError as ae:
            print("\namount of operators is not suitable for the amount of operands")
        except Exception as ae:
            print("invalid amount of Parenthesis")




if __name__ == '__main__':
    main()