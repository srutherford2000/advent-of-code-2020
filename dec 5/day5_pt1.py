#file_name=input('enter a file name')
file_name = "input.txt"
in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(line.strip())

in_file.close()


def getSeatID(letters):
    frontBack = letters[:7]
    leftRight = letters[7:]
    range_fb = [0,127]
    range_lr = [0,7]
    for let in frontBack:
        current_set = range_fb[1] - range_fb[0]
        current_set //=2
        new_limit = current_set + range_fb[0]
        if let == "B":
            range_fb[0] = new_limit+1
        else:
            range_fb[1] = new_limit
    for let in leftRight:
        current_set = range_lr[1] - range_lr[0]
        current_set //=2
        new_limit = current_set + range_lr[0]
        if let == "R":
            range_lr[0] = new_limit+1
        else:
            range_lr[1] = new_limit

    #print(range_fb[0])
    #print(range_lr[0])
    return range_fb[0]*8 + range_lr[0]

max_seat_id = 0
for line in lines:
    Id = getSeatID(line)
    if Id > max_seat_id:
        max_seat_id = Id
print(max_seat_id)
