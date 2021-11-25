#!/usr/bin/env python
import sys

def main():
    input_path = sys.argv[1]
    lines = []
    with open(input_path, 'r') as file:
        lines = [int(x) for x in file.read().splitlines()]
    current_index = 25
    preamble= lines[current_index - 25:current_index]
    while two_sum_exists(preamble,lines[current_index]):
        current_index += 1
        preamble= lines[current_index - 25:current_index]
    print( lines[current_index])

def two_sum_exists(options, target):
    for num in options:
        complement = target - num
        if complement == num: continue
        if complement in options:
            return True
    return False


if __name__ == "__main__":
    main()

