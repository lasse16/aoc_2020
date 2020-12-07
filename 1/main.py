from pathlib import Path
import bisect
def main():
    current_working_directory = Path.cwd()
    input_path = current_working_directory / "input.txt"

    parity_numbers = {0: [], 1:[]}
    with open( input_path ) as file:
        for line in file:
            number = int(line)
            bisect.insort_left(parity_numbers[number % 2 ], number)

    for parity in parity_numbers.values():
        min_element = min(parity)
        corresponding_max = 2020 - min_element
        cut_off_by_max = bisect.bisect_left(parity, corresponding_max)
        if parity[cut_off_by_max] == corresponding_max:
            # corresponding element to min exists in array
            print("corresponding min value found")
            return min_element * parity[cut_off_by_max]
        parity = parity[:cut_off_by_max]
        while parity:
            min_element = parity[0]
            max_element = parity[-1]
            sum_extrema = min_element + max_element
            if sum_extrema > 2020:
                parity=parity[:-1]
            elif sum_extrema < 2020:
                parity=parity[1:]
            else:
                print(f"pair found {min_element},{max_element}")
                return min_element * max_element
    return -1

if __name__ == "__main__":
    print(main())
