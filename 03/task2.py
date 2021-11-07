from functools import reduce


def main():
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    input_path = "input.txt"
    lines = []
    with open(input_path) as f:
        lines = [line.rstrip() for line in f]

    hit_trees = []
    for slope in slopes:
        hit_fields = get_hitting_fields(lines, slope)
        hit_trees += [hit_fields.count("#")]
    print(reduce(lambda x, y: x * y, hit_trees, 1))
    return hit_trees


def get_hitting_fields(input, slope):
    downwards, sidewards = slope
    hit_fields = ""
    slope_applied = 0
    for index, line in enumerate(input):
        if index % downwards == 0:
            index_hit_field = (slope_applied * sidewards) % len(line)
            hit_fields += line[index_hit_field]
            slope_applied += 1
    return hit_fields


if __name__ == "__main__":
    print(main())
