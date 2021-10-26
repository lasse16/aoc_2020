import re

necessary_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
optional_fields = set(["cid"])

# Attempted soution, not finding the error
def main():
    input_path = "input.txt"

    passports = parse_input_into_passports(input_path)
    passports_with_required_fields = [
        passport for passport in passports if are_required_fields_present(passport)
    ]
    valid_passports = [
        passport
        for passport in passports_with_required_fields
        if are_all_fields_valid(passport)
    ]
    return len(valid_passports)


def are_all_fields_valid(passport):
    passport_entries = passport.split(" ")
    valid_fields = []
    for entry in passport_entries:
        field_type, value = entry.split(":")
        valid_fields.append(is_valid_value(field_type, value))
    return all(valid_fields)


def parse_input_into_passports(input):
    passports = []
    with open(input, "r") as file:
        passports = [
            passport.replace("\n", " ", -1).strip()
            for passport in file.read().split("\n\n")
        ]
    return passports


def are_required_fields_present(passport):
    passport_entries = passport.split(" ")
    present_fields = [entry[:3] for entry in passport_entries]
    necessary_fields_present = all(
        [field in present_fields for field in necessary_fields]
    )
    return necessary_fields_present


def valid_birth_year(value_string):
    return re.search("\d{4}", value_string) and int(value_string) in range(1920, 2003)


def valid_issued_year(value_string):
    return re.search("\d{4}", value_string) and int(value_string) in range(2010, 2021)


def valid_expiration_year(value_string):
    return re.search("\d{4}", value_string) and int(value_string) in range(2020, 2031)


def valid_height(value_string):
    if not re.search("\d{2,3}[a-z]{2}", value_string):
        return False
    unit = value_string[-2:]
    value = int(value_string[:-2])
    if unit == "in":
        return value in range(50, 77)
    elif unit == "cm":
        return value in range(150, 194)
    return False


def valid_hair_color(value_string):
    valid_color = bool(re.search("#[0-9a-f]{6}", value_string))
    return valid_color


def valid_eye_color(value_string):
    return value_string in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def valid_pid(value_string):
    return bool(re.search("\d{9}", value_string))


def valid_cid(value_string):
    return True


def is_valid_value(field_type, value_string):
    return field_type_based_validation.get(field_type, lambda x: False)(value_string)


field_type_based_validation = {
    "byr": valid_birth_year,
    "iyr": valid_issued_year,
    "eyr": valid_expiration_year,
    "hgt": valid_height,
    "hcl": valid_hair_color,
    "ecl": valid_eye_color,
    "pid": valid_pid,
    "cid": valid_cid,
}
if __name__ == "__main__":
    print(main())
