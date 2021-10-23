import math


def main():
    input = "input.txt"
    bus_ids_and_offset_in_use = parse_input_into_bus_ids_and_offset_in_use(input)
    bus_ids_and_offset_in_use = sorted(bus_ids_and_offset_in_use, key=lambda x: x[0])

    bus_ids, _ = zip(*bus_ids_and_offset_in_use)

    # All bus ids are primes
    least_common_multiplier = math.prod(bus_ids)

    timestep = 1
    step_interval = 1

    for bus_id, offset in bus_ids_and_offset_in_use:
        # Everything after least_common_multiplier is the same modulo, so no solution should be possible to find
        while timestep < least_common_multiplier:
            if is_multiple_of(timestep + offset, bus_id):
                step_interval *= bus_id
                break
            timestep += step_interval
    print(f" solution {timestep}")


def parse_input_into_bus_ids_and_offset_in_use(input):
    with open(input) as file:
        next(file)
        bus_ids = next(file).strip().split(",")
        bus_ids_and_time_offset = enumerate(bus_ids)
        bus_ids_and_offset_in_use = []
        for offset, bus_id in bus_ids_and_time_offset:
            if bus_id != "x":
                bus_ids_and_offset_in_use.append((int(bus_id), offset))

        return bus_ids_and_offset_in_use


def is_multiple_of(target, multiple_base):
    return target % multiple_base == 0


if __name__ == "__main__":
    main()
