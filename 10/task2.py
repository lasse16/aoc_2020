cache = dict()


def main():
    input = "input.txt"
    adapters = parse_input_into_adapter(input)
    sorted_adapters = sorted(adapters)
    sorted_adapters.append(sorted_adapters[-1] + 3)
    sorted_adapters.insert(0, 0)
    print(paths_to_end(0, sorted_adapters))


def paths_to_end(i, adapters):
    if i == len(adapters) - 1:
        return 1
    if i in cache:
        return cache[i]
    possible_paths = sum(
        [
            paths_to_end(j, adapters)
            for j in range(i + 1, min(i + 4, len(adapters)))
            if adapters[j] - adapters[i] <= 3
        ]
    )
    cache[i] = possible_paths
    return possible_paths


def parse_input_into_adapter(input):
    with open(input) as file:
        adapters = [int(line.strip()) for line in file]
        return adapters


if __name__ == "__main__":
    main()
