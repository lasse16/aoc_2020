tiles = dict()

direction_to_shift = {
    "e": (-2, 0),
    "w": (2, 0),
    "se": (-1, -1),
    "ne": (-1, 1),
    "sw": (1, -1),
    "nw": (1, 1),
}


def main():
    input = "input.txt"
    tile_flip_instructions = parse_input_into_tile_flip_instructions(input)
    for instruction in tile_flip_instructions:
        file_location = execute_flip(instruction)
        tiles[file_location] = not tiles.get(file_location, False)
    print(sum(value for value in tiles.values()))


def execute_flip(flip_location):
    east_west, north_south = zip(*flip_location)
    return sum(east_west), sum(north_south)


def parse_input_into_tile_flip_instructions(input):
    with open(input) as file:
        return [parse_flip_instruction(line.strip()) for line in file]


def parse_flip_instruction(line):
    flip_instruction = []
    diagram = False
    for _char in line:
        if diagram:
            diagram += _char
            flip_instruction.append(direction_to_shift[diagram])
            diagram = False
        elif _char in "ew":
            flip_instruction.append(direction_to_shift[_char])
        else:
            diagram = _char

    return flip_instruction


if __name__ == "__main__":
    main()
