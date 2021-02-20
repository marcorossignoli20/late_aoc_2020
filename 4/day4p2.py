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
    
    if not(1920 <= int(psp["byr"]) and int(psp["byr"]) <= 2002): # validate birth year
        valid = False
    
    if not(2010 <= int(psp["iyr"]) and int(psp["iyr"]) <= 2020): # validate passport issue year
        valid = False
    
    if not(2020 <= int(psp["eyr"]) and int(psp["eyr"]) <= 2030): # validate passport expire year
        valid = False

    height = re.search(r'\d+(cm|in)', psp["hgt"]) # validate height
    if height is not None:
        height_val = re.search(r'\d+', height.string).group()
        unit = re.search(r'cm|in', height.string).group()
        if unit == "cm":
            if not(150 <= int(height_val) and int(height_val) <= 193):
                valid = False
        elif unit == "in":
            if not(59 <= int(height_val) and int(height_val) <= 76):
                valid = False
    else:
        valid = False
    
    hair_color = re.search(r'#[a-f0-9]{6}', psp['hcl']) # validate hair color
    if hair_color is None:
        valid = False
    if len(psp['hcl']) != 7:
        valid = False
    
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] # validate eyes
    if psp['ecl'] not in eye_colors:
        valid = False
    
    pid = re.search(r'\d{9}', psp['pid']) # validate password id
    if pid is None:
        valid = False
    if len(psp['pid']) != 9:
        valid = False

    if valid:
        print(psp)
    return valid

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