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
    return int(result) if float(result).is_integer() else result