from calculator import consts
from calculator.utility import *
from calculator.expression_token import *
from calculator.token_stream import TokenStream
from errors.lexical_error import LexicalError


class Lexer(object):
    def __init__(self, string):
        self.__index = 0
        self.__string = remove_spaces_from_string(string)
        self.__token_stream = []

    def tokenize_lexeme(self, lexeme):
        if is_number(lexeme):
            return Token(float(lexeme), consts.NUMBER_TOKEN)

        elif is_average(lexeme):
            return Token(lexeme, consts.AVERAGE_TOKEN)

        elif is_sum(lexeme):
            return Token(lexeme, consts.PLUS_TOKEN)

        elif is_subtract(lexeme):
            return Token(lexeme, consts.MINUS_TOKEN)

        elif is_sum(lexeme):
            return Token(lexeme, consts.PLUS_TOKEN)

        elif is_power(lexeme):
            return Token(lexeme, consts.POWER_TOKEN)

        elif is_multiply(lexeme):
            return Token(lexeme, consts.STAR_TOKEN)

        elif is_division(lexeme):
            return Token(lexeme, consts.DIVISION_TOKEN)

        elif is_factorial(lexeme):
            return Token(lexeme, consts.FACTORIAL_TOKEN)

        elif is_mod(lexeme):
            return Token(lexeme, consts.MOD_TOKEN)

        elif is_min(lexeme):
            return Token(lexeme, consts.MIN_TOKEN)

        elif is_max(lexeme):
            return Token(lexeme, consts.MAX_TOKEN)

        elif is_close_paren(lexeme):
            return Token(lexeme, consts.RPAR_TOKEN)

        elif is_open_paren(lexeme):
            return Token(lexeme, consts.LPAR_TOKEN)

        elif is_negate(lexeme):
            return Token(lexeme, consts.NEGATE_TOKEN)

        raise LexicalError

    def tokenize(self):
        lexeme = ""
        is_number_lexeme = False
        while(self.__index < len(self.__string)):
            char = self.__string[self.__index]
            if is_number_lexeme:
                if is_number(char):
                    lexeme += char
                    if self.__index == len(self.__string) - 1:
                        self.__token_stream.append(self.tokenize_lexeme(lexeme))
                else:
                    self.__token_stream.append(self.tokenize_lexeme(lexeme))
                    lexeme = char
                    is_number_lexeme = False
                    self.__token_stream.append(self.tokenize_lexeme(lexeme))
            else:
                lexeme = char
                if is_number(char):
                    is_number_lexeme = True
                    if self.__index == len(self.__string) - 1:
                        self.__token_stream.append(self.tokenize_lexeme(lexeme))
                else:
                    self.__token_stream.append(self.tokenize_lexeme(lexeme))
            self.__index += 1

        self.__token_stream = TokenStream(self.__token_stream)
        return self.__token_stream
