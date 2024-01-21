from db import *

class invalid_opr_placements(Exception):
    def __int__(self):
        pass
    def __str__(self):
        return "invalid symbol placement"

class invalid_parenthesis_placements(Exception):
    def __int__(self):
        pass
    def __str__(self):
        return "invalid parenthesis placement"

class invalid_symbols(Exception):
    def __int__(self):
        pass
    def __str__(self):
        return "invalid symbols"



def change_minuses(math_expr: list):
    """
    A method that receives a list representing an infix mathematical expression.
    The method goes through the minuses in the expression (if any) and checks which minus is unary or binary.
    The method deletes the sequences of unary minuses accordingly
    :param math_expr: A list representing an in infix  mathematical expression (not necessarily a correct expression)
    :return: a new list with the same mathematical expression only the minuses have changed, every unary minus has changed
    to the operator "u-", and the new list doesn't contain sequences of unary minuses
    """
    new_list = []
    i=0

    while i < len(math_expr):
        if math_expr[i] == '-':
            if (i == 0) or (i > 0 and math_expr[i] == '('):
                minus = 'u-'

            elif math_expr[i - 1] in operator_dict:
                opr_tuple = operator_dict[math_expr[i - 1]]
                minus = 'u-' if opr_tuple[2] is True else '-'

            else:
                minus = '-'


            if minus == '-':
                new_list.append(minus)
                i+=1

            else:
                count = 0
                while i < len(math_expr) and math_expr[i] == '-':
                    count += 1
                    i += 1
                if count % 2 == 1:
                    new_list.append(minus)
                if i < len(math_expr) and math_expr[i] == '~':
                    raise invalid_opr_placements
        else:
            new_list.append(math_expr[i])
            i += 1

    return new_list



def handle_unary_minuses(math_expr: list):
    """
    A method that receives a list representing an infix mathematical expression and changes every
    unary minus that is after an operator to "~".
    the method also checks if the placement of each operator is valid
    :param math_expr: A list representing an in infix  mathematical expression (not necessarily a correct expression)
    :return: a new list with the same mathematical expression only the unary minuses have changed,
     every unary minus that is after an operator has changed to "~"(an operator the role of tilda)
    """
    removed = change_minuses(math_expr)
    check_symbols_and_placements(removed)

    for i in range(len(removed)):
        if removed[i] == 'u-':
            if i != 0 and removed[i-1] in operator_dict:
                removed[i] = '~'
    return removed



def from_string_to_list(math_expr: str):
    """
    A method that receives a string representing an infix mathematical expression and converts it to a list
    :param math_expr: A string representing an in infix  mathematical expression (not necessarily a correct expression)
    :return: A new list that that contains the same expression the string has
    """
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
    """
    A method that receives two operators and checks which operator has the higher precedence
    :param operator1: a curtain operator tuple
    :param operator2: a curtain operator tuple
    :return: True if operator1 has a higher equal precedence than operator2, else False
    """
    operator_tuple1 = operator_dict[operator1]
    operator_tuple2 = operator_dict[operator2]
    return operator_tuple1[0] >= operator_tuple2[0]



def check_symbols_and_placements(math_expr: list):
    """
    A method that receives a list representing an infix mathematical expression.
    The method goes through the operators in the expression (if any) and checks if the placement of the operator
    in the expression is valid.
    :param math_expr: A list representing an in infix  mathematical expression (not necessarily a correct expression)
    :return: An exception adjusted to the curtain error in the expression

    """
    for i in range(len(math_expr)):
        if math_expr[i] in operator_dict:
            opr_tuple = operator_dict[math_expr[i]]
            if opr_tuple[1] == "right":
                if i+1< len(math_expr) and math_expr[i+1] not in operator_dict:
                    raise invalid_opr_placements

            elif math_expr[i] == '~':
                if (i < len(math_expr)-1 and math_expr[i+1] == '~') or (i > 0 and math_expr[i-1] == 'u-'):
                    raise invalid_opr_placements

        elif math_expr[i] == '(':
            if i > 0 and math_expr[i-1] not in operator_dict and math_expr[i-1] != '(':
                raise invalid_parenthesis_placements

        elif math_expr[i] == ')':
            if i+1 < len(math_expr) and math_expr[i+1] not in operator_dict and math_expr[i-1] != ')':
                raise invalid_parenthesis_placements

        else:
            if not isinstance(math_expr[i], float):
                raise invalid_symbols



def to_postfix(exp_list: list):
    """
    A method that receives a list representing an infix mathematical expression and converts the expression
    from infix to postfix.
    :param exp_list: A list representing an in infix  mathematical expression (not necessarily a correct expression)
    :return: A new list that contains the same mathematical expression, only in a postfix order
    """
    post_list = []
    operator_stack = []

    for obj in exp_list:
        if obj in operator_dict:

            while operator_stack and operator_stack[-1] != '(' and has_higher_equal_precedence(operator_stack[-1], obj) and post_list:
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

            if operator_stack:
                operator_stack.pop();
            else:
                raise invalid_parenthesis_placements


    while operator_stack:
        op1 = operator_stack.pop()
        post_list.append(op1)

    if ('(' or ')') in post_list:
        raise invalid_parenthesis_placements
    return post_list



def calculate_postfix(math_expr: list):
    """
    A method that receives a list representing a postfix mathematical expression and calculates it.
    :param math_expr: A list representing an in postfix  mathematical expression (not necessarily a correct expression)
    :return: The result to the given expression if there was no error in the expression,
    otherwise the method would raise an adjusted exception.
    """
    i = 0
    result = math_expr[0]
    while i < len(math_expr):
        if math_expr[i] in operator_dict:
            operator_tuple = operator_dict[math_expr[i]]
            opr_dir = operator_tuple[1]
            try:
                if opr_dir != "both":
                    result = calc(math_expr[i], math_expr[i - 1], None)
                    math_expr[i - 1] = result
                    math_expr.pop(i)

                else:
                    result = calc(math_expr[i], math_expr[i - 2], math_expr[i - 1])
                    math_expr[i - 2] = result
                    math_expr.pop(i)
                    math_expr.pop(i - 1)

            except TypeError:
                raise TypeError
            except OverflowError:
                raise OverflowError
            except ValueError:
                raise Exception

            i = 0
        i = i + 1
    if len(math_expr) > 1:
        raise invalid_opr_placements
    return result



def get_expression():
    """
    A method that scans a mathematical expression from the user
    :return: An infix mathematical expression (not necessarily a correct expression)
    """
    while True:
        math_expr = input("enter a math expression: ")

        try:
            math_list = from_string_to_list(math_expr)
            new_list = handle_unary_minuses(math_list)
            return new_list

        except ValueError:
            print("invalid number input")

        except invalid_opr_placements:
            print("invalid operators placement")

        except invalid_parenthesis_placements:
            print("invalid parenthesis placement")

        except invalid_symbols:
            print("invalid symbols in the math expression")
        print()


def main():
    while True:
        try:
            math_expr = get_expression()
            posted_exp = to_postfix(math_expr)
            result = calculate_postfix(posted_exp)
            print(result)

        except KeyboardInterrupt:
            print("\nlogged out of console")
            break

        except TypeError:
            print("invalid operators placement")

        except OverflowError:
            print("calculation on a number that is to big")

        except invalid_parenthesis_placements:
            print("invalid parenthesis placement")

        except invalid_opr_placements:
            print("invalid operands placement")

        except EOFError:
            print("\nlogged out of console")
            break

        except Exception:
            print("impossible  calculation")
        print()


if __name__ == '__main__':
    main()