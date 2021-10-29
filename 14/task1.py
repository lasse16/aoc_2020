import re


def main():
    input = "input.txt"
    instructions = parse_input_into_instructions(input)
    bitmask = "X" * 36
    memory = dict()
    for instruction in instructions:
        instruction_type, value = instruction
        if instruction_type.startswith("mem"):
            address = get_address_from_instruction_type(instruction_type)
            value = int(value)
            memory[address] = update_value_with_bitmask(value, bitmask)
        elif instruction_type == "mask":
            bitmask = value
    print(sum(memory.values()))


def update_value_with_bitmask(value, bitmask):
    value_in_binary = "{0:036b}".format(value)
    output = ""
    for value_char, mask_char in zip(value_in_binary, bitmask):
        if mask_char != "X":
            output += mask_char
        else:
            output += value_char
    return int(output, 2)


def update_bitmask(bitmask, update_to_apply):
    output = ""
    for mask_char, update_char in zip(bitmask, update_to_apply):
        if update_char != "X":
            output += update_char
        else:
            output += mask_char
    return output


def get_address_from_instruction_type(instruction_type):
    pattern = r"\[(\d+)\]"
    address = re.search(pattern, instruction_type).group(1)
    return int(address)


def parse_input_into_instructions(input):
    instructions = []
    with open(input) as file:
        for line in file:
            instruction_type, value = line.split("=")
            instruction_type = instruction_type.strip()
            value = value.strip()
            instructions.append((instruction_type, value))
    return instructions


if __name__ == "__main__":
    main()
