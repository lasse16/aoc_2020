def main():
    input = "input.txt"
    adapters = parse_input_into_adapter(input)
    sorted_adapters = sorted(adapters)
    sorted_adapters.append(sorted_adapters[-1] + 3)
    sorted_adapters.insert(0, 0)
    differences = [
        abs(sorted_adapters[i] - sorted_adapters[i + 1])
        for i in range(len(sorted_adapters) - 1)
    ]
    print(differences.count(1) * differences.count(3))


def parse_input_into_adapter(input):
    with open(input) as file:
        adapters = [int(line.strip()) for line in file]
        return adapters


if __name__ == "__main__":
    main()
