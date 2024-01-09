from db_helper import *

class invalid_symbol_placements(Exception):
    def __int__(self):
        pass
    def __str__(self):
        return "invalid symbol placement"



def check_opr_placements(math_expr: list):
    pass


def handle_minuses(math_expr: list):
    new_list = []
    i = 0

    while i < len(math_expr):
        new_list.append(math_expr[i])

        if math_expr[i] in operator_dict or math_expr[i] == '(':
            if len(math_expr) == i+1:
                raise invalid_symbol_placements

            elif math_expr[i+1] == '-':
                count = 0
                opr = math_expr[i]
                if opr == '(':
                    can_be_with_opr = True
                else:
                    if opr == '-' and i == 0:
                        new_list.pop()
                    operator_tuple = operator_dict[opr]
                    can_be_with_opr = operator_tuple[2]

                if not can_be_with_opr:
                    new_list.append(math_expr[i+1])
                    count = -1
                j = i + 1
                while j < len(math_expr)-1 and math_expr[j] == '-':
                    count = count + 1
                    j = j + 1

                if isinstance(math_expr[j], float):
                    if count % 2 != 0:
                        math_expr[j] = math_expr[j] * -1
                    new_list.append(math_expr[j])
                    i = j
                else:
                    raise invalid_symbol_placements

        i = i + 1

    return new_list



def has_valid_parenthesis(math_expr: list):
    right_p_count = 0
    left_p_count = 0
    for obj in math_expr:
        if obj == '(':
            right_p_count = right_p_count+1
        elif obj == ')':
            left_p_count = left_p_count+1
    return left_p_count == right_p_count



def has_valid_symbols(math_expr: list):
    for obj in math_expr:
        if (not isinstance(obj, float)) and obj not in operator_dict:
            if obj != '(' and obj != ')':
                return False
    return True



def from_string_to_list(math_expr: str):
    l1 = []
    i = 0

    while i < len(math_expr):
        num = ''
        j = i
        is_num = False
        while j < len(math_expr) and (math_expr[j].isnumeric() or math_expr[j] == '.'):
            is_num = True
            num = num + math_expr[j]
            j = j + 1
        i = j
        if is_num:
            l1.append(float(num))
        else:
            if math_expr[i] != ' ' and math_expr[i] != '\t':
                l1.append(math_expr[i])
            i = i + 1

    return l1



def has_higher_equal_precedence(operator1, operator2):
    operator_tuple1 = operator_dict[operator1]
    operator_tuple2 = operator_dict[operator2]
    return operator_tuple1[0] >= operator_tuple2[0]



def to_postfix(exp_list: list):
    post_list = []
    operator_stack = []

    for obj in exp_list:

        if obj in operator_dict:

            while operator_stack and operator_stack[-1] != '(' and has_higher_equal_precedence(operator_stack[-1], obj):
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



def calculate_postfix(math_expr: list):

    i = 0
    result = math_expr[0]
    while i < len(math_expr):
        if math_expr[i] in operator_dict:
            operator_tuple = operator_dict[math_expr[i]]
            opr_dir = operator_tuple[1]
            if opr_dir != "both":
                result = calc(math_expr[i], math_expr[i - 1], None)
                math_expr[i - 1] = result
                math_expr.pop(i)

            else:
                result = calc(math_expr[i], math_expr[i - 2], math_expr[i - 1])
                math_expr[i - 2] = result
                math_expr.pop(i)
                math_expr.pop(i - 1)

            i = 0
        i = i + 1

    if len(math_expr) > 1:
        raise invalid_symbol_placements
    return result



def get_expression():
    while True:
        math_expr = input("enter a math expression: ")

        try:
            math_list = from_string_to_list(math_expr)
            if has_valid_symbols(math_list):
                if has_valid_parenthesis(math_list):
                    new_list = handle_minuses(math_list)
                    return new_list
                else:
                    print("invalid usage of parenthesis")
            else:
                print("invalid symbols in the math expression")

        except ValueError as e:
            print("invalid number input")

        except invalid_symbol_placements as e:
            print("invalid operators placement")

        print()


def main():
    print(float('2.'))
    while True:
        try:
            math_expr = get_expression()
            print(math_expr)
            posted_exp = to_postfix(math_expr)
            print(posted_exp)
            result = calculate_postfix(posted_exp)
            print(result)
        except KeyboardInterrupt as e:
            print("\nlogged out of console")
            break
        except invalid_symbol_placements as e:
            print("invalid placement of operands")
        except Exception as e:
            print("invalid usage of parenthesis")
        print()




if __name__ == '__main__':
    main()