from dataclasses import dataclass


@dataclass
class Ticket:
    numbers: list


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
    invalid_numbers = []
    for ticket in nearby_tickets:
        for number in ticket.numbers:
            if not any([rule.in_range(number) for rule in rules]):
                invalid_numbers.append(number)
    print(sum(invalid_numbers))


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
