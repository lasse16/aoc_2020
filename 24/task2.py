direction_to_shift = {
    "e": (-2, 0),
    "w": (2, 0),
    "se": (-1, -1),
    "ne": (-1, 1),
    "sw": (1, -1),
    "nw": (1, 1),
}


def main():
    tiles = dict()
    input = "input.txt"
    tile_flip_instructions = parse_input_into_tile_flip_instructions(input)
    for instruction in tile_flip_instructions:
        file_location = execute_flip(instruction)
        tiles[file_location] = not tiles.get(file_location, False)

    for day in range(100):
        updated_tiles = apply_rules(tiles)
        tiles.update(updated_tiles)

    print(sum(value for value in tiles.values()))


def apply_rules(tiles):
    updated_tiles = {}
    black_tiles = {tile for tile in tiles if tiles[tile]}
    neighbours_with_black_tiles = set(
        flatten([get_neighbours(tile) for tile in black_tiles])
    )
    tiles_to_check = neighbours_with_black_tiles.union(black_tiles)
    for tile in tiles_to_check:
        tile_colours = [tiles.get(location, False) for location in get_neighbours(tile)]
        black_neighbours = [tile_colour for tile_colour in tile_colours if tile_colour]
        count_black_neighbours = len(black_neighbours)
        tile_colour = tiles.get(tile, False)
        if tile_colour:
            if count_black_neighbours == 0 or count_black_neighbours > 2:
                updated_tiles[tile] = False
        elif count_black_neighbours == 2:
            updated_tiles[tile] = True

    return updated_tiles


def flatten(list_of_lists):
    out = []
    for i in list_of_lists:
        out.extend(i)
    return out


def get_neighbours(tile):
    x, y = tile
    return [
        (x + neighbour[0], y + neighbour[1])
        for neighbour in direction_to_shift.values()
    ]


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
