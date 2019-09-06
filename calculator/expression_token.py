

class Token(object):

    def __init__(self, lexeme, token_class):
        self._lexeme = lexeme 
        self._token_class = token_class

    @property
    def lexeme(self):
        return self._lexeme

    @property
    def token_class(self):
        return self._token_class
    




