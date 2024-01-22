import pytest
from begginer_proj.calculater import calculate_expression
from begginer_proj.db import *


"""the calculater code has 2 steps using 2 methods: 
1)  get_expression() - the code requests an infix mathematical expression from the user.
    this method checks if the expression has invalid inputs or invalid placements for the operands/parenthesis 
    if everything is okay, the expression will be returned, else, an adjusted exception will be raised
2) calculate_expression(math_expr) - the method receives an infix mathematical expression from the user.
    this method calculates the expression
    if everything is okay, the expression will be returned, else, an adjusted exception will be raised

i will test these 2 method in pytest
"""


def test_calculate_expression(math_expr:str)->str:
    try:
        result = calculate_expression(math_expr)
        return str(result)

    except invalid_operands_placements:
        return "invalid operands placement"

    except OverflowError:
        return "calculation on a number that is to big"

    except invalid_parenthesis_placements:
        return "invalid parenthesis placement"

    except invalid_operators_placements:
        return "invalid operators placement"

    except ValueError:
        return "invalid number input"

    except invalid_symbols:
        return "invalid symbols in the math expression"

    except Exception:
        return "impossible  calculation"



def test_hello():
    assert test_calculate_expression("5+7") == "12.0"
    assert test_calculate_expression("3*(4+2)") == "18.0"
    assert test_calculate_expression("9-(6/2)") == "6.0"
    assert test_calculate_expression("-81^0.5") == "-9.0"
    assert test_calculate_expression("3^3!") == "729.0"
    assert test_calculate_expression("(26*4)#") == "5.0"
    assert test_calculate_expression("56@24") == "40.0"
    assert test_calculate_expression("~------6") == "-6.0"
    assert test_calculate_expression("25$34") == "34.0"
    assert test_calculate_expression("303%10") == "3.0"
    assert test_calculate_expression("5&21") == "5.0"
    assert test_calculate_expression("5           + 21/3") == "12.0"
    assert test_calculate_expression(" 303 + 10 ") == "313.0"



    assert test_calculate_expression("7*(12+5.5) + 2!*(3/4+5/6)#") == "238.5"
    assert test_calculate_expression("2^4! + (4^3 -2^5) / (~-16^0.5) + 54@40") == "16777271.0"
    assert test_calculate_expression("(2 ^ 4)$(3!!) + ~-----10!  # *100%23") == "936.0"
    assert test_calculate_expression("((2+3)!)&(7564#)*---4+ 25*10/5^2") == "-78.0"
    assert test_calculate_expression("~(-2^5)#/2! + (26*4)@(72*3)") == "162.5"
    assert test_calculate_expression("(455%5)* 56 + ((2^-2)*9!)# + ----5") == "23.0"
    assert test_calculate_expression("(((378/2^-1)$3!!)&184*4)# + 2/2!") == "17.0"
    assert test_calculate_expression("~(789#^3) + (283*23)@9!*  197----15^2") == "36370767.5"
    assert test_calculate_expression("-726# + 78%4! + (134^3)# -~((54*12)@5!)") == "392.0"
    assert test_calculate_expression("(199*24)&9!@((4+3)!)$((126^2)#)-5123+56%4") == "-215.0"
    assert test_calculate_expression("(-150-6!)@8!-((4^10+3*111)#)+((126^2)$34579)*12") == "434642.0"
    assert test_calculate_expression("(123879534*0.01--151&---532)/1000") == "1239.32734"
    assert test_calculate_expression("3  @-8^ 3* (10^12# * 4 + ~(4*2!)$-78)----512") == "-61863.0"
    assert test_calculate_expression("25 ^ (5 / 25)%     2!!!! * 	3450/23") == "285.5480908073818"
    assert test_calculate_expression("680-(~23 * 20 & 5!) +95^2 --12397 @ (4356*23)#") == "16354.5"



    assert test_calculate_expression("34   34") == "invalid operands placement"
    assert test_calculate_expression("123*45		6") == "invalid operands placement"

    assert test_calculate_expression("34~45*6") == "invalid operators placement"
    assert test_calculate_expression("!65") == "invalid operators placement"
    assert test_calculate_expression("45++23//2") == "invalid operators placement"
    assert test_calculate_expression("~~45 **6!5") == "invalid operators placement"

    assert test_calculate_expression("3*34yhg+ 1A6") == "invalid symbols in the math expression"
    assert test_calculate_expression("134A*X12?") == "invalid symbols in the math expression"

    assert test_calculate_expression("67865^10000") == "calculation on a number that is to big"

    assert test_calculate_expression("8/0") == "impossible  calculation"
    assert test_calculate_expression("0^-1") == "impossible  calculation"
    assert test_calculate_expression("~23!") == "impossible  calculation"
    assert test_calculate_expression("") == "impossible  calculation"

    assert test_calculate_expression("45(*)34") == "invalid parenthesis placement"
    assert test_calculate_expression("34(34+12") == "invalid parenthesis placement"
    assert test_calculate_expression("12+45)!") == "invalid parenthesis placement"

    assert test_calculate_expression("2.34.1") == "invalid number input"
    assert test_calculate_expression(".21.89") == "invalid number input"

