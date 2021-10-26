import sys

necessary_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
optional_fields = set(["cid"])


def main():
    input_path = sys.argv[1]

    passports = []
    with open(input_path, "r") as file:
        passports = file.read().split("\n\n")
    return [is_valid_passport(passport) for passport in passports].count(True)


def is_valid_passport(passport):
    passport = passport.replace("\n", " ", -1)
    passport_entries = passport.split(" ")
    present_fields = [entry[:3] for entry in passport_entries]
    return False not in [field in present_fields for field in necessary_fields]


if __name__ == "__main__":
    print(main())
