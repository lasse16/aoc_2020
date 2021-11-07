def main():
    input = "input.txt"
    groups = parse_input_into_groups(input)
    answered_by_anyone = []
    for group in groups:
        answers = set()
        for person in group.splitlines():
            answers.update(list(person))
        answered_by_anyone.append(len(answers))
    print(sum(answered_by_anyone))


def parse_input_into_groups(input):
    with open(input) as file:
        groups = file.read().split("\n\n")
        return groups


if __name__ == "__main__":
    main()
