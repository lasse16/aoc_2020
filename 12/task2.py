from dataclasses import dataclass
from enum import IntEnum
import math


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
    waypoint_position = (10, 1)
    for instruction in instructions:
        position, rotation, waypoint_position = execute_instruction(
            instruction, position, rotation, waypoint_position
        )
    print(position)
    print(f"manhattan distance {sum([abs(val) for val in position])}")


def execute_instruction(
    instruction, starting_position, starting_direction, waypoint_position
):
    action = instruction.action
    value = instruction.value
    position = starting_position
    rotation = starting_direction
    if action == Action.EAST:
        x, y = waypoint_position
        x += value
        waypoint_position = (x, y)
    elif action == Action.SOUTH:
        x, y = waypoint_position
        y -= value
        waypoint_position = (x, y)
    elif action == Action.WEST:
        x, y = waypoint_position
        x -= value
        waypoint_position = (x, y)
    elif action == Action.NORTH:
        x, y = waypoint_position
        y += value
        waypoint_position = (x, y)
    elif action == Action.LEFT:
        waypoint_position = rotate_around_origin_2D(position, waypoint_position, value)
    elif action == Action.RIGHT:
        waypoint_position = rotate_around_origin_2D(position, waypoint_position, -value)
    elif action == Action.FORWARD:
        movement = get_local_coords(position, waypoint_position)
        scaled_movement = (value * movement[0], value * movement[1])
        position = tuple([sum(x) for x in zip(position, scaled_movement)])
        waypoint_position = get_absolute_coords(position, movement)

    return position, rotation, waypoint_position


def rotate_around_origin_2D(origin, point, angle):
    angle = math.radians(angle)
    cos_angle = math.cos(angle)
    sin_angle = math.sin(angle)
    x_local, y_local = get_local_coords(origin, point)
    x_local_updated = x_local * cos_angle - y_local * sin_angle
    y_local_updated = x_local * sin_angle + y_local * cos_angle
    return get_absolute_coords(origin, (x_local_updated, y_local_updated))


def get_local_coords(origin, point):
    x, y = point
    x_origin, y_origin = origin
    x_local = x - x_origin
    y_local = y - y_origin
    return x_local, y_local


def get_absolute_coords(origin, point):
    x, y = point
    x_origin, y_origin = origin
    x_global = x + x_origin
    y_global = y + y_origin
    return x_global, y_global


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
