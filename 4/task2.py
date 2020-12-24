import sys
import re

necessary_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
optional_fields = set(["cid"])

def main():
    input_path = sys.argv[1]

    passports =[]
    with open(input_path,'r') as file:
        passports = file.read().split('\n\n')
    return [is_valid_passport(passport) for passport in passports].count(True)

def is_valid_passport(passport):
    passport = passport.replace('\n',' ',-1)
    passport_entries = passport.split(" ")
    present_fields = [entry[:3] for entry in passport_entries]
    necessary_fields_present = False not in [field in present_fields for field in necessary_fields]
    if necessary_fields_present:
        if '' in passport_entries: passport_entries.remove('')
        all_fields_valid = False not in [is_valid_value(*entry.split(':')) for entry in passport_entries]
        if all_fields_valid:
            print(passport)
        return all_fields_valid
    return False

def valid_birth_year(value_string):
    return re.search('\d{4}', value_string) and int(value_string) in range(1920,2003)

def valid_issued_year(value_string):
    return re.search('\d{4}', value_string) and int(value_string) in range(2010,2021)

def valid_expiration_year(value_string):
    return re.search('\d{4}', value_string) and int(value_string) in range(2020,2031)

def valid_height(value_string):
    if not re.search('\d{2,3}[a-z]{2}', value_string):
        return False
    unit = value_string[-2:]
    value = int(value_string[:-2])
    if unit == "in":
        return value in range(50,77)
    elif unit == "cm":
        return value in range(150,194)
    return False

def valid_hair_color(value_string):
    return re.search('#[0-9a-f]{6}', value_string)

def valid_eye_color(value_string):
    return value_string in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def valid_pid(value_string):
    return re.search('\d{9}',value_string)

def valid_cid(value_string):
    return True

def is_valid_value(field_type, value_string):
    return field_type_based_validation.get(field_type, False)(value_string)

field_type_based_validation = {
    "byr": valid_birth_year,
    "iyr": valid_issued_year,
    "eyr": valid_expiration_year,
    "hgt": valid_height,
    "hcl": valid_hair_color,
    "ecl": valid_eye_color,
    "pid": valid_pid,
    "cid": valid_cid
}
if __name__ == "__main__":
    print(main())
