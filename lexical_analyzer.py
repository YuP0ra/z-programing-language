import re

# Define all reserverd words in COOL
zp_keywords = { 'at', 'as', 'and',
                'bool', 'break',
                'case', 'class', 'continue',
                'def',
                'else', 'elif', 'except',
                'false', 'finally', 'for',
                'if', 'in', 'id', 'is', 'import',
                'loop',
                'new', 'not', 'none',
                'or',
                'then', 'try', 'true', 'type',
                'while'}


token_decimal  = r'[+-]?' + r'\d+' + r'(.\d*)?'             # [Sign]  [Integer]  [Fraction]
token_identifier = r'[_a-zA-Z]+[_a-zA-Z0-9]*'               # [_ or latter] [any vaild char]

token_operator = "|".join([ r'(->|<-)',                     # Dirrecting
                            r'=|+=|-=|%=|/=|\*=',           # Assign
                            r'<=|>=|==|!=|<|>',             # Comparession
                            r'+|-|\*|/|%'                   # Math
                          ])

token_special_operators = r'[:,!]'

class LaxicalAnalyzer:
    """LaxicalAnalyzer will take a raw string as input then split it into words,
     Next, it will map each word to a token,
     If the token was not found it will match it to ERROR! """

    def __init__(self,):
        # the current tokens that our laxical match
        tokens_dict = {
            "Identifier"    : token_identifier,
            "Decimal"       : token_decimal,
            "Operator"      : token_operator,
            "Special Opt"   : token_special_operators,
        }

        # compile the tokens to be used later
        self._tokens = [(k, re.compile(tokens_dict[k])) for k in tokens_dict]

    def analyze(self, string):
        string = string.split()

        for word in string:
            matched = False

            # first we check that the word is a keyword token
            if word in zp_keywords:
                print("%s\t\t Type: %s" % (word, "Keyword"))
                continue

            # try to match the current word with every complied token we have
            for token_name, pattern in self._tokens:
                match = re.match(pattern, word)

                # check that the entire workd is matched
                if match and (match.end() - match.start() == len(word)):
                    print("%s\t\t Type: %s" % (word, token_name))
                    matched = True
                    break

            if not matched:
                print("%s\t\t Type: %s" % (word, "UNKOWN! ERROR!"))
