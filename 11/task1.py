from enum import Enum, auto

list_of_neighbour_index_shifts = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


class SeatingState(Enum):
    FLOOR = auto()
    FREE = auto()
    OCCUPIED = auto()


def main():
    seating_grid, seats = parse_input_into_seating_and_seats("input.txt")
    seating_grid, change_occured = do_one_round(seats, seating_grid)
    while change_occured:
        seating_grid, change_occured = do_one_round(seats, seating_grid)
    print(list(seating_grid.values()).count(SeatingState.OCCUPIED))


def parse_input_into_seating_and_seats(input):
    seating_grid = dict()
    seats = []
    with open(input) as file:
        for row_index, line in enumerate(file):
            for col_index, char in enumerate(line):
                if char == ".":
                    seating_grid[(row_index, col_index)] = SeatingState.FLOOR
                elif char == "L":
                    seating_grid[(row_index, col_index)] = SeatingState.FREE
                    seats.append((row_index, col_index))
                elif char == "#":
                    seating_grid[(row_index, col_index)] = SeatingState.OCCUPIED
                    seats.append((row_index, col_index))
    return seating_grid, seats


def get_number_of_adjacent_occupied_seats(seat, seating_grid):
    number_of_occupied_neighbours: int = 0
    for neighbour_seat in get_neighbours(seat):
        number_of_occupied_neighbours += int(
            is_seat_occupied(neighbour_seat, seating_grid)
        )
    return number_of_occupied_neighbours


def get_neighbours(seat):
    neighbours = []
    row_index, col_index = seat
    for neighbour_shift in list_of_neighbour_index_shifts:
        neighbours.append(
            (row_index + neighbour_shift[0], col_index + neighbour_shift[1])
        )
    return neighbours


def is_seat_occupied(seat, seating_grid):
    return get_seat_state(seat, seating_grid) == SeatingState.OCCUPIED


def get_seat_state(seat, seating_grid, default=SeatingState.FLOOR):
    return seating_grid.get(seat, default)


def do_one_round(seats, seating_grid):
    updated_seats = dict()
    for seat in seats:
        amount_of_occupied_neighbours = get_number_of_adjacent_occupied_seats(
            seat, seating_grid
        )
        seat_state = get_seat_state(seat, seating_grid)
        if seat_state == SeatingState.FREE and amount_of_occupied_neighbours == 0:
            updated_seats[seat] = SeatingState.OCCUPIED
        elif seat_state == SeatingState.OCCUPIED and amount_of_occupied_neighbours > 3:
            updated_seats[seat] = SeatingState.FREE
    seating_grid.update(updated_seats)
    return seating_grid, bool(updated_seats)


def __visualize_seating_grid(seating_grid):
    prev_seat = (0, 0)
    output = "-------------------------------\n"
    for seat, state in seating_grid.items():
        if seat[0] != prev_seat[0]:
            output += "\n"
        output += __to_char(state)
        prev_seat = seat

    print(output)
    return output


def __to_char(state: SeatingState):
    if state == SeatingState.FLOOR:
        return "."
    elif state == SeatingState.FREE:
        return "L"
    elif state == SeatingState.OCCUPIED:
        return "#"


if __name__ == "__main__":
    main()
