import re

from calculator.consts import *


def is_pattern(regex_pattern, lexeme):
    match_list = re.findall(
        string=lexeme,
        pattern=regex_pattern
    )
    matched_lexeme = ''.join(match_list)
    return lexeme == matched_lexeme


def is_number(lexeme):
    regex_pattern = "[0-9]+"
    return is_pattern(lexeme=lexeme, regex_pattern=regex_pattern)


def is_sum(lexeme):
    return lexeme == '+'


def is_subtract(lexeme):
    return lexeme == '-'


def is_multiply(lexeme):
    return lexeme == '*'


def is_power(lexeme):
    return lexeme == '^'


def is_division(lexeme):
    return lexeme == '/'


def is_negate(lexeme):
    return lexeme == '~'


def is_mod(lexeme):
    return lexeme == '%'


def is_factorial(lexeme):
    return lexeme == '!'


def is_average(lexeme):
    return lexeme == '@'


def is_max(lexeme):
    return lexeme == '$'


def is_min(lexeme):
    return lexeme == '&'


def is_close_paren(lexeme):
    return lexeme == ')'


def is_open_paren(lexeme):
    return lexeme == '('


def remove_spaces_from_string(string: str):
    return ''.join([char for char in string if (not char.isspace())])


def is_operator(token_class):
    return token_class >= PLUS_TOKEN and token_class < RPAR_TOKEN


def is_left_greate_precedence_than_right(left, right):
    return get_precedence(left) >= get_precedence(right)


def get_precedence(token_class):
    precedence = {
        PLUS_TOKEN: 1,
        MINUS_TOKEN: 1,
        STAR_TOKEN: 2,
        DIVISION_TOKEN: 2,
        POWER_TOKEN: 3,
        MOD_TOKEN: 4,
        FACTORIAL_TOKEN: 4,
        MIN_TOKEN: 5,
        MAX_TOKEN: 5,
        AVERAGE_TOKEN: 5,
        NEGATE_TOKEN: 6,
        LPAR_TOKEN: 7,
        RPAR_TOKEN: 7
    }
    return precedence[token_class]


def print_token_stream(token_stream):
    token_stream_str = ""
    for token in token_stream:
        if token.token_class == END_OF_STREAM:
            token_stream_str += "<END_OF_STREAM>"
        elif token.token_class == NUMBER_TOKEN:
            token_stream_str += "<NUMBER>"
        elif token.token_class == PLUS_TOKEN:
            token_stream_str += "<PLUS>"
        elif token.token_class == MINUS_TOKEN:
            token_stream_str += "<MINUS>"
        elif token.token_class == STAR_TOKEN:
            token_stream_str += "<STAR>"
        elif token.token_class == DIVISION_TOKEN:
            token_stream_str += "<DIVISION>"
        elif token.token_class == MOD_TOKEN:
            token_stream_str += "<MOD>"
        elif token.token_class == POWER_TOKEN:
            token_stream_str += "<POWER>"
        elif token.token_class == FACTORIAL_TOKEN:
            token_stream_str += "<FACTORIAL>"
        elif token.token_class == MIN_TOKEN:
            token_stream_str += "<MIN>"
        elif token.token_class == MAX_TOKEN:
            token_stream_str += "<MAX>"
        elif token.token_class == LPAR_TOKEN:
            token_stream_str += "<OPEN_PAREN>"
        elif token.token_class == RPAR_TOKEN:
            token_stream_str += "<CLOSE_PAREN>"
        elif token.token_class == AVERAGE_TOKEN:
            token_stream_str += "<AVERAGE>"
        else:
            token_stream_str = "<UNEXPECTED_TOKEN>"
            break
    return token_stream_str


def print_lexeme_stream(token_stream):
    token_stream_str = ""
    for token in token_stream:
        token_stream_str += str(token.lexeme) + ' '
    return token_stream_str
