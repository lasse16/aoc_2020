def main():
    input = "input.txt"
    with open(input) as file:
        next(file)
        bus_ids = next(file).strip().split(",")
        bus_ids_and_time_offset = enumerate(bus_ids)
        bus_ids_and_offset_in_use = []
        for offset, bus_id in bus_ids_and_time_offset:
            if bus_id != "x":
                bus_ids_and_offset_in_use.append((int(bus_id), offset))
        print(bus_ids_and_offset_in_use)
        max_bus_id_and_offset = max(bus_ids_and_offset_in_use, key=lambda x: x[0])
        bus_ids_and_offset_in_use = shift_offsets(
            bus_ids_and_offset_in_use, max_bus_id_and_offset[1]
        )
        print(bus_ids_and_offset_in_use)
        solution_found = False
        multiples = generate_multiples(max_bus_id_and_offset[0])
        while not solution_found:
            multiples_found = []
            multiple = next(multiples)
            for bus_id, offset in bus_ids_and_offset_in_use:
                if not is_multiple_of(multiple + offset, bus_id):
                    break
                multiples_found.append(True)
            solution_found = len(multiples_found) == len(bus_ids_and_offset_in_use)
            if solution_found:
                print(multiple)

            if len(multiples_found) > 2:
                print(f"{multiple} with {len(multiples_found)}")


def shift_offsets(bus_ids_and_offsets, amount):
    return [(bus_id, offset - amount) for bus_id, offset in bus_ids_and_offsets]


def generate_multiples(multiple_base):
    num = 1
    while True:
        yield multiple_base * num
        num += 1


def is_multiple_of(target, multiple_base):
    return target % multiple_base == 0


if __name__ == "__main__":
    main()
