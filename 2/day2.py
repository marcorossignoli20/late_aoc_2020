input = open("input.txt", "r").read().split("\n")

result = 0
for row in input:
    tokens = row.split(" ")
    if len(tokens) > 2:
        boundaries = tokens[0].split("-")
        letter = tokens[1][0]
        password = tokens[2]
        left_bound = int(boundaries[0])
        right_bound = int(boundaries[1])
        count = 0
        for c in password:
            if c == letter:
                count = count+1
        if count >= left_bound and count <= right_bound:
            result = result+1
print(result)



