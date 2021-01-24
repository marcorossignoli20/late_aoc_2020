input = open("input.txt", "r").read().split()
input = input[1:len(input)]

class Path:
  def __init__(self, num):
    self.num = num
    self.pos = num
    self.tree_count = 0

v = []
v.append(Path(1))
v.append(Path(3))
v.append(Path(5))
v.append(Path(7))
tree_count = 0
alt_tree_count = 0
alt_pos = 1
count = 1
module = len(input[0])

for row in input:
    for p in v:
        if row[p.pos] == '#':
            p.tree_count = p.tree_count + 1
        p.pos = (p.pos + p.num) % module
    if count > 1 and count % 2 == 0:
        if row[alt_pos] == '#':
            alt_tree_count = alt_tree_count + 1
        alt_pos = (alt_pos + 1) % module 
    count = count+1

total = alt_tree_count
for p in v:
    total = total * p.tree_count 

print(total)

class Path:
  def __init__(self, num):
    self.num = num
    self.pos = num
    self.tree_count = 0