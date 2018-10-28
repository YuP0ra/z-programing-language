import re

class LaxicalAnalyzer:
    """LaxicalAnalyzer will take a string and split it into tokens"""
    def __init__(self, tokens_dict):
        self._tokens = [(k, re.compile(tokens_dict[k])) for k in tokens_dict]

    def analyze(self, string):
        string = string.split()
        for word in string:
            for token_name, pattern in self._tokens:
                match = re.match(pattern, word)
                if match and (match.end() - match.start() == len(word)):
                    print("%s\t Type: %s" % (word, token_name))
                    break
