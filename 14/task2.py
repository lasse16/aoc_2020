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
            resolved_addresses = resolve_addresses(address, bitmask)
            for address in resolved_addresses:
                memory[address] = int(value)
        elif instruction_type == "mask":
            bitmask = value
    print(sum(memory.values()))


def resolve_addresses(address, bitmask):
    address_in_binary = "{0:036b}".format(address)
    output = ""
    for value_char, mask_char in zip(address_in_binary, bitmask):
        if mask_char == "X":
            output += mask_char
        elif mask_char == "0":
            output += value_char
        else:
            output += "1"

    unresolved_addresses = [output]
    while any(map(lambda x: "X" in x, unresolved_addresses)):
        possible_resolved_addresses = []
        for address in unresolved_addresses:
            for number in (0, 1):
                possible_resolved_address = address.replace("X", str(number), 1)
                possible_resolved_addresses.append(possible_resolved_address)
        unresolved_addresses = possible_resolved_addresses
    resolved_addresses = unresolved_addresses
    return resolved_addresses


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
