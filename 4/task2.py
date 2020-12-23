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

def is_valid_value(field_type, value_string):
    # This is making me puke in terms of readibility, thankful for any fixes
    if(field_type == "byr"):
        return re.search('\d{4}', value_string) and int(value_string) in range(1920,2003)
    elif(field_type == "iyr"):
        return re.search('\d{4}', value_string) and int(value_string) in range(2010,2021)
    elif(field_type == "eyr"):
        return re.search('\d{4}', value_string) and int(value_string) in range(2020,2031)
    elif(field_type == "hgt"):
        if not re.search('\d{2,3}[a-z]{2}', value_string):
            return False
        unit = value_string[-2:]
        value = int(value_string[:-2])
        if unit == "in":
            return value in range(50,78)
        elif unit == "cm":
            return value in range(150,194)
        return False
    elif field_type == "hcl":
        return re.search('#[0-9a-f]{6}', value_string)
    elif field_type == "ecl":
        return value_string in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif field_type == "pid":
        return re.search('\d{9}',value_string)
    elif field_type == "cid":
        return True
    else:
        return False

if __name__ == "__main__":
    print(main())
