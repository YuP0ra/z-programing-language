import re

class Token:
    """ The token complier will takes a dict of tokens, compine them together
        and reutrn the complied valid re expression."""

    def __init__(self, tokens_dict):
        self._expression = "".join([str(tokens_dict[k]) for k in tokens_dict])
        self.pattern = re.compile(self._expression)

    def __str__(self):
        return self._expression


class LaxicalAnalyzer:
    """LaxicalAnalyzer will take a string and split it into tokens"""
    def __init__(self, compiled_tokens_dict):
        self._tokens = [(k, compiled_tokens_dict[k]) for k in compiled_tokens_dict]

    def append_complied_tokens(self, compiled_tokens):
        tmp = [(k, compiled_tokens_dict[k]) for k in compiled_tokens_dict]
        for t in tmp:
            self._tokens.append(t)

    def analyze(self, string):
        string = string.split()

        for word in string:
            for token_name, token in self._tokens:
                match = re.match(token.pattern, word)
                if match and (match.end() - match.start() == len(word)):
                    print(token_name, word)
                    break
