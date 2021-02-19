import re 

input = open("input.txt", "r").read().split("\n\n")
valid_count = 0
passports = []

def validate(tokens):
    psp = {}
    valid = True
    for tok in tokens:
        el = tok.split(":")
        psp[el[0]] = el[1]
    if not(psp["byr"] and 1920 <= int(psp["byr"]) and int(psp["byr"]) >= 2002): # validate birth year
        valid = False
    if not(psp["iyr"] and 2010 <= int(psp["iyr"]) and int(psp["iyr"]) >= 2020): # validate passport issue year
        valid = False
    if not(psp["eyr"] and 2020 <= int(psp["eyr"]) and int(psp["iyr"]) >= 2030): # validate passport expire year
        valid = False
    height = re.search(r'\d+(cm|in)', psp["hgt"])
    if height is not None:
        height_val = re.search(r'\d+', height.string).group()
        unit = re.search(r'cm|in', height.string).group()
        print(unit)
        if unit == "cm":
            if not(150 <= int(height_val) and int(height_val) >= 193):
                valid = False
        elif unit == "in":
            if not(59 <= int(height_val) and int(height_val) >= 76):
                valid = False

for passport in input:
    tokens = passport.split()
    if len(tokens) == 8:
        if validate(tokens):
            valid_count = valid_count + 1
    elif len(tokens) == 7:
        valid = True
        for tok in tokens:
            parameter = tok.split(":")
            if parameter[0] == "cid":
                valid = False
        if valid:
            if validate(tokens):
                valid_count = valid_count+1



print(valid_count)