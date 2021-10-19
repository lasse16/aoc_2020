from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class BagType:
    color: str


def main():
    input_file = "/home/lasse/src/aoc_2020/7/input.txt"
    containing_rule_set = parse_input_into_rule_set(input_file)
    target = BagType("shiny gold")
    possible_containers = {target}
    prev_possible_containers = set()
    while possible_containers != prev_possible_containers:
        prev_possible_containers = possible_containers.copy()
        for containing_bag, contained_bags in containing_rule_set.items():
            for bag in prev_possible_containers:
                if bag in contained_bags:
                    possible_containers.add(containing_bag)

    print(len(possible_containers))


def parse_input_into_rule_set(input_file):
    containing_rule_set = dict()
    with open(input_file, "r") as f:
        for line in f:
            words = line.split()
            containing_bag_color = " ".join(words[:2])
            containing_bag_type = BagType(containing_bag_color)
            words = words[4:]
            contained_bags = []
            while words:
                words, contained_bag_type = get_one_bag_type(words)
                contained_bags.append(contained_bag_type)
            containing_rule_set[containing_bag_type] = contained_bags
    return containing_rule_set


def get_one_bag_type(words):
    bag_amount = words[0]
    bag_color = " ".join(words[1:3])
    return words[4:], BagType(bag_color)


if __name__ == "__main__":
    main()
