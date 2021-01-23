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
        if (password[left_bound-1] == letter) ^ (password[right_bound-1] == letter):
            result = result+1
print(result)