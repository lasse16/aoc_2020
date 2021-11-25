#!/usr/bin/env python
import sys

def main():
    input_path = sys.argv[1]
    lines = []
    with open(input_path, 'r') as file:
        lines = [int(x) for x in file.read().splitlines()]
    solution_task1 = 105950735
    solution = 0
    for i, line in enumerate(lines):
        range_counter = 1
        sum_ = line
        while sum_ < solution_task1:
            sum_ += lines[i + range_counter]
            range_counter += 1
        if sum_ == solution_task1 and range_counter > 1:
            solution =  lines[i:i+range_counter]
    print(( sum(solution),solution_task1 ))
    print(min(solution) + max(solution))
    return solution


if __name__ == "__main__":
    print(main())

