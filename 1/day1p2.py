f = open("input.txt", "r")
input = f.read().split()

print
res = 0

for num in input:
    for poss in input:
        for poss2 in input:
            if (int(num)+int(poss)+int(poss2)) == 2020:
                        res = int(num)*int(poss)*int(poss2)
                        break

print(res)