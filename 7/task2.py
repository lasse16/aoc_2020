#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True, eq=True)
class BagType:
    color: str


@dataclass(frozen=True, eq=True)
class Contained_Bag:
    type: BagType
    amount: int

    def __iter__(self):
        return iter((self.type, self.amount))


global containing_rule_set


def main():
    global containing_rule_set
    containing_rule_set = parse_input_into_rule_set("input.txt")
    # Remove 1 as shiny gold does not count towards contained bag total
    amount_contained_bags = get_contained_bag_count(BagType("shiny gold")) - 1
    print(amount_contained_bags)


def parse_input_into_rule_set(input_file: str):
    containing_rule_set = dict()
    with open(input_file, "r") as f:
        for line in f:
            words = line.split()
            containing_bag_color: str = " ".join(words[:2])
            containing_bag_type: BagType = BagType(containing_bag_color)
            words: list = words[4:]
            contained_bags = []
            while words:
                words, contained_bag_type = get_one_contained_bag_and_amount(words)
                if contained_bag_type:
                    contained_bags.append(contained_bag_type)
            containing_rule_set[containing_bag_type] = contained_bags
    return containing_rule_set


def get_one_contained_bag_and_amount(words):
    if words == ["no", "other", "bags."]:
        return [], None
    bag_amount: int = int(words[0])
    bag_color: str = " ".join(words[1:3])
    return words[4:], Contained_Bag(BagType(bag_color), bag_amount)


def get_contained_bag_count(bag: BagType):
    contained_bags_and_counts = containing_rule_set[bag]
    if not contained_bags_and_counts:
        return 1
    else:
        total: int = 1
        for contained_bag in contained_bags_and_counts:
            total += contained_bag.amount * get_contained_bag_count(contained_bag.type)
        return total


if __name__ == "__main__":
    main()
