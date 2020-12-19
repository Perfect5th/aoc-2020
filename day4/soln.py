import re

from utils import input_groups


fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
rules = {
    'byr': [r'\sbyr:(\d{4})\s', 1920, 2002],
    'iyr': [r'\siyr:(\d{4})\s', 2010, 2020],
    'eyr': [r'\seyr:(\d{4})\s', 2020, 2030],
    'hgt': [r'\shgt:(\d+)(cm|in)\s'],
    'hcl': [r'\shcl:#[0-9a-f]{6}\s'],
    'ecl': [r'\secl:(amb|blu|brn|gry|grn|hzl|oth)\s'],
    'pid': [r'\spid:\d{9}\s'],
}

def read_passport(ipt):
    passport = ''
    for l in ipt:
        if l == '\n':
            yield passport
            passport = ''
        
        passport += l


def solve1(ipt):
    valid = 0
    for passport in input_groups(ipt):
        is_valid = True

        for f in fields:
            if f not in f' {" ".join(passport)} ':
                is_valid = False
                break
        
        if is_valid:
            valid += 1

    print(valid)


def validate(field, passport):
    rule = rules[field]
    found = re.search(rule[0], f' {" ".join(passport)} ')

    if not found:
        return False

    if len(rule) == 3:
        value = int(found.group(1))
        return value >= rule[1] and value <= rule[2]

    if field == 'hgt':
        value = int(found.group(1))
        if found.group(2) == 'cm':
            return value >= 150 and value <= 193
        return value >= 59 and value <= 76

    return True


def solve2(ipt):
    valid = 0
    for passport in input_groups(ipt):
        is_valid = True

        for f in fields:
            if not validate(f, passport):
                is_valid = False
                break
        
        if is_valid:
            valid += 1

    print(valid)