import sys
from functools import reduce

# This solution is not accepted but I can not make out the error right now :/ 
def main():
    slopes = [(1,1),(1, 3), (1,5),(1,7),(2,1)]
    input_path = sys.argv[1]
    lines = []
    with open(input_path) as f:
            lines = [line.rstrip() for line in f]

    hit_trees = []
    for slope in slopes:
        hit_fields = get_hitting_fields(lines, slope)
        hit_trees += [hit_fields.count('#')]
    print(reduce(lambda x, y: x*y, hit_trees, 1))
    return hit_trees

def get_hitting_fields(input, slope):
    downwards, sidewards = slope
    hit_fields = ""
    for index, line in enumerate(input):
        if index % downwards == 0:
            index_hit_field = (index * sidewards)%len(line)
            hit_fields += line[index_hit_field]
    return hit_fields




if __name__ == "__main__":
    print(main())
