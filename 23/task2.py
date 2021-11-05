import math

PUZZLE_INPUT = "962713854"
MAX_CUP = 9
MIN_CUP = 1


def main():
    cups = [int(_char) for _char in PUZZLE_INPUT]
    for cup in range(MAX_CUP + 1, 1_000_001):
        cups.append(cup)
    linked_list_cups = {}
    prev_value = cups[0]
    for cup in cups[::-1]:
        linked_list_cups[cup] = prev_value
        prev_value = cup
    current_cup = 9
    cups = linked_list_cups
    for _ in range(10_000_000):
        cups, current_cup = do_move(cups, current_cup)
    cups_after_one = iterate_over_linked_list(cups, 1, 2)
    print(f"product [{math.prod(cups_after_one)}]")


def do_move(cups, current_cup):
    next_three_cups = iterate_over_linked_list(cups, current_cup, 3)
    cups[current_cup] = cups[next_three_cups[-1]]

    destination_cup = ((current_cup - 2) % 1_000_000) + 1
    while destination_cup in next_three_cups:
        destination_cup = ((destination_cup - 2) % 1_000_000) + 1

    ending_link = cups[destination_cup]
    cups[destination_cup] = next_three_cups[0]
    cups[next_three_cups[-1]] = ending_link
    return cups, cups[current_cup]


def iterate_over_linked_list(linked_list, start, times):
    output = []
    last_pointer = start
    for _ in range(times):
        value = linked_list[last_pointer]
        output.append(value)
        last_pointer = value
    return output


if __name__ == "__main__":
    main()
