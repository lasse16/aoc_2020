import re


class ContextFreeGrammar:
    def __init__(self, starting_symbol, terminals, non_terminals, rules):
        self.starting_symbol = starting_symbol
        self.terminals = terminals
        self.non_terminals = non_terminals
        self.rules = rules
        self.regex = self.build_regex(self.__replace_elevens(self.abc(starting_symbol)))
        self.eleven_pattern = "x11x"

    def build_regex(self, regex_string_list):
        patterns = [re.compile(regex_string) for regex_string in regex_string_list]
        return patterns

    def constructs(self, word):
        for regular_expression in self.regex:
            if regular_expression.fullmatch(word):
                return True

    def __replace_elevens(self, regex):
        # In lack of a better solution I just created 5 different regexs with different count of rule 11
        # Normally rule 11 constructs 42^n31^n but there is no clecer solution in regex for that ( a^nb^n)
        regex_variants = []
        eleven_index = regex.find("x11x")
        pre_eleven = regex[:eleven_index]
        post_eleven = regex[eleven_index + len("x11x") :]

        for i in range(1, 5):
            regex = pre_eleven + self.abc("42") * i + self.abc("31") * i + post_eleven
            regex_variants.append(regex)

        return regex_variants

    def abc(self, rule_number):
        if rule_number == "8":
            return f'({self.abc("42")})+'
        if rule_number == "11":
            return "x11x"
        rule = self.rules[rule_number]
        options = rule.split("|")
        if '"a"' in options or '"b"' in options or "(" in options[0]:
            return options.pop().strip('"')
        resolved_options = []
        for option in options:
            next_rules = option.strip().split()
            resolved_options.append("".join([self.abc(rule) for rule in next_rules]))

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
