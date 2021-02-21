input = open("input.txt", "r").read().split("\n")
valid = 0
max_seat_id = -1

for code in input:
    lower_bound = 0         # row detection
    higher_bound = 127
    for i in range(7):
        middle = (higher_bound-lower_bound)/2
        if code[i] == "F":
            higher_bound = higher_bound-middle
        if code[i] == "B":
            lower_bound = lower_bound+middle
    if code[6] == "F":
        row = int(lower_bound)
    if code[6] == "B":
        row = int(higher_bound)

    lower_bound = 0         # column detection
    higher_bound = 7
    for i in range(7,10):
        middle = (higher_bound-lower_bound)/2
        if code[i] == "L":
            higher_bound = higher_bound-middle
        if code[i] == "R":
            lower_bound = lower_bound+middle
    if code[9] == "L":
        column = int(lower_bound)
    if code[9] == "R":
        column = int(higher_bound)
    seat_id = (row*8)+column

    if seat_id > max_seat_id:   # check if there is a seat_id higher then the max_seat_id
        max_seat_id = seat_id

print(max_seat_id)