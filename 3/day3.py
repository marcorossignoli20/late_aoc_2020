input = open("input.txt", "r").read().split()
input = input[1:len(input)]
pos = 3
tree_count = 0
module = len(input[0])

for row in input:
    if row[pos] == '#':
        tree_count = tree_count + 1
    pos = (pos+3)%module

print(tree_count)