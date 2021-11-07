#!/usr/bin/env python
import math
import sys

max_vertical = 128
max_horizontal = 8
markers_vertical=('F', 'B')
markers_horizontal=('L', 'R')
def main():
    input_path = sys.argv[1]
    board_passes = []
    with open(input_path,'r') as file:
        for line in file:
            vertical_placement = line[:7]
            horizontal_placement = line[7:]
            row = calculate_vertical_seat(vertical_placement)
            column = calculate_horizontal_seat(horizontal_placement)
            board_pass = (row, column, row * 8 + column)
            print(board_pass)
            board_passes += [board_pass]
    return max(board_passes, key= lambda x: x[2])

def calculate_vertical_seat(instructions):
    instructions = instructions.replace(markers_vertical[0],'L')
    instructions = instructions.replace(markers_vertical[1],'H')
    return binary_select(instructions,max_vertical)[0]

def calculate_horizontal_seat(instructions):
    instructions = instructions.replace(markers_horizontal[0],'L')
    instructions = instructions.replace(markers_horizontal[1],'H')
    return binary_select(instructions,max_horizontal)[0]

def binary_select(instructions, max_):
    instructions = instructions.strip()
    lower_end = 0
    upper_end = max_
    if len(instructions) > math.log(upper_end - lower_end, 2):
        raise ValueError("Too many instructions")
    range_ = range(lower_end,upper_end)
    while(instructions):
        half = int(len(range_)/2) + lower_end
        current_instruction = instructions[0]
        if current_instruction == 'L':
            upper_end = half
        elif current_instruction == 'H':
            lower_end = half
        else:
            raise ValueError("Unknown insrtruction")
        instructions = instructions[1:]
        range_ = range(lower_end,upper_end)
    return range_

if __name__ == "__main__":
    print(main())
