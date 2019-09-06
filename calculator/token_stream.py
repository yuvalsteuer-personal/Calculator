from calculator.expression_token import Token


class TokenStream(list):
    def __init__(self, token_stream_list=[]):
        super(TokenStream, self).__init__(token_stream_list)

    def read_token(self) -> Token:
        if(len(self)):
            return self.pop(0)
        return None

    def peek_token(self) -> Token:
        if(len(self)):
            return self[0]
        return None

    def push_token(self, token: Token):
        self.insert(0,token)