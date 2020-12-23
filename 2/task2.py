import sys

def main():
    input = sys.argv[1]
    valid_input_counter = 0
    with open(input,'r') as file:
        for line in file:
            parsed_line = parse_line(line)
            valid_input_counter += int(password_follows_policy(parsed_line))
    return valid_input_counter

def parse_line(line):
    left_side, password = line.split(':')
    range_string, letter = left_side.split(' ')
    lower_limit, upper_limit = range_string.split('-')
    return int(lower_limit),int(upper_limit),letter,password

def password_follows_policy(parsed_line):
    first_position,second_position, letter, password = parsed_line
    letter_in_place = int(password[first_position]==letter) + int(password[second_position]==letter)
    return letter_in_place == 1



if __name__ == "__main__":
    print(main())
