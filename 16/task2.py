from dataclasses import dataclass


@dataclass
class Ticket:
    numbers: list

    def __iter__(self):
        return iter(self.numbers)


@dataclass
class Rule:
    field_name: str
    range1: range
    range2: range

    def in_range(self, value) -> bool:
        return value in self.range1 or value in self.range2


def main():
    input = "input.txt"
    rules, own_ticket, nearby_tickets = parse_input(input)
    tickets_to_remove = []
    for ticket in nearby_tickets:
        for number in ticket.numbers:
            if not any([rule.in_range(number) for rule in rules]):
                tickets_to_remove.append(ticket)
                break
    for ticket in tickets_to_remove:
        nearby_tickets.remove(ticket)
    tickets = nearby_tickets + [own_ticket]
    ticket_values = list(zip(*tickets))
    field_options = {k: set() for k in range(20)}
    rule_options = {k: set() for k in [rule.field_name for rule in rules]}
    for field_index, value_class in enumerate(ticket_values):
        for rule in rules:
            if check_value_against_rule(value_class, rule):
                field_options[field_index].add(rule.field_name)
                rule_options[rule.field_name].add(field_index)
    rule_options_sorted_by_option_amount = sorted(
        rule_options.items(), key=lambda x: len(x[1])
    )
    assigned_field_indices = set()
    assigned_rules = dict()
    for rule, options in rule_options_sorted_by_option_amount:
        remaining_options = options - assigned_field_indices
        if len(remaining_options) == 1:
            field_index = list(remaining_options)[0]
            assigned_rules[rule] = field_index
            assigned_field_indices.add(field_index)
    print(assigned_rules)
    product = 1
    for value in [
        "departure location",
        "departure station",
        "departure platform",
        "departure track",
        "departure date",
        "departure time",
    ]:
        product *= own_ticket.numbers[assigned_rules[value]]
    print(product)


def check_value_against_rule(values, rule):
    for value in values:
        if not rule.in_range(value):
            return False
    return True


def parse_input(input):
    with open(input) as file:
        lines = file.read()
    rules, own_ticket, nearby_tickets = lines.split("\n\n")
    parsed_rules = []
    for rule in rules.splitlines(keepends=False):
        field_name, range_strings = rule.split(":")
        ranges = [range.strip() for range in range_strings.split(" or ")]
        parsed_ranges = []
        for _range in ranges:
            range_start, range_end = _range.split("-")
            parsed_range = range(int(range_start), int(range_end) + 1)
            parsed_ranges.append(parsed_range)
        rule = Rule(field_name, parsed_ranges[0], parsed_ranges[1])
        parsed_rules.append(rule)

    ticket_string = own_ticket.splitlines(keepends=False)[1]
    own_ticket = Ticket([int(number) for number in ticket_string.split(",")])

    nearby_tickets_string = nearby_tickets.splitlines(keepends=False)[1:]
    parsed_tickets = []
    for ticket_string in nearby_tickets_string:
        ticket = Ticket([int(number) for number in ticket_string.split(",")])
        parsed_tickets.append(ticket)
    return parsed_rules, own_ticket, parsed_tickets


if __name__ == "__main__":
    main()
