import sys

def main():
    input = sys.argv[1]
    valid_input_counter = 0
    with open(input,'r') as file:
        for line in file:
            range_, letter, password = parse_line(line)
            valid_input_counter += int(password.count(letter) in range_)
    return valid_input_counter

def parse_line(line):
    left_side, password = line.split(':')
    range_string, letter = left_side.split(' ')
    lower_limit, upper_limit = range_string.split('-')
    range_ = range(int(lower_limit), int(upper_limit) + 1)
    return range_,letter,password

if __name__ == "__main__":
    print(main())
