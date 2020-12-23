from pathlib import Path
import bisect

def main():
    current_working_directory = Path.cwd()
    input_path = current_working_directory / "input.txt"

    sorted_numbers = []
    with open( input_path ) as file:
        for line in file:
            number = int(line)
            bisect.insort_left(sorted_numbers, number)
    for index, item in enumerate(sorted_numbers):
        start = index + 1
        end = len(sorted_numbers) -1
        while(start < end):
            lower_element = sorted_numbers[start]
            upper_element = sorted_numbers[end]
            sum_of_elements =item + lower_element + upper_element
            if sum_of_elements == 2020:
                return item,lower_element,upper_element
            elif sum_of_elements > 2020:
                end -= 1
            else:
                start += 1

if __name__ == "__main__":
    print(main())
