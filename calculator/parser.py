from calculator.utility import *
from calculator.token_stream import TokenStream
from errors.syntax_error import SyntaxError


class Parser(object):
    def __init__(self, token_stream):
        self.__token_stream = token_stream

    def parse_syntax(self) -> TokenStream:
        rpn_token_stream = TokenStream()
        operator_stack = TokenStream()
        while len(self.__token_stream):
            current_token = self.__token_stream.read_token()

            if current_token.token_class == NUMBER_TOKEN:
                rpn_token_stream.append(current_token)

            if is_operator(current_token.token_class):
                while (
                        len(operator_stack) and is_left_greate_precedence_than_right(
                    left=operator_stack.peek_token().token_class,
                    right=current_token.token_class
                ) and operator_stack.peek_token().token_class != LPAR_TOKEN
                ):
                    rpn_token_stream.append(operator_stack.read_token())
                operator_stack.push_token(current_token)

            if current_token.token_class == LPAR_TOKEN:
                operator_stack.push_token(current_token)

            if current_token.token_class == RPAR_TOKEN:
                while len(operator_stack) and operator_stack.peek_token().token_class != LPAR_TOKEN:
                    rpn_token_stream.append(operator_stack.read_token())
                if operator_stack.peek_token().token_class == LPAR_TOKEN:
                    _ = operator_stack.read_token()
                else:
                    raise SyntaxError("Parenthesis mismatch!")

        if not len(self.__token_stream):
            while len(operator_stack):
                temp_token = operator_stack.read_token()
                if temp_token.token_class == LPAR_TOKEN or temp_token.token_class == RPAR_TOKEN:
                    raise SyntaxError("Parenthesis mismatch!")
                rpn_token_stream.append(temp_token)

        return rpn_token_stream
