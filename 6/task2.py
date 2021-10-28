def main():
    input = "input.txt"
    groups = parse_input_into_groups(input)
    answered_by_everyone = []
    for group in groups:
        answers = set("abcdefghijklmnopqrstuvwxyz")
        for person in group.splitlines():
            answers = answers.intersection(set(person))
        answered_by_everyone.append(len(answers))
    print(sum(answered_by_everyone))


def parse_input_into_groups(input):
    with open(input) as file:
        groups = file.read().split("\n\n")
        return groups


if __name__ == "__main__":
    main()
