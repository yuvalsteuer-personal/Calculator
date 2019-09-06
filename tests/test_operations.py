import pytest


from calculator.lexer import Lexer
from calculator.parser import Parser
from calculator.evaluator import Evaluator


def calculate(expression):
    lexer = Lexer(string=expression)
    token_stream = lexer.tokenize()

    parser = Parser(token_stream=token_stream)
    parsed_rpn_token_stream = parser.parse_syntax()

    evaluator = Evaluator(parsed_rpn_token_stream)
    result = evaluator.evaluate()
    return result

class TestCalculatorOps(object):

    def test_addition(self):
        assert calculate("1+3") == 4, "Addition test failed"

    def test_subtraction(self):
        assert calculate("1-3") == -2

    def test_multiplication(self):
        assert calculate("3*4") == 12
        assert calculate("0*4") == 0
        assert calculate("1*9") == 9

    def test_division(self):
        assert calculate("20/4") == 5
        assert calculate("3/4") == eval("3/4")
        assert calculate("0/4") == 0
        with pytest.raises(ZeroDivisionError):
            calculate("4/0")

    def test_power(self):
        assert calculate("2^4") == 16
        assert calculate("4^0") == 1
        assert calculate("(4+2)^(3-1)") == 36

    def test_negate(self):
        assert calculate("~4") == -4
        assert calculate("~(4+3)") == -7

    def test_factorial(self):
        assert calculate("!4") == 24
        assert calculate("!(3-2)") == 1

    def test_maximum(self):
        assert calculate("5$4") == 5
        assert calculate("(5+3)$(9)") == 9

    def test_minimum(self):
        assert calculate("5&4") == 4
        assert calculate("(5+3)$(9)") == 8

    def test_modulu(self):
        assert calculate("4%4") == 0
        assert calculate("5%4") == 1
        assert calculate("4%5") == 4

    def test_combo(self):
        assert calculate("((((5^3)+(99/3)-!3+(~6)-(3*6))$(100))@100)&(100%1000)") == 0