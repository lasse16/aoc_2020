def main():
    input = "input.txt"
    numbers_and_turns_spoken, prev_number = parse_input(input)
    is_starting_number = True
    turn_limit = 2020
    for turn in range(len(numbers_and_turns_spoken), turn_limit):
        last_turn_previous_number_spoken = numbers_and_turns_spoken.get(prev_number, 0)
        number_spoken = -1
        if not last_turn_previous_number_spoken or is_starting_number:
            is_starting_number = False
            number_spoken = 0
        else:
            number_spoken = turn - last_turn_previous_number_spoken
        numbers_and_turns_spoken[prev_number] = turn
        prev_number = number_spoken
    numbers_and_turns_spoken[prev_number] = turn_limit
    print(numbers_and_turns_spoken)
    print(prev_number)


def parse_input(input):
    starting_numbers_and_turns = dict()
    with open(input) as file:
        starting_numbers = next(file).strip().split(",")
        for turn, starting_number in enumerate(starting_numbers, 1):
            starting_number = int(starting_number)
            starting_numbers_and_turns[starting_number] = turn
        return starting_numbers_and_turns, int(starting_numbers[-1])


if __name__ == "__main__":
    main()
