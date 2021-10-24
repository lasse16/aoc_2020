from dataclasses import dataclass


@dataclass
class MemorySaveInstruction:
    value: int
    adress: int

    def execute(self, bit_mask, memory_book):
        return bit_mask, memory_book


@dataclass
class MaskUpdateInstruction:
    value: str

    def execute(self, bit_mask, memory_book):
        return bit_mask, memory_book


def main():
    input = "input.txt"
    instructions = parse_input_into_instructions(input)
    bit_mask = "X" * 36
    memory = dict()
    for instruction in instructions:
        bit_mask, memory = instruction.execute(bit_mask, memory)

    print(sum(memory.values()))


def parse_input_into_instructions(input):
    instructions = []
    with open(input) as file:
        lines = [line.strip() for line in file]
        for line in lines:
            instruction_type, instruction_value = line.split("=")
            instruction_type = instruction_type.strip()
            instruction_value = instruction_value.strip()
            if instruction_type.startswith("mem"):
                value = int(instruction_value)
                adress = int(instruction_type.partition("[")[2].partition("]")[0])
                instruction = MemorySaveInstruction(value, adress)
                instructions.append(instruction)
            elif instruction_type.startswith("mask"):
                value = instruction_value
                instruction = MaskUpdateInstruction(value)
                instructions.append(instruction)
            else:
                raise Exception()
    return instructions


if __name__ == "__main__":
    main()
