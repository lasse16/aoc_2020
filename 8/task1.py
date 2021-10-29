def main():
    input = "input.txt"
    statements = parse_input_into_statements(input)
    numbered_statement = {i: statement for i, statement in enumerate(statements)}
    executed_statements = set()
    statement = 0
    accumulator = 0
    while statement not in executed_statements:
        executed_statements.add(statement)
        statement_shift, accumulator = execute_statement(
            numbered_statement[statement], accumulator
        )
        statement += statement_shift
    print(f"accumulator [{accumulator}]")


def execute_statement(statement, accumulator):
    operation, value = statement
    statement_shift = 1

    if operation == "acc":
        accumulator += value
    elif operation == "jmp":
        statement_shift = value
    return statement_shift, accumulator


def parse_input_into_statements(input):
    statements = []
    with open(input) as file:
        for line in file:
            statement = parse_to_statement(line.strip())
            statements.append(statement)
    return statements


def parse_to_statement(line):
    operation, value = line.split()
    return operation, int(value)


if __name__ == "__main__":
    main()
