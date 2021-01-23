f = open("input.txt", "r")
input = f.read().split()

print
res = 0

for num in input:
    for poss in input:
        if (int(num)+int(poss)) == 2020:
            res = int(num)*int(poss)
            break

print(res)