from math import factorial


from calculator.utility import *
from calculator.expression_token import Token
from calculator.token_stream import TokenStream

class Evaluator(object):

    def __init__(self, parsed_token_stream):
        self.__parsed_token_stream = parsed_token_stream

    def evaluate(self):
        result = None
        stack = TokenStream()
        for token in self.__parsed_token_stream:
            if(is_operator(token_class=token.token_class)):
                if(token.lexeme == '~' or token.lexeme == '!'):
                    operand_1 = stack.read_token()
                    result = Token(self.__eval_unary_expression(token, operand_1.lexeme),NUMBER_TOKEN)
                else:
                    operand_2 = stack.read_token()
                    operand_1 = stack.read_token()
                    result = Token(
                        lexeme=self.__eval_binary_expression(
                            op=token,
                            left=operand_1.lexeme,
                            right=operand_2.lexeme
                        ), 
                        token_class=NUMBER_TOKEN
                    )
                stack.push_token(result)
            elif(token.token_class == NUMBER_TOKEN):
                stack.push_token(token)

        return stack.read_token().lexeme

    def __eval_binary_expression(self, op, left, right):
        if op.token_class == PLUS_TOKEN:
            return left + right
        elif op.token_class == MINUS_TOKEN:
            return left - right
        elif op.token_class == STAR_TOKEN:
            return left * right
        elif op.token_class == DIVISION_TOKEN:
            return left / right
        elif op.token_class == POWER_TOKEN:
            return left ** right
        elif op.token_class == AVERAGE_TOKEN:
            return (left + right) / 2
        elif op.token_class == MIN_TOKEN:
            return min(left, right)
        elif op.token_class == MAX_TOKEN:
            return max(left, right)
        elif op.token_class == MOD_TOKEN:
            return left%right

    def __eval_unary_expression(self, op, operand):
        if(op.token_class == FACTORIAL_TOKEN):
            return factorial(operand)
        elif(op.token_class == NEGATE_TOKEN):
            return -operand