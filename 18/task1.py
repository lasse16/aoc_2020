import operator as op

operators = {"+": op.add, "*": op.mul}


def main():
    input = "input.txt"
    postfix_statements = parse_input_into_postfix_statements(input)
    print(
        sum(
            [
                execute_postfix_statement(postfix_statement)
                for postfix_statement in postfix_statements
            ]
        )
    )


def execute_postfix_statement(statement):
    operands = [int(statement[i]) for i in range(2)]
    statement = statement[2:]
    result = 0
    for _char in statement:
        if is_operator(_char):
            applied_operands = operands[-2:]
            operands = operands[:-2]
            result = operators[_char](*applied_operands)
            operands.append(result)
        else:
            operands.append(int(_char))
    return result


def parse_input_into_postfix_statements(input):
    postfix_notations = []
    with open(input) as file:
        for line in file:
            postfix_notation = convert_from_infix_to_postfix_notation(line)
            postfix_notations.append(postfix_notation)
    return postfix_notations


def convert_from_infix_to_postfix_notation(infix_notation: str) -> str:
    stack = []
    output = ""
    for _char in infix_notation:
        if _char.isnumeric():
            output += _char
        elif is_operator(_char):
            while stack and stack[-1] not in "()":
                output += stack.pop()
            stack.append(_char)
        elif _char == "(":
            stack.append(_char)
        elif _char == ")":
            while stack[-1] != "(":
                output += stack.pop()
            stack.pop()
    while stack:
        output += stack.pop()
    return output


def is_operator(value):
    return value in operators


if __name__ == "__main__":
    main()
