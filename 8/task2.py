from copy import deepcopy


def main():
    input = "input.txt"
    statements = parse_input_into_statements(input)
    numbered_statement = {i: statement for i, statement in enumerate(statements)}
    index_statement_after_file_ending = len(numbered_statement)
    for changed_statement in range(len(numbered_statement)):
        changed_statements = deepcopy(numbered_statement)
        changed_statements[changed_statement] = change_statement(
            numbered_statement[changed_statement]
        )
        executed_statements = set()
        statement = 0
        accumulator = 0

        while statement not in executed_statements:
            if statement == index_statement_after_file_ending:
                print("success")
                print(f"accumulator [{accumulator}]")
                break
            executed_statements.add(statement)
            statement_shift, accumulator = execute_statement(
                changed_statements[statement], accumulator
            )
            statement += statement_shift


def change_statement(statement):
    operation, value = statement
    if operation == "acc":
        return statement
    elif operation == "nop":
        return "jmp", value
    else:
        return "nop", value


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
