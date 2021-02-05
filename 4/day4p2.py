input = open("C:\\Users\\marcor.BF\\Documents\\Personal\\late_aoc\\4\\input.txt", "r").read().split("\n\n")
valid_count = 0

for passport in input:
    tokens = passport.split()
    if len(tokens) == 8:
        valid_count = valid_count + 1
    elif len(tokens) == 7:
        for tok in tokens:
            parameter = tok.split(":")
            if parameter[0] == "cid":
                valid_count = valid_count - 1
                break
        valid_count = valid_count + 1
print(valid_count)