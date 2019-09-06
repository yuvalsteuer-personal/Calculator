

class SyntaxError(Exception):
    def __init__(self, message=""):
        self.message = "<SyntaxError>" + message