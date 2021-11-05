import re


class ContextFreeGrammar:
    def __init__(self, starting_symbol, terminals, non_terminals, rules):
        self.starting_symbol = starting_symbol
        self.terminals = terminals
        self.non_terminals = non_terminals
        self.rules = rules
        self.regex = self.build_regex(starting_symbol, rules)

    def build_regex(self, starting_symbol, rules):
        regex_string = self.__resolve_rule_to_regex(rules[starting_symbol])
        pattern = re.compile(regex_string)
        return pattern

    def constructs(self, word):
        return bool(self.regex.fullmatch(word))

    def __resolve_rule_to_regex(self, rule):
        options = rule.split("|")
        if '"a"' in options or '"b"' in options:
            return options.pop().strip('"')
        resolved_options = []
        for option in options:
            next_rules = option.strip().split()
            resolved_options.append(
                "".join(
                    [
                        self.__resolve_rule_to_regex(self.rules[rule])
                        for rule in next_rules
                    ]
                )
            )

        return "(" + "|".join(resolved_options) + ")"


def main():
    words, grammar = parse_input_into_words_and_grammar("input.txt")
    print(len([word for word in words if grammar.constructs(word)]))


def parse_input_into_words_and_grammar(input):
    with open(input) as file:
        grammar_bare, words_bare = file.read().split("\n\n")
        words = [word.strip() for word in words_bare.splitlines()]
        grammar = parse_string_into_grammar(grammar_bare)
        return words, grammar


def parse_string_into_grammar(string):
    rules = {}
    terminals = {"a", "b"}
    non_terminals = []
    starting_symbol = "0"
    for rule_bare in string.splitlines():
        number, rule_text = rule_bare.split(":")
        rules[number] = rule_text.strip()
    non_terminals = list(rules)
    return ContextFreeGrammar(starting_symbol, terminals, non_terminals, rules)


if __name__ == "__main__":
    main()
