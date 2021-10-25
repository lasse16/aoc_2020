from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int
    z: int
    w: int


neighbour_shifts = [
    (0, 0, 0, 1),
    (0, 0, 0, -1),
    (0, 0, 1, 0),
    (0, 0, 1, 1),
    (0, 0, 1, -1),
    (0, 0, -1, 0),
    (0, 0, -1, 1),
    (0, 0, -1, -1),
    (0, 1, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 0, -1),
    (0, 1, 1, 0),
    (0, 1, 1, 1),
    (0, 1, 1, -1),
    (0, 1, -1, 0),
    (0, 1, -1, 1),
    (0, 1, -1, -1),
    (0, -1, 0, 0),
    (0, -1, 0, 1),
    (0, -1, 0, -1),
    (0, -1, 1, 0),
    (0, -1, 1, 1),
    (0, -1, 1, -1),
    (0, -1, -1, 0),
    (0, -1, -1, 1),
    (0, -1, -1, -1),
    (1, 0, 0, 0),
    (1, 0, 0, 1),
    (1, 0, 0, -1),
    (1, 0, 1, 0),
    (1, 0, 1, 1),
    (1, 0, 1, -1),
    (1, 0, -1, 0),
    (1, 0, -1, 1),
    (1, 0, -1, -1),
    (1, 1, 0, 0),
    (1, 1, 0, 1),
    (1, 1, 0, -1),
    (1, 1, 1, 0),
    (1, 1, 1, 1),
    (1, 1, 1, -1),
    (1, 1, -1, 0),
    (1, 1, -1, 1),
    (1, 1, -1, -1),
    (1, -1, 0, 0),
    (1, -1, 0, 1),
    (1, -1, 0, -1),
    (1, -1, 1, 0),
    (1, -1, 1, 1),
    (1, -1, 1, -1),
    (1, -1, -1, 0),
    (1, -1, -1, 1),
    (1, -1, -1, -1),
    (-1, 0, 0, 0),
    (-1, 0, 0, 1),
    (-1, 0, 0, -1),
    (-1, 0, 1, 0),
    (-1, 0, 1, 1),
    (-1, 0, 1, -1),
    (-1, 0, -1, 0),
    (-1, 0, -1, 1),
    (-1, 0, -1, -1),
    (-1, 1, 0, 0),
    (-1, 1, 0, 1),
    (-1, 1, 0, -1),
    (-1, 1, 1, 0),
    (-1, 1, 1, 1),
    (-1, 1, 1, -1),
    (-1, 1, -1, 0),
    (-1, 1, -1, 1),
    (-1, 1, -1, -1),
    (-1, -1, 0, 0),
    (-1, -1, 0, 1),
    (-1, -1, 0, -1),
    (-1, -1, 1, 0),
    (-1, -1, 1, 1),
    (-1, -1, 1, -1),
    (-1, -1, -1, 0),
    (-1, -1, -1, 1),
    (-1, -1, -1, -1),
]

number_of_cycles = 6


def main():
    input = "input.txt"
    active_cubes = parse_input(input)

    for i in range(number_of_cycles):
        active_cubes = do_cycle(active_cubes)

    print(f"active cubes [{len(active_cubes)}]")


def do_cycle(active_cubes):
    possibly_updating_cubes = set()
    updated_active_cubes = set()
    for cube in active_cubes:
        neighbours = get_neighbours(cube)
        possibly_updating_cubes.update(neighbours)

        active_neighbours = [
            True for neighbour in neighbours if neighbour in active_cubes
        ]
        if len(active_neighbours) in range(2, 4):
            updated_active_cubes.add(cube)
    for cube in possibly_updating_cubes:
        if cube in active_cubes:
            # Already handled in previous statement
            continue
        neighbours = get_neighbours(cube)
        active_neighbours = [
            True for neighbour in neighbours if neighbour in active_cubes
        ]
        if len(active_neighbours) == 3:
            updated_active_cubes.add(cube)

    return updated_active_cubes


def get_neighbours(cube):
    neighbours = set()
    for shift in neighbour_shifts:
        x, y, z, w = shift
        neighbours.add(Coordinate(cube.x + x, cube.y + y, cube.z + z, cube.w + w))
    return neighbours


def parse_input(input):
    active_cubes = []
    with open(input) as file:
        for y, line in enumerate(file):
            for x, active_char in enumerate(line):
                is_active = active_char == "#"
                if is_active:
                    active_cubes.append(Coordinate(x, y, 0, 0))
    return active_cubes


if __name__ == "__main__":
    main()
