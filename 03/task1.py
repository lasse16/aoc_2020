import sys

def main():
    slope = (1, 3)
    input_path = sys.argv[1]
    lines = []
    with open(input_path) as f:
            lines = [line.rstrip() for line in f]

    hit_fields = get_hitting_fields(lines, slope)
    hit_trees = hit_fields.count('#')
    return hit_trees

def get_hitting_fields(input, slope):
    downwards, sidewards = slope
    hit_fields = ""
    for index, line in enumerate(input):
        if index % downwards == 0:
            hit_fields += line[(index * sidewards)%len(line)]
    return hit_fields




if __name__ == "__main__":
    print(main())
