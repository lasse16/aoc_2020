PUZZLE_INPUT = "962713854"
MAX_CUP = 9
MIN_CUP = 1


def main():
    cups = [int(_char) for _char in PUZZLE_INPUT]
    for _ in range(100):
        cups = do_move(cups)
    one_index = cups.index(1)
    reordered_cups = cups[one_index + 1 :] + cups[:one_index]
    print("".join([str(cup) for cup in reordered_cups]))


def do_move(cups):
    current_cup = cups[0]
    next_three_cups = cups[1:4]
    remaining_cups = [current_cup] + cups[4:]
    sorted_remaining_cups = sorted(remaining_cups)
    destination_cup = sorted_remaining_cups[
        (sorted_remaining_cups.index(current_cup) - 1) % len(remaining_cups)
    ]
    destination_cup_index = remaining_cups.index(destination_cup)
    return (
        remaining_cups[1 : destination_cup_index + 1]
        + next_three_cups
        + remaining_cups[destination_cup_index + 1 :]
        + [current_cup]
    )


if __name__ == "__main__":
    main()
