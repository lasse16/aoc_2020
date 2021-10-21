from dataclasses import dataclass
from enum import IntEnum


class Action(IntEnum):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3
    LEFT = 4
    RIGHT = 5
    FORWARD = 6


@dataclass
class Instruction(object):
    action: Action
    value: int


def main():
    input = "input.txt"
    instructions = parse_input_into_instructions(input)
    rotation = Action.EAST
    position = (0, 0)
    for instruction in instructions:
        position, rotation = execute_instruction(instruction, position, rotation)
    print(position)
    print(f"manhattan distance {sum([abs(val) for val in position])}")


def execute_instruction(instruction, starting_position, starting_direction):
    action = instruction.action
    value = instruction.value
    position = starting_position
    rotation = starting_direction
    if action == Action.EAST:
        x, y = position
        x += value
        position = (x, y)
    elif action == Action.SOUTH:
        x, y = position
        y -= value
        position = (x, y)
    elif action == Action.WEST:
        x, y = position
        x -= value
        position = (x, y)
    elif action == Action.NORTH:
        x, y = position
        y += value
        position = (x, y)
    elif action == Action.LEFT:
        rotation = get_rotation_from_angle(-value, rotation)
    elif action == Action.RIGHT:
        rotation = get_rotation_from_angle(value, rotation)
    elif action == Action.FORWARD:
        position, rotation = execute_instruction(
            Instruction(rotation, value), position, rotation
        )

    return position, rotation


def get_rotation_from_angle(angle, starting_direction):
    angle = (angle / 90) % 4
    new_direction = Action((angle + int(starting_direction)) % 4)
    return new_direction


def parse_input_into_instructions(input):
    instructions = []
    with open(input) as file:
        lines = [line.strip() for line in file]
        for line in lines:
            action = get_action_from_char(line[0])
            value = int(line[1:])
            instructions.append(Instruction(action, value))
    return instructions


def get_action_from_char(c):
    if c == "E":
        return Action.EAST
    elif c == "S":
        return Action.SOUTH
    elif c == "W":
        return Action.WEST
    elif c == "N":
        return Action.NORTH
    elif c == "L":
        return Action.LEFT
    elif c == "R":
        return Action.RIGHT
    elif c == "F":
        return Action.FORWARD
    else:
        raise Exception()


if __name__ == "__main__":
    main()
